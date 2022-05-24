import models
import psycopg
from func_Days_less10 import func_Days_less10
from func_for_days_more_than_10 import func_for_days_more_than_10
from models import cursor
from flask import Flask, render_template, request
models.create_database_and_table()
func_Days_less10()
func_for_days_more_than_10()


conn = psycopg.connect(
    user='postgres', password='1234', host='127.0.0.1', port='5432'
)
conn.autocommit = True

app = Flask (__name__)

@app.route("/",  methods=['POST', 'GET'])
def spisok():
  get_data_from_db = "SELECT DISTINCT data from currencies ORDER by data;";
  cursor.execute(get_data_from_db)
  data=cursor.fetchall()
  return render_template('spisok.html', data=data)




@app.route("/currencies", methods=['POST', 'GET'])
def home_page():
  chosen_data = request.form.get('data')
  get_data_from_db = f"select * from currencies  where data = '{chosen_data}' order by name;";
  cursor.execute(get_data_from_db)
  my_table=cursor.fetchall()
    # cursor.close()
    # conn.close()

  return render_template('main.html', my_table=my_table, chosen_data=chosen_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 1245)








