# Intelligent_Course_Management_System_With_Facial_Login

1. When a student logs in with their face, their information such as name, login time, and welcome message will be presented in the graphics user interface (GUI).
2. If the student has a class within one hour, the corresponding course information, classroom address, teacher's message, links to Zoom, tutorial/lecture notes, and other course materials will be presented in the GUI. The student could click the links to redirect to Zoom or other materials. The GUI should also allow the student to send the above information to their email address.
3. If the student does not have class at the moment, the GUI could present a personal class timetable for the student.
4. The system should record the latest behavior of the student, such as when they log in the system, how long the student stays in the system, etc.

# Contributers
Leung King To

Iu Chi Ho Tyler

Wong Zee Meng

Wen Qi Li

Louis Polwarth

# Database Design
Course(course_id (Primary Key), course_code, course_name, classroom_address, teacher_message, zoom_link, tutorial_lecture_notes, other_course_materials, start_time, end_time, days_of_week

Enrollment(enrollment_id (Primary Key), student_id, course_id)
student_id: foreign Key referencing Student Table
course_id: Foreign Key referencing Course Table

Student(student_id (Primary Key), student_name, email_address)

Email(email_id (Primary Key), student_id, email_time, email_content)
student_id: foreign Key referencing Student Table

Login(login_id (Primary Key), student_id, login_time, logout_time)
student_id: foreign Key referencing Student Table

Behavior(behavior_id (Primary Key), student_id, session_duration)
student_id: foreign Key referencing Student Table

FacialInfo(facial_id (Primary Key), facial_data)
student_id: foreign Key referencing Student Table


# UI Design
Log In: The system redirects users to face recognition page

Facial Detection: Displaying Scrren in which face is autonmatically detected.

Log Out: System logout and user will be redirected to Log In Page again

Info: Name of the student, Current Login Time, Last Login Date &Time will be shown

Courses Details: Venue of class and zoom link is given

Timetable: Course code, Course name, Date and Time of each course will be shown











