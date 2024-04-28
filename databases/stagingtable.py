import duckdb as db

conn = db.connect('edw')
conn.execute("EXPORT DATABASE './databases/'")

import pandas as pd

# Specify the path to your CSV file
#csv_file_path = './sources/fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv'

# Use pandas to read the CSV file into a DataFrame
#df = pd.read_csv(csv_file_path)

# Display the DataFrame
#print(df)

import os

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Display the script directory
print("Script Directory:", script_directory)