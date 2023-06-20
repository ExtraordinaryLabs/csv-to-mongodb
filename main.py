import csv
import pandas as pd
from pymongo import MongoClient



MONGODB_CONNECTION_STRING = 'mongodb+srv:...'
df = pd.read_csv('myfile.csv')

# Rename the columns in case they aren't in lower case separeted by underscore
df.columns = df.columns.str.lower().str.replace(' ', '_')

# # Save the DataFrame to a new CSV file
df.to_csv('myfile2.csv', index=False)

# Connection to MongoDB
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.your_db

# Open the CSV
with open('myfile2.csv', 'r') as file:
    csv_data = csv.DictReader(file)

    for row in csv_data:
        db.your_collection.insert_one(row)