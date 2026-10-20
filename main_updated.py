import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

from analyzer import find_suitable_schemes, get_all_schemes, search_scheme


APP_BG = "#eef3f8"
CARD_BG = "#ffffff"
PRIMARY = "#1769aa"
DARK = "#17324d"
MUTED = "#64748b"
SUCCESS = "#15803d"
DANGER = "#b42318"
BORDER = "#d7e0ea"

INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
    "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu", "Delhi",
    "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
]

AGES = [str(age) for age in range(1, 101)]

GENDERS = ["Male", "Female", "Other"]

CATEGORIES = [
    "General", "SC", "ST", "OBC", "EBC", "EWS", "SEBC","NTC",
    "DNT", "Disability", "CAPF", "Assam Rifles"
]

EDUCATION = [
    "School", "College", "Diploma", "Undergraduate",
    "Postgraduate", "Technical Degree","Post-Matric", 
    "Professional Degree", "Higher Education","Regular Degree"
]

COURSES = [
    "Engineering", "Diploma","B.A","M.A","B.Sc","M.Sc",
    "Technical Degree", "B.Com", "M.Com","Professional Degree",
    "MBBS","BAMS","BHMS","B Pharmacy","M Pharmacy",
    "D Pharmacy","Regular Degree","Other"
]

YEARS = ["1st Year", "2nd Year", "3rd Year", "4th Year", "Final Year"]

HOSTEL = [ "Hosteller", "Day Scholar"]

root = tk.Tk()
root.title("Government Scheme Assistant | Smart Eligibility Finder")
root.geometry("1200x850")
root.minsize(1050, 760)
root.configure(bg=APP_BG)


def configure_styles():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "TCombobox",
        padding=7,
        fieldbackground="white",
        background="white",
        bordercolor=BORDER,
        foreground=DARK
    )

    style.configure(
        "Treeview",
        background="white",
        fieldbackground="white",
        foreground=DARK,
        rowheight=38,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=DARK,
        foreground="white",
        font=("Segoe UI", 10, "bold"),
        padding=9
    )

    style.map(
        "Treeview",
        background=[("selected", "#dbeafe")],
        foreground=[("selected", DARK)]
    )


configure_styles()


def make_card(parent):
    return tk.Frame(
        parent,
        bg=CARD_BG,
        bd=1,
        relief="solid",
        highlightbackground=BORDER,
        highlightcolor=BORDER
    )


header = tk.Frame(root, bg=DARK, height=105)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="GOVERNMENT SCHEME ASSISTANT",
    font=("Segoe UI", 25, "bold"),
    fg="white",
    bg=DARK
).pack(anchor="w", padx=35, pady=(18, 2))

tk.Label(
    header,
    text="Smart eligibility matching • Transparent reasons • Easy scheme discovery",
    font=("Segoe UI", 11),
    fg="#cfe4f7",
    bg=DARK
).pack(anchor="w", padx=37)


main = tk.Frame(root, bg=APP_BG)
main.pack(fill="both", expand=True, padx=25, pady=20)


form_card = make_card(main)
form_card.pack(fill="x")


tk.Label(
    form_card,
    text="Student Profile",
    font=("Segoe UI", 17, "bold"),
    fg=DARK,
    bg=CARD_BG
).grid(row=0, column=0, columnspan=4, sticky="w", padx=25, pady=(18, 3))

tk.Label(
    form_card,
    text="Enter your details to find schemes that match your eligibility.",
    font=("Segoe UI", 10),
    fg=MUTED,
    bg=CARD_BG
).grid(row=1, column=0, columnspan=4, sticky="w", padx=25, pady=(0, 12))


fields = {}


def add_label(row, col, text):
    tk.Label(
        form_card,
        text=text,
        font=("Segoe UI", 10, "bold"),
        fg=DARK,
        bg=CARD_BG
    ).grid(row=row, column=col * 2, sticky="w", padx=(25, 8), pady=7)


def add_combo(row, col, values, default=""):
    combo = ttk.Combobox(
        form_card,
        values=values,
        state="readonly",
        width=24
    )
    combo.grid(row=row, column=col * 2 + 1, sticky="ew", padx=(0, 25), pady=7)
    if default:
        combo.set(default)
    return combo


