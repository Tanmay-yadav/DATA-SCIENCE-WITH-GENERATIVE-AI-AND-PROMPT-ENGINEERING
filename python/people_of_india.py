import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 1000

# Define the data columns
data = {
    'Name': [fake.name() for _ in range(num_records)],
    'Place': [fake.city() for _ in range(num_records)],
    'Sex': [random.choice(['Male', 'Female']) for _ in range(num_records)],
    'Married': [random.choice(['Yes', 'No']) for _ in range(num_records)],
    'Income': [round(random.uniform(20000, 100000), 2) for _ in range(num_records)],
    'Age': [random.randint(18, 70) for _ in range(num_records)],
    'Caste': [random.choice(['General', 'OBC', 'SC', 'ST']) for _ in range(num_records)],
    'Occupation': [random.choice(['Engineer', 'Doctor', 'Student', 'Teacher', 'Business', 'Lawyer', 'Nurse', 'Artist', 'Scientist']) for _ in range(num_records)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_path = 'people_of_india.xlsx'
df.to_excel(file_path, index=False)

print(f"Excel file with {num_records} records has been created at {file_path}.")
