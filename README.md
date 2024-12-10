## pdp_t1_A1
This repository aims to compare the execution time between linear and parallel processing.
#  linear and parallel execution
This project involves processing two CSV files: one containing student information and the other containing fee payment details. The goal is to ensure data integrity, generate fee payment dates, determine the most frequent payment date for each student, and implement both linear and parallel execution versions of the code to perform the tasks efficiently.
### Table of contents:
1. Overview
2. CSV File Structure
3. Code Functionality
   3.1 Linear Execution
   3.2 Parallel Execution (Using multiprocessing)
6. Performance Comparison
7. Running the Code
8. Results
## Overview:
The project has two main tasks:
Data Integrity: 
Ensure that each student in the students CSV has a corresponding fee payment in the student_fees CSV.
Payment Date Analysis:
Generate a list of payment dates for each student based on monthly payments.
Identify the most frequent payment date for each student.
Execution Variants: 
Implement both linear execution and parallel execution (using the multiprocessing module) to handle the task, and compare their performance.
The solution was implemented using Python and the pandas library for data manipulation.
## Code Functionality:
#### Linear Execution:
In the linear execution approach, the program reads both the students.csv and student_fees.csv files, ensures each student appears in both files, generates a list of payment dates for each student, and determines the most frequent payment date for each student sequentially.
#### Parallel Execution (Using multiprocessing):
In the parallel execution approach, the program uses Python's multiprocessing library to parallelize the task of determining the most frequent payment date for each student. This significantly reduces processing time by utilizing multiple CPU cores.
## Performance Comparison:
The linear execution approach processes the data sequentially, whereas the parallel execution approach distributes the workload to multiple processes, which should ideally reduce execution time.
The performance comparison is measured by timing the execution of both approaches using Python's time module.
