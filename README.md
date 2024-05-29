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

The University of Hong Kong owns the Software intellectual property of the AI of Image Recognition Training.

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

# Environment
Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

# MySQL Installation
[Mac](https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-linuxunix-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/downloads/installer/)

You'll obtain an account and password after installation, then you should modify the `faces.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```


# 1. Run the Program- Face Recognition
  1.1 Collect Face Data
  ```
  """
  user_name = "Jack"   # the name
  NUM_IMGS = 400       # the number of saved images
  """
  python face_capture.py
  ```
  The camera will be activated and the captured images will be stored in `data/Jack` folder.      
  **Note:** Only one person’s images can be captured at a time.
  
  1.2 Train a Face Recognition Model
  ```
  python train.py
  ```
  `train.yml` and `labels.pickle` will be created at the current folder.
  


# 2. Run the Program- Database Design
  
  2.1 Define Database
  **You need to** create tables in `facerecognition.sql`.      
  Here is a sample code for `Student`.
  ```
  # Create TABLE 'Student'
  CREATE TABLE `Student` (
    `student_id` int NOT NULL,
    `name` varchar(50) NOT NULL,
    `login_time` time NOT NULL,
    `login_date` date NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
  
  LOCK TABLES `Student` WRITE;
  /*!40000 ALTER TABLE `Student` DISABLE KEYS */;
  INSERT INTO `Student` VALUES (1, "JACK", NOW(), '2021-01-20');
  /*!40000 ALTER TABLE `Student` ENABLE KEYS */;
  UNLOCK TABLES;
```

  2.2 Import Database
  Open mysql server and import the file `facerecognition.sql`.
  ```
  # login the mysql command
  mysql -u root -p
  
  # create database.  'mysql>' indicates we are now in the mysql command line
  mysql> CREATE DATABASE facerecognition;
  mysql> USE facerecognition;
  
  # import from sql file
  mysql> source facerecognition.sql
  ```



# 3. Run the Program- Login Interface

  3.1 OpenCV GUI
  ```
  python faces.py
  ```

  3.2 PySimpleGUI GUI
  ```
  python faces_gui.py
  ```
  
  The camera will be activated and recognize your face using the pretrained model.    
  **You need to** implement other useful functions in this part.
  










