-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--
DROP TABLE IF EXISTS `Student`;

# Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` int PRIMARY KEY NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;

INSERT INTO `Student` VALUES (6, 'Jack', 'jack@connect.hku.hk');
INSERT INTO Student (student_id, name, email_address)
VALUES
    (1, 'John Chan', 'john.chan@connect.hku.hk'),
    (2, 'Jane Leung', 'jane.leung@connect.hku.hk'),
    (3, 'David Lam', 'david.lam@connect.hku.hk'),
    (4, 'Emily Kwan', 'emily.kwan@connect.hku.hk'),
    (5, 'Michael Ng', 'michael.ng@connect.hku.hk');

/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Course'
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_code VARCHAR(255),
    course_name VARCHAR(255),
    classroom_address VARCHAR(255),
    teacher_message VARCHAR(255),
    zoom_link VARCHAR(255),
    tutorial_lecture_notes LONGBLOB,
    other_course_materials LONGBLOB,
    start_time TIME,
    end_time TIME,
    days_of_week VARCHAR(255)
);

INSERT INTO Course (course_id, course_code, course_name, classroom_address, teacher_message, zoom_link, tutorial_lecture_notes, other_course_materials, start_time, end_time, days_of_week)
VALUES
    (1, 'COMP101', 'Introduction to Computer Science', 'Room 101', 'Welcome to the course!', 'https://zoom.us/j/123456789', NULL, NULL, '08:30:00', '10:30:00', 'Monday, Wednesday, Friday'),
    (2, 'MATH201', 'Calculus I', 'Room 201', 'Welcome to the course!', 'https://zoom.us/j/987654321', NULL, NULL, '10:30:00', '12:30:00', 'Tuesday, Thursday'),
    (3, 'ECON301', 'Microeconomics', 'Room 301', 'Welcome to the course!', 'https://zoom.us/j/567890123', NULL, NULL, '13:30:00', '15:30:00', 'Monday, Wednesday'),
    (4, 'PHYS101', 'Physics I', 'Room 401', 'Welcome to the course!', 'https://zoom.us/j/234567890', NULL, NULL, '15:30:00', '17:30:00', 'Tuesday, Thursday'),
    (5, 'ENG201', 'English Composition', 'Room 501', 'Welcome to the course!', 'https://zoom.us/j/901234567', NULL, NULL, '17:30:00', '18:30:00', 'Friday');


# Create TABLE 'Login'
-- Create Login table
CREATE TABLE Login (
    login_id INT PRIMARY KEY,
    student_id INT,
    login_time TIME,
    logout_time TIME,
    login_date DATE,
    duration TIME,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

INSERT INTO Login (login_id, student_id, login_time, login_date, logout_time)
VALUES
    (1, 1, '2023-11-01 09:00:00', '2023-11-01', '2023-11-01 10:00:00'),
    (2, 2, '2023-11-01 09:30:00', '2023-11-01', '2023-11-01 11:00:00'),
    (3, 3, '2023-11-01 10:00:00', '2023-11-01', '2023-11-01 11:30:00'),
    (4, 4, '2023-11-01 10:30:00', '2023-11-01', '2023-11-01 12:00:00'),
    (5, 5, '2023-11-01 11:00:00', '2023-11-01', '2023-11-01 12:30:00'),
    (6, 6, '2023-11-02 09:00:00', '2023-11-01', '2023-11-02 10:00:00');


-- Create Behavior table
CREATE TABLE Behavior (
    behavior_id INT PRIMARY KEY,
    student_id INT,
    login_time DATETIME,
    session_duration INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

INSERT INTO Behavior (behavior_id, student_id, login_time, session_duration)
VALUES
    (1, 1, '2023-11-01 09:00:00', 60),
    (2, 2, '2023-11-01 09:30:00', 90),
    (3, 3, '2023-11-01 10:00:00', 120),
    (4, 4, '2023-11-01 10:30:00', 60),
    (5, 5, '2023-11-01 11:00:00', 90),
    (6, 1, '2023-11-02 09:00:00', 60),
    (7, 2, '2023-11-02 09:30:00', 90),
    (8, 3, '2023-11-02 10:00:00', 120),
    (9, 4, '2023-11-02 10:30:00', 60),
    (10, 5, '2023-11-02 11:00:00', 90);

-- Create Email table
CREATE TABLE Email (
    email_id INT PRIMARY KEY,
    student_id INT,
    email_time DATETIME,
    email_content VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

INSERT INTO Email (email_id, student_id, email_time, email_content)
VALUES
    (1, 1, '2023-11-01 09:00:00', 'Reminder: Assignment due tomorrow'),
    (2, 2, '2023-11-01 09:30:00', 'Meeting rescheduled to next week'),
    (3, 3, '2023-11-01 10:00:00', 'Course material updated'),
    (4, 4, '2023-11-01 10:30:00', 'Upcoming exam information'),
    (5, 5, '2023-11-01 11:00:00', 'Student club event announcement'),
    (6, 1, '2023-11-02 09:00:00', 'Change in tutorial session timings'),
    (7, 2, '2023-11-02 09:30:00', 'Reminder: Group project meeting today'),
    (8, 3, '2023-11-02 10:00:00', 'Important course announcement'),
    (9, 4, '2023-11-02 10:30:00', 'Feedback on your recent assignment'),
    (10, 5, '2023-11-02 11:00:00', 'Invitation to guest lecture');

-- Create FacialInfo table
CREATE TABLE FacialInfo (
    facial_id INT PRIMARY KEY,
    student_id INT,
    facial_data BLOB,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

INSERT INTO `FacialInfo` (facial_id, student_id, facial_data)
VALUES
    (1, 1, NULL),
    (2, 2, NULL),
    (3, 3, NULL),
    (4, 4, NULL),
    (5, 4, NULL),
    (6, 6, load_file('data/Jack')); # not sure if this is the correct way to store images

-- Create Enrollment table
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrolment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
INSERT INTO `Enrollment`
VALUES
    (1, 1, 1, '2023-09-01'),
    (2, 2, 2, '2023-09-01'),
    (3, 3, 3, '2023-09-01'),
    (4, 4, 4, '2023-09-01'),
    (5, 5, 5, '2023-09-01'),
    (6, 1, 2, '2023-09-01'),
    (7, 2, 3, '2023-09-01'),
    (8, 3, 4, '2023-09-01'),
    (9, 4, 5, '2023-09-01'),
    (10, 6, 1, '2023-09-01'),
    (11, 6, 3, '2023-09-01'),
    (12, 5, 1, '2023-09-01');

# Create other TABLE...


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
