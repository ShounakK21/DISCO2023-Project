# DISCO2023-Project
# Backtracking Algorithm for Faculty Course Allotment

This Python script implements a backtracking algorithm to allot courses to faculty members based on their preferences and category. The faculty data is read from an input CSV file, and the final allotment results are written to an output CSV file.

## Script Structure:

### 1. Reading Input Data
- The `read_input_file` function reads data from the input CSV file specified by the `input_file_path`.
- The `read_data` function processes the raw data and constructs a dictionary (`faculty_data`) with faculty IDs as keys and associated category and course preferences.

### 2. Initializing Allotment Data
- The `initialize_allot_data` function initializes the `faculty_allotment` dictionary with faculty IDs as keys and empty lists as values.

### 3. Reducing Course Weightage
- The `reduce` function reduces the course weightage for a specified faculty and course based on the given reduction value.
- This reduction is applied to both the category and course preferences for all faculty members.

### 4. Checking Faculty Load
- The `check` function checks if the course load for all faculty members is zero, indicating a valid allotment.

### 5. Faculty Course Allotment
- The `allotment` function performs the backtracking algorithm for faculty course allotment.
- It randomly selects a faculty, checks the load, and iterates through course preferences to make allotments.
- Recursion is used to explore different allotment possibilities.

### 6. Writing Output to CSV
- The final allotment results are written to an output CSV file named "output2.csv".
- The headers include 'faculty_id' and 'alloted_course'.

## How to Use:
1. Ensure you have a CSV file named "input2.csv" with the required faculty data.
2. Run the script.

```python
python script_name.py
```

3. View the output in "output2.csv" to see the faculty-wise course allotments.

Note: Make sure to replace 'script_name.py' with the actual name of your Python script.
