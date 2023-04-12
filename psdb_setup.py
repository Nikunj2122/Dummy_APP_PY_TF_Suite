import psycopg2
import json

db_host = "your-cloud-sql-host"
db_name = "your-db-name"
db_user = "your-db-username"
db_password = "your-db-password"

conn = psycopg2.connect(
   host=db_host,
   dbname=db_name,
   user=db_user,
   password=db_password
)

cur = conn.cursor()

query = "SELECT * FROM "binding";"

cur.execute(query)

results = cur.fetchall()

json_data = json.dumps(results)

print(json_data)
