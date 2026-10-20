-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2026 at 06:04 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `government_scheme_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `schemes`
--

CREATE TABLE `schemes` (
  `scheme_id` int(11) NOT NULL,
  `scheme_name` varchar(200) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `min_age` int(11) DEFAULT 0,
  `max_age` int(11) DEFAULT 100,
  `income_limit` decimal(12,2) DEFAULT 99999999.00,
  `min_10th_marks` decimal(5,2) DEFAULT 0.00,
  `min_12th_marks` decimal(5,2) DEFAULT 0.00,
  `education` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `benefits` varchar(500) DEFAULT NULL,
  `documents` varchar(500) DEFAULT NULL,
  `application_link` varchar(500) DEFAULT NULL,
  `course` varchar(255) DEFAULT 'All',
  `year` varchar(255) DEFAULT 'All',
  `hostel_status` varchar(50) DEFAULT 'All'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schemes`
--

INSERT INTO `schemes` (`scheme_id`, `scheme_name`, `description`, `min_age`, `max_age`, `income_limit`, `min_10th_marks`, `min_12th_marks`, `education`, `category`, `gender`, `state`, `benefits`, `documents`, `application_link`, `course`, `year`, `hostel_status`) VALUES
(4, 'Chhatrapati Rajarshi Shahu Maharaj Scholarship', 'Financial assistance for eligible students pursuing higher and professional education in Maharashtra.', 16, 30, 800000.00, 75.00, 0.00, 'All', 'SC', 'All', 'Maharashtra', 'Scholarship and educational financial assistance.', 'Aadhaar Card, Income Certificate, Caste Certificate, Marksheet, Domicile Certificate, Bank Account Details', 'https://mahadbt.maharashtra.gov.in/', 'All', 'All', 'All'),
(5, 'Dr. Punjabrao Deshmukh Vasatigruh Nirvah Bhatta Yojana', 'Allowance scheme providing financial assistance to eligible students from economically weaker sections and specified families pursuing professional education in Maharashtra.', 17, 30, 800000.00, 0.00, 0.00, 'Professional', 'EBC,EWS,SEBC', 'All', 'Maharashtra', 'Maintenance and hostel-related allowance for eligible students.', 'Aadhaar Card, Income Certificate, Domicile Certificate, College Admission Proof, Hostel Certificate, Bank Account Details', 'https://mahadbt.maharashtra.gov.in/', 'All', 'All', 'All'),
(6, 'AICTE Swanath Scholarship Scheme - Technical Degree', 'Scholarship support for eligible students belonging to specified disadvantaged categories and pursuing technical degree education.', 17, 30, 800000.00, 0.00, 0.00, 'Technical Degree', 'All', 'All', 'All', 'Annual financial assistance for eligible students pursuing technical education.', 'Aadhaar Card, Income Certificate, Educational Marksheet, Admission Letter, Bank Account Details, Relevant Supporting Certificate', 'https://www.aicte-india.org/', 'All', 'All', 'All'),
(7, 'Post-Matric Scholarship for Students with Disabilities', 'Financial assistance for eligible students with disabilities pursuing post-matriculation education.', 16, 35, 250000.00, 0.00, 0.00, 'Post-Matric', 'Disability', 'All', 'All', 'Financial assistance for education and related expenses.', 'Aadhaar Card, Disability Certificate or UDID, Income Certificate, Marksheet, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All'),
(8, 'AICTE Pragati Scholarship Scheme for Girl Students', 'Scholarship scheme for eligible girl students pursuing technical degree education in AICTE-approved institutions.', 17, 30, 800000.00, 0.00, 0.00, 'Technical Degree', 'All', 'Female', 'All', 'Financial assistance to eligible girl students pursuing technical education.', 'Aadhaar Card, Income Certificate, Marksheet, Admission Proof, Bank Account Details, Institute Certificate', 'https://www.aicte-india.org/', 'All', 'All', 'All'),
(9, 'Prime Minister Scholarship Scheme for Central Armed Police Forces and Assam Rifles', 'Merit-based scholarship scheme for eligible wards and widows of Central Armed Police Forces and Assam Rifles personnel pursuing professional degree courses.', 17, 30, 999999999.00, 0.00, 60.00, 'Professional Degree', 'CAPF,Assam Rifles', 'All', 'All', 'Scholarship assistance for eligible students pursuing professional degree courses.', 'Aadhaar Card, Marksheet, Service Certificate, Dependent Certificate, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All'),
(10, 'National Fellowship and Scholarship for Higher Education of ST Students', 'Scholarship support for eligible students belonging to Scheduled Tribe communities pursuing higher education.', 17, 36, 999999999.00, 0.00, 0.00, 'Higher Education', 'ST', 'All', 'All', 'Financial assistance for higher education for eligible ST students.', 'Aadhaar Card, ST Caste Certificate, Income Certificate, Educational Certificates, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All'),
(11, 'PM-USP Central Sector Scheme of Scholarship for College and University Students', 'Merit-based scholarship for eligible students pursuing regular college and university courses.', 17, 30, 450000.00, 0.00, 80.00, 'Regular Degree', 'All', 'All', 'All', 'Financial scholarship assistance for eligible college and university students.', 'Aadhaar Card, Class 12 Marksheet, Income Certificate, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All'),
(12, 'PM YASASVI Top Class Education in College for OBC EBC and DNT Students', 'Scholarship support for eligible OBC, EBC and DNT students pursuing higher education in identified institutions.', 17, 30, 250000.00, 0.00, 0.00, 'College', 'OBC,EBC,DNT', 'All', 'All', 'Financial support for eligible students including educational expenses as permitted under the scheme.', 'Aadhaar Card, Category Certificate, Income Certificate, Marksheet, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All'),
(13, 'Central Sector Scholarship of Top Class Education for SC Students', 'Financial support for eligible SC students pursuing studies beyond Class 12 in notified institutions.', 17, 30, 800000.00, 0.00, 0.00, 'College', 'SC', 'All', 'All', 'Financial support for higher education in notified institutions.', 'Aadhaar Card, SC Caste Certificate, Income Certificate, Marksheet, Admission Proof, Bank Account Details', 'https://scholarships.gov.in/', 'All', 'All', 'All');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `schemes`
--
ALTER TABLE `schemes`
  ADD PRIMARY KEY (`scheme_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `schemes`
--
ALTER TABLE `schemes`
  MODIFY `scheme_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