name_entry = tk.Entry(
    form_card,
    font=("Segoe UI", 10),
    width=27,
    relief="solid",
    bd=1
)
name_entry.grid(row=2, column=1, sticky="ew", padx=(0, 25), pady=7)
add_label(2, 0, "Student Name")

add_label(2, 1, "Age")
age_combo = add_combo(2, 1, AGES, " ")

add_label(3, 0, "Student Email")
email_entry = tk.Entry(
    form_card,
    font=("Segoe UI", 10),
    width=27,
    relief="solid",
    bd=1
)
email_entry.grid(row=3, column=1, sticky="ew", padx=(0, 25), pady=7)

add_label(3, 1, "Gender")
gender_combo = add_combo(3, 1, GENDERS, " ")

add_label(4, 0, "Category")
category_combo = add_combo(4, 0, CATEGORIES, " ")

add_label(4, 1, "Education")
education_combo = add_combo(4, 1, EDUCATION, " ")

add_label(5, 0, "State / UT")
state_combo = add_combo(5, 0, INDIAN_STATES, " ")

add_label(5, 1, "Annual Family Income")
income_entry = tk.Entry(
    form_card, font=("Segoe UI", 10), relief="solid", bd=1
)
income_entry.grid(row=5, column=3, sticky="ew", padx=(0, 25), pady=7)

add_label(6, 0, "10th Marks (%)")
marks10_entry = tk.Entry(
    form_card, font=("Segoe UI", 10), relief="solid", bd=1
)
marks10_entry.grid(row=6, column=1, sticky="ew", padx=(0, 25), pady=7)

add_label(6, 1, "12th Marks (%)")
marks12_entry = tk.Entry(
    form_card, font=("Segoe UI", 10), relief="solid", bd=1
)
marks12_entry.grid(row=6, column=3, sticky="ew", padx=(0, 25), pady=7)

add_label(7, 0, "Course")
course_combo = add_combo(7, 0, COURSES, " ")

add_label(7, 1, "Academic Year")
year_combo = add_combo(7, 1, YEARS, " ")

add_label(8, 0, "Hostel Status")
hostel_combo = add_combo(8, 0, HOSTEL, " ")


for col in range(4):
    form_card.grid_columnconfigure(col, weight=1)


def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    income_entry.delete(0, tk.END)
    marks10_entry.delete(0, tk.END)
    marks12_entry.delete(0, tk.END)

    age_combo.set("18")
    gender_combo.set("Female")
    category_combo.set("General")
    education_combo.set("College")
    state_combo.set("Maharashtra")
    course_combo.set("All")
    year_combo.set("All")
    hostel_combo.set("All")


def open_link(link):
    if link and str(link).strip():
        webbrowser.open(str(link).strip())


def add_summary_card(parent, column, title, value, color):
    card = tk.Frame(parent, bg="white", bd=1, relief="solid")
    card.grid(row=0, column=column, sticky="ew", padx=6)

    tk.Label(
        card,
        text=title,
        font=("Segoe UI", 9, "bold"),
        fg=MUTED,
        bg="white"
    ).pack(pady=(10, 0))

    label = tk.Label(
        card,
        text=str(value),
        font=("Segoe UI", 20, "bold"),
        fg=color,
        bg="white"
    )
    label.pack(pady=(0, 10))
    return label


