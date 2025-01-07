import csv
import subprocess
from pymongo import MongoClient

subprocess.run(["mongod"])

client = MongoClient('mongodb://127.0.0.1:27017/')
dbnames = client.list_database_names()
if 'database' in dbnames:
    client.drop_database('database')
db = client['database']  
collection = db['collection']  

file_path = 'new_retail_data.csv'  

try:
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    if data:
        collection.insert_many(data)
        print(f"{len(data)} records successfully inserted!")
    else:
        print("The file is empty or not formatted correctly.")

    print("Inserted Documents:")
    for doc in collection.find():
        print(doc)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()


