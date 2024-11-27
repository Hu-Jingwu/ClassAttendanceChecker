import os
import pandas as pd

# List of attendance files, here the example only with one file, you can add more
attendance_files = ['Attendance Week3 Lecture 1.xlsx','Attendance Week5 Lecture 2.xlsx']

attendance_dict = {}
students_df = pd.read_excel('student_ids.xlsx')
# Loop through the list of files
for file in attendance_files:
    # Check if the file exists before attempting to read it
    if os.path.exists(file):
        print(f"File {file} exists")
        
        # Split the filename to extract the week and lecture numbers
        parts = file.split(' ')  # Split by spaces
        print(f"Parts of filename '{file}':", parts)  # Debug print to check how the filename is split
        
        # Extract week number and lecture number
        week_number = parts[1].replace('Week', '')  # Remove 'Week' and get the number
        lecture_number = parts[3].replace('Lecture', '').replace('.xlsx', '')  # Remove 'Lecture' and the file extension
        
        # Debugging: print the week and lecture number
        print(f"Week: {week_number}, Lecture: {lecture_number}")
        
        # Create a key like 'W3L1' for Week 3, Lecture 1
        key = f'W{week_number}L{lecture_number}'
        
        # Print the generated key to verify
        print(f"Generated key: {key}")
        
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file)
        
        # Store the DataFrame in the dictionary with the key
        attendance_dict[key] = df
    else:
        print(f"File {file} does not exist!")
        
students_df['Student_ID'] = students_df['Student_ID'].astype(str).str.strip()

for key, lecture_df in attendance_dict.items():
    week_lecture = key  # e.g., 'W3L1', 'W3L2', ...
    print(f"Processing {week_lecture}...")
    lecture_df['Email'] = lecture_df['Email'].str.split('@').str[0].str.strip()
    lecture_df['Email'] = lecture_df['Email'].astype(str).str.strip()
    # Check if student IDs in students_df are present in the current attendance_df
    students_df[week_lecture] = students_df['Student_ID'].isin(lecture_df['Email']).astype(int)
    
students_df.to_excel('students_with_full_attendance.xlsx', sheet_name='Attendance Data', index=False)
