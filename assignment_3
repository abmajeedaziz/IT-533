# ==========================================
# Assignment: Convert CSV data to JSON
# File used: SalesJan2009.csv
# Output file: transaction_data.json
# ==========================================

import json

# Creating an empty list called "sales_data"

sales_data = []

# Open the CSV file and process its data
# Fields in order:
# Transaction_date, Product, Price, Payment_Type,
# Name, City, State, Country

input_file = "data_files/SalesJan2009.csv"
output_file = "output_files/transaction_data.json"

with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        # Processing  line-by-line & Cleaning extra quote characters &
        # Creating a dictionary for each line & Appending each dictionary to sales_data        
        # Remove extra spaces/newline characters

        line = line.strip()
        
        # Split line by comma
        parts = line.split(",")

        # Remove extra quote characters from each field
        cleaned_parts = [item.strip().replace('"', '') for item in parts]

        # Create dictionary for the current transaction
        transaction = {
            "Transaction_date": cleaned_parts[0],
            "Product": cleaned_parts[1],
            "Price": cleaned_parts[2],
            "Payment_Type": cleaned_parts[3],
            "Name": cleaned_parts[4],
            "City": cleaned_parts[5],
            "State": cleaned_parts[6],
            "Country": cleaned_parts[7]
        }

        # Append dictionary to sales_data list
        sales_data.append(transaction)

# Saving sales_data list to transaction_data.json

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(sales_data, json_file, indent=4)

print("CSV data has been converted to JSON successfully.")
print(f"Output saved in: {output_file}")