import models
import psycopg
from func_Days_less10 import func_Days_less10
from func_for_days_more_than_10 import func_for_days_more_than_10
from models import cursor
#from flask import Flask, render_template
models.create_database_and_table()
func_Days_less10()
func_for_days_more_than_10()



conn = psycopg.connect(
    user='postgres', password='1234', host='127.0.0.1', port='5432'
)
conn.autocommit = True

def home_page():
  get_data_from_db = 'SELECT * FROM currencies ORDER BY data, name';
  cursor.execute(get_data_from_db)
  my_table=cursor.fetchall()
  for row in my_table:
      print( row[0], row[1], row [2], row[3], row[4], row[5], row[6] )



home_page()












#app = Flask (__name__)

#@app.route("/")
#def home_page():
 #   get_data_from_db = 'SELECT * FROM currencies';
#    a=conn.cursor.execute(get_data_from_db)
#    print(a)
#    return render_template('main.html', a=a)



#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port = 12645)