def create_table(parent, columns, widths):
    frame = tk.Frame(parent, bg="white")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for column, width in zip(columns, widths):
        tree.heading(column, text=column)
        tree.column(column, width=width, minwidth=100, anchor="w")

    yscroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    xscroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.grid(row=0, column=0, sticky="nsew")
    yscroll.grid(row=0, column=1, sticky="ns")
    xscroll.grid(row=1, column=0, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    return tree


def show_results(student, eligible, not_eligible):
    window = tk.Toplevel(root)
    window.title("Eligibility Results")
    window.geometry("1200x760")
    window.minsize(950, 650)
    window.configure(bg=APP_BG)

    tk.Label(
        window,
        text=f"Results for {student['name']}",
        font=("Segoe UI", 21, "bold"),
        fg=DARK,
        bg=APP_BG
    ).pack(anchor="w", padx=25, pady=(20, 2))

    tk.Label(
        window,
        text="Eligible schemes are matched against every available criterion in your profile.",
        font=("Segoe UI", 10),
        fg=MUTED,
        bg=APP_BG
    ).pack(anchor="w", padx=27, pady=(0, 15))

    summary = tk.Frame(window, bg=APP_BG)
    summary.pack(fill="x", padx=20, pady=(0, 15))

    summary.grid_columnconfigure(0, weight=1)
    summary.grid_columnconfigure(1, weight=1)
    summary.grid_columnconfigure(2, weight=1)

    add_summary_card(summary, 0, "ELIGIBLE", len(eligible), SUCCESS)
    add_summary_card(summary, 1, "NOT ELIGIBLE", len(not_eligible), DANGER)
    add_summary_card(summary, 2, "TOTAL CHECKED", len(eligible) + len(not_eligible), PRIMARY)

    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True, padx=20, pady=5)

    eligible_tab = tk.Frame(notebook, bg="white")
    not_tab = tk.Frame(notebook, bg="white")

    notebook.add(
        eligible_tab,
        text=f"  ✓ Eligible Schemes ({len(eligible)})  "
    )
    notebook.add(
        not_tab,
        text=f"  ✕ Not Eligible ({len(not_eligible)})  "
    )

    eligible_columns = (
        "Scheme",
        "Category",
        "State",
        "Benefits",
        "Documents",
        "Application"
    )

    eligible_tree = create_table(
        eligible_tab,
        eligible_columns,
        [280, 120, 130, 260, 300, 100]
    )

    for scheme in eligible:
        eligible_tree.insert(
            "",
            "end",
            values=(
                scheme["scheme_name"],
                scheme["category"],
                scheme["state"],
                scheme["benefits"],
                scheme["documents"],
                "Open Link"
            ),
            tags=(str(scheme["scheme_id"]),)
        )

    eligible_tree.tag_configure("selected", background="#e8f5e9")

    tk.Label(
        eligible_tab,
        text="Double-click a scheme row to open its official application link.",
        font=("Segoe UI", 9),
        fg=MUTED,
        bg="white"
    ).pack(anchor="w", padx=15, pady=(0, 8))

    def open_eligible_link(event):
        item = eligible_tree.identify_row(event.y)
        if not item:
            return

        values = eligible_tree.item(item, "values")
        scheme_name = values[0]

        for scheme in eligible:
            if scheme["scheme_name"] == scheme_name:
                open_link(scheme["application_link"])
                break

    eligible_tree.bind("<Double-1>", open_eligible_link)

    not_columns = (
        "Scheme",
        "Category",
        "State",
        "Why Not Eligible"
    )

    not_tree = create_table(
        not_tab,
        not_columns,
        [300, 150, 150, 600]
    )

    for scheme, reasons in not_eligible:
        not_tree.insert(
            "",
            "end",
            values=(
                scheme["scheme_name"],
                scheme["category"],
                scheme["state"],
                " • ".join(reasons)
            )
        )

    tk.Label(
        not_tab,
        text="The reason column shows exactly which eligibility conditions were not satisfied.",
        font=("Segoe UI", 9),
        fg=MUTED,
        bg="white"
    ).pack(anchor="w", padx=15, pady=(0, 8))


