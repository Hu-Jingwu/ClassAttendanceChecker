import pandas as pd
import numpy as np

#We need to define the dictionary for all the atttendance data
attendance_files = ['Attendance Week3 Lecture 1.xlsx','Attendance Week3 Lecture 2.xlsx','Attendance Week3 Lecture 3.xlsx',\
                    'Attendance Week4 Lecture 1.xlsx','Attendance Week4 Lecture 2.xlsx','Attendance Week4 Lecture 3.xlsx',\
                    'Attendance Week5 Lecture 1.xlsx','Attendance Week5 Lecture 2.xlsx','Attendance Week5 Lecture 3.xlsx',\
                    'Attendance Week6 Lecture 1.xlsx','Attendance Week6 Lecture 2.xlsx','Attendance Week6 Lecture 3.xlsx',\
                    'Attendance Week7 Lecture 1.xlsx','Attendance Week7 Lecture 2.xlsx',\
                    'Attendance Week8 Lecture 1.xlsx','Attendance Week8 Lecture 2.xlsx','Attendance Week8 Lecture 3.xlsx',\
                    'Attendance Week9 Lecture 1.xlsx','Attendance Week9 Lecture 2.xlsx','Attendance Week9 Lecture 3.xlsx',\
                    'Attendance Week10 Lecture 1.xlsx','Attendance Week10 Lecture 2.xlsx','Attendance Week10 Lecture 3.xlsx',\
                    'Attendance Week11 Lecture 1.xlsx','Attendance Week11 Lecture 2.xlsx','Attendance Week11 Lecture 3.xlsx']
attendance_dict = {}

for file in attendance_files:
    # Split the filename to extract the week and lecture numbers
    parts = file.split(' ')  # Split by spaces
    week_number = parts[1].replace('Week', '')  # Remove 'Week' and get the number
    lecture_number = parts[3].replace('Lecture', '')  # Remove 'Lecture' and get the number
    
    # Create a key like 'W3L1' for Week 3, Lecture 1
    key = f'W{week_number}L{lecture_number}'
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    
    # Store the DataFrame in the dictionary with the key
    attendance_dict[key] = df

# Example: Access the DataFrame for Week 3, Lecture 1
print(attendance_dict['W3L1'])


