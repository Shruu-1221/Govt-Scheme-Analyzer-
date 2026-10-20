import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "government_scheme_db"
}

SCHEME_COLUMNS = """
    scheme_id,
    scheme_name,
    description,
    min_age,
    max_age,
    income_limit,
    min_10th_marks,
    min_12th_marks,
    education,
    category,
    gender,
    state,
    benefits,
    documents,
    application_link,
    course,
    year,
    hostel_status
"""


def connect_database():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None


def get_all_schemes():
    conn = connect_database()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT {SCHEME_COLUMNS} FROM schemes ORDER BY scheme_id")
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print("Database error:", e)
        return []
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass


def _text(value):
    return "" if value is None else str(value).strip()


def _normal(value):
    return _text(value).casefold()


def _is_all(value):
    return _normal(value) in ("", "all", "any", "any state", "all states")


def _contains_allowed(student_value, scheme_value):
    if _is_all(scheme_value):
        return True

    student_value = _normal(student_value)
    allowed = [_normal(x) for x in _text(scheme_value).split(",")]
    return student_value in allowed


def _education_matches(student_value, scheme_value):
    if _is_all(scheme_value):
        return True

    student_value = _normal(student_value)
    required = _normal(scheme_value)

    if student_value == required:
        return True

    return required in student_value or student_value in required


def _course_matches(student_value, scheme_value):
    if _is_all(scheme_value):
        return True

    student_value = _normal(student_value)
    required = _normal(scheme_value)

    if student_value == required:
        return True

    return required in student_value or student_value in required


def check_eligibility(student, scheme):
    reasons = []

    min_age = scheme.get("min_age")
    max_age = scheme.get("max_age")
    income_limit = scheme.get("income_limit")
    min10 = scheme.get("min_10th_marks")
    min12 = scheme.get("min_12th_marks")

    if min_age is not None and student["age"] < int(min_age):
        reasons.append(f"Minimum age required: {min_age}")

    if max_age is not None and student["age"] > int(max_age):
        reasons.append(f"Maximum age allowed: {max_age}")

    if income_limit is not None and student["income"] > float(income_limit):
        reasons.append(
            f"Family income must be ≤ ₹{float(income_limit):,.0f}"
        )

    if min10 is not None and student["marks10"] < float(min10):
        reasons.append(f"Minimum 10th marks required: {float(min10):g}%")

    if min12 is not None and student["marks12"] < float(min12):
        reasons.append(f"Minimum 12th marks required: {float(min12):g}%")

    if not _education_matches(student["education"], scheme.get("education")):
        reasons.append(f"Education required: {scheme.get('education')}")

    if not _contains_allowed(student["category"], scheme.get("category")):
        reasons.append(f"Category required: {scheme.get('category')}")

    if not _contains_allowed(student["gender"], scheme.get("gender")):
        reasons.append(f"Gender eligibility: {scheme.get('gender')}")

    if not _contains_allowed(student["state"], scheme.get("state")):
        reasons.append(f"State eligibility: {scheme.get('state')}")

    if not _course_matches(student["course"], scheme.get("course")):
        reasons.append(f"Course required: {scheme.get('course')}")

    if not _contains_allowed(student["year"], scheme.get("year")):
        reasons.append(f"Year required: {scheme.get('year')}")

    if not _contains_allowed(student["hostel"], scheme.get("hostel_status")):
        reasons.append(f"Hostel status required: {scheme.get('hostel_status')}")

    return reasons


def find_suitable_schemes(student):
    schemes = get_all_schemes()
    eligible = []
    not_eligible = []

    for scheme in schemes:
        reasons = check_eligibility(student, scheme)
        if reasons:
            not_eligible.append((scheme, reasons))
        else:
            eligible.append(scheme)

    return eligible, not_eligible


def search_scheme(search_text):
    search_text = _normal(search_text)

    if not search_text:
        return get_all_schemes()

    schemes = get_all_schemes()
    results = []

    for scheme in schemes:
        searchable = " ".join([
            _text(scheme.get("scheme_name")),
            _text(scheme.get("description")),
            _text(scheme.get("benefits")),
            _text(scheme.get("category")),
            _text(scheme.get("education"))
        ]).casefold()

        if search_text in searchable:
            results.append(scheme)

    return results


if __name__ == "__main__":
    conn = connect_database()

    if conn:
        print("Database connected successfully!")
        print("Total schemes:", len(get_all_schemes()))
        conn.close()
    else:
        print("Database connection failed.")
