#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import multiprocessing as mp
import time

# File paths
students_file_path = "students.csv"
fees_file_path = "student_fees.csv"

# Load the datasets
students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

# Extract the day from the Payment Date in the fees dataset
fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)

# Function to calculate consistent payment days for a chunk of data
def calculate_consistent_payment_days(chunk):
    return chunk.groupby('Student ID')['Day'].agg(lambda x: x.mode()[0]).reset_index()

# Measure the start time
start_time = time.time()

# Split the fees dataset into chunks
num_partitions = mp.cpu_count()  # Number of CPU cores
chunk_size = len(fees_df) // num_partitions
chunks = [fees_df.iloc[i:i + chunk_size] for i in range(0, len(fees_df), chunk_size)]

# Use multiprocessing to process chunks in parallel
with mp.Pool(num_partitions) as pool:
    results = pool.map(calculate_consistent_payment_days, chunks)

# Combine results from all processes
consistent_payment_days = pd.concat(results).drop_duplicates(subset='Student ID')

# Merge the consistent payment data with the student information
merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

# Measure the end time
end_time = time.time()
execution_time = end_time - start_time

# Display runtime and a preview of the merged dataset
print(f"Execution Time: {execution_time} seconds")
merged_df


# In[ ]:




