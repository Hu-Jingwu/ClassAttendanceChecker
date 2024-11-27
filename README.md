This attendance checker program is designed for a course where attendance is taken via Microsoft Forms, created using the university’s Office 365 account. The forms capture student email addresses in the format:

StudentID@uni.edu.usa

The program works with .xlsx files, each named with the Week Number and Lecture Number, for example:

Attendance Week 5 Lecture 2.xlsx

There is also an .xlsx file containing the list of student IDs enrolled in the course.

Key Features:
The program can easily process multiple attendance files. You can add more files to a predefined dictionary in the package for batch processing.
It removes the domain part of each student email (i.e., @uni.edu.usa) and compares the prefix (student ID) against the enrolled student ID list. If the student is enrolled, the program marks their attendance as 1; otherwise, it marks it as 0.
The program automatically extracts the week and lecture number from the file name (e.g., "Attendance Week 5 Lecture 2" becomes W5L2), marking the attendance accordingly.