def find_button_clicked():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    income_text = income_entry.get().strip()
    marks10_text = marks10_entry.get().strip()
    marks12_text = marks12_entry.get().strip()

    if not name:
        messagebox.showwarning("Missing Information", "Please enter student name.")
        return

    if not email:
        messagebox.showwarning(
            "Missing Information",
            "Please enter student email."
    )
        return

    import re

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showerror(
            "Invalid Email",
            "Please enter a valid email address."
    )
        return

    if not income_text or not marks10_text or not marks12_text:
        messagebox.showwarning(
            "Missing Information",
            "Please enter annual income, 10th marks and 12th marks."
        )
        return

    try:
        income = float(income_text)
        marks10 = float(marks10_text)
        marks12 = float(marks12_text)
        age = int(age_combo.get())

        if income < 0:
            raise ValueError

        if not 0 <= marks10 <= 100 or not 0 <= marks12 <= 100:
            messagebox.showerror(
                "Invalid Marks",
                "10th and 12th marks must be between 0 and 100."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for income and marks."
        )
        return

    student = {
        "name": name,
        "age": age,
        "email": email,
        "gender": gender_combo.get(),
        "category": category_combo.get(),
        "education": education_combo.get(),
        "state": state_combo.get(),
        "income": income,
        "marks10": marks10,
        "marks12": marks12,
        "course": course_combo.get(),
        "year": year_combo.get(),
        "hostel": hostel_combo.get()
    }

    eligible, not_eligible = find_suitable_schemes(student)
    show_results(student, eligible, not_eligible)


def view_all_schemes():
    schemes = get_all_schemes()

    window = tk.Toplevel(root)
    window.title("All Government Schemes")
    window.geometry("1200x700")
    window.configure(bg=APP_BG)

    tk.Label(
        window,
        text=f"All Government Schemes ({len(schemes)})",
        font=("Segoe UI", 20, "bold"),
        fg=DARK,
        bg=APP_BG
    ).pack(anchor="w", padx=20, pady=15)

    columns = ("Scheme", "Education", "Category", "Gender", "State", "Benefits")
    tree = create_table(
        window,
        columns,
        [330, 170, 150, 100, 150, 350]
    )

    for scheme in schemes:
        tree.insert(
            "",
            "end",
            values=(
                scheme["scheme_name"],
                scheme["education"],
                scheme["category"],
                scheme["gender"],
                scheme["state"],
                scheme["benefits"]
            )
        )


def search_scheme_window():
    window = tk.Toplevel(root)
    window.title("Search Government Scheme")
    window.geometry("1100x680")
    window.configure(bg=APP_BG)

    top = tk.Frame(window, bg=APP_BG)
    top.pack(fill="x", padx=20, pady=15)

    tk.Label(
        top,
        text="Search Scheme",
        font=("Segoe UI", 19, "bold"),
        fg=DARK,
        bg=APP_BG
    ).pack(side="left")

    search_entry = tk.Entry(
        top,
        font=("Segoe UI", 11),
        width=45,
        relief="solid",
        bd=1
    )
    search_entry.pack(side="left", padx=25)

    columns = ("Scheme", "Description", "Category", "Education", "State")
    tree = create_table(
        window,
        columns,
        [320, 430, 150, 180, 150]
    )

    def perform_search():
        for item in tree.get_children():
            tree.delete(item)

        schemes = search_scheme(search_entry.get())

        for scheme in schemes:
            tree.insert(
                "",
                "end",
                values=(
                    scheme["scheme_name"],
                    scheme["description"],
                    scheme["category"],
                    scheme["education"],
                    scheme["state"]
                )
            )

        if not schemes:
            messagebox.showinfo(
                "Search",
                "No matching scheme found.",
                parent=window
            )

    ttk.Button(
        top,
        text="Search",
        command=perform_search
    ).pack(side="left")

    search_entry.bind("<Return>", lambda event: perform_search())


button_bar = tk.Frame(root, bg=APP_BG)
button_bar.pack(fill="x", padx=25, pady=(0, 20))

ttk.Button(
    button_bar,
    text="Find Suitable Schemes",
    command=find_button_clicked
).pack(side="left", padx=5)

ttk.Button(
    button_bar,
    text="Clear",
    command=clear_form
).pack(side="left", padx=5)

ttk.Button(
    button_bar,
    text="View All Schemes",
    command=view_all_schemes
).pack(side="left", padx=5)

ttk.Button(
    button_bar,
    text="Search Scheme",
    command=search_scheme_window
).pack(side="left", padx=5)

tk.Label(
    button_bar,
    text="Tip: Double-click an eligible scheme to open its application website.",
    font=("Segoe UI", 9),
    fg=MUTED,
    bg=APP_BG
).pack(side="right", padx=10)


root.mainloop()
