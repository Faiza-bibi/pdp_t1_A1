#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import time

students_file_path = "students.csv"
fees_file_path = "student_fees.csv"

students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

start_time = time.time()

fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)
consistent_payment_days = fees_df.groupby('Student ID')['Day'].agg(lambda x: x.mode()[0]).reset_index()
consistent_payment_days.rename(columns={'Day': 'Most Consistent Payment Day'}, inplace=True)

merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")
merged_df

