import psycopg
from func_Days_less10 import *
#import func_Days_less10

conn = psycopg.connect(
    user='postgres', password='1234', host='127.0.0.1', port='5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
def create_database_and_table():
  delete_database='DROP DATABASE IF EXISTS currencies';
  create_database = '''CREATE DATABASE currencies ''';
  create_table='CREATE TABLE IF NOT EXISTS currencies (data VARCHAR(255), id VARCHAR(255), numcode VARCHAR(255), charcode VARCHAR(255), nominal VARCHAR(255), name VARCHAR(255), value VARCHAR(255))';
  cursor.execute(delete_database)
  print("Database deleted successfully........")
  cursor.execute(create_database)
  print("Database created successfully........")
  cursor.execute(create_table)
  print("Table created successfully........")


#Closing the connection
#conn.close()

