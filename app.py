import models
import psycopg
from func_Days_less10 import func_Days_less10
from func_for_days_more_than_10 import func_for_days_more_than_10
from models import cursor
from flask import Flask, render_template
models.create_database_and_table()
func_Days_less10()
func_for_days_more_than_10()



conn = psycopg.connect(
    user='postgres', password='1234', host='127.0.0.1', port='5432'
)
conn.autocommit = True

app = Flask (__name__)
@app.route("/")
def home_page():
  get_data_from_db = "SELECT * FROM currencies";  #'SELECT * FROM currencies ORDER BY data, name';
  cursor.execute(get_data_from_db)
  my_table=cursor.fetchall()
  for row in my_table:
      data=row[0]
      id=row[1]
      numcode=row[2]
      charcode=row[3]
      nominal=row[4]
      name=row[5]
      value=row[6]
      #print( id, numcode, charcode, nominal, name, value )
      return render_template('main.html', data=data, id=id, numcode=numcode, charcode=charcode, nominal=nominal, name=name, value=value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 1245)















