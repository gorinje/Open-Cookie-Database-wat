import csv
import json

# File paths
OCD_CSV = 'open-cookie-database.csv'
WAT_JSON = 'open-cookie-database-wat.json'

# Attributions
WAT_DATA = {
    "name": "Open Cookie Database",
    "author": "jkwakman",
    "category": "cookie",
    "trustLevel": "informative",
    "used": True,
}

# Mapping from csv to json
COLUMN_MAPPING = {
    "Domain": "domain",
    "Description": "comment",
    "Cookie / Data Key name": "name",
    "User Privacy & GDPR Rights Portals" : "policy",
    "Data Controller" : "controller",
    "Category" : "category"
}

# Clean up columns with no equivalence in the wat knowledge base
EXCLUDED_COLUMNS = {"ID", "Platform", "Retention period", "Wildcard match"}

def ocd_to_wat(input_csv, output_json):
    try:
        with open(input_csv, mode='r', encoding='utf-8') as ocd_csv:
            csv_reader = csv.DictReader(ocd_csv)
            data = []
            
            # Converting each row in the CSV
            for row in csv_reader:
                 # Conversion
                
                renamed_row = {COLUMN_MAPPING.get(key, key): value for key, value in row.items()}

                # Set * instead of empty domains
                renamed_row["domain"] = renamed_row.get("domain", "").strip() or "*"
                
                # Add source information
                renamed_row["source"] = "Open Cookie Database"

                
                # Convert open database wildcards
                if row.get("Wildcard match") == "1":
                    renamed_row["name"] = f"*{renamed_row.get('name', '').strip()}*"
                    renamed_row["wildcard_match"] = 1
                else:
                    renamed_row["wildcard_match"] = 0
                
                filtered_row = {key: value for key, value in renamed_row.items() if key not in EXCLUDED_COLUMNS}
                data.append(filtered_row)
        
            WAT_DATA["knowledges"] = data

        with open(output_json, mode='w', encoding='utf-8') as wat_json:
            json.dump(WAT_DATA, wat_json, indent=4)

        print(f"{OCD_CSV} file from in open-cookie-database format has been converted to website audit format JSON format and saved as {WAT_JSON}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' does not exist. Please check the file path.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to encode JSON. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


ocd_to_wat(OCD_CSV, WAT_JSON)

