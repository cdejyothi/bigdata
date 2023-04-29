     
   from google.cloud import bigquery

# Create a BigQuery client object
client = bigquery.Client()

# Define the schema for the table
schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("age", "INTEGER"),
    bigquery.SchemaField("city", "STRING"),
]

# Create a table reference
table_ref = client.stack.python1

# Create the table
table = bigquery.python1(table_ref, schema=schema)
table = client.create_table(python1)

# Insert data into the table
rows_to_insert = [
    ("John", 25, "New York"),
    ("Jane", 30, "San Francisco"),
    ("Bob", 45, "Seattle"),
]

errors = client.insert_rows(table, rows_to_insert)

if errors == []:
    print("Data inserted successfully.") 
    
    
    
    
    
    
    
    
    
    