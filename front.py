import psycopg
from flask import Flask, render_template

conn = psycopg.connect(
    user='postgres', password='1234', host='127.0.0.1', port='5432'
)
conn.autocommit = True

app = Flask (__name__)

@app.route("/")
def home_page():
  get_data_from_db = 'SELECT * FROM currencies';
  a=conn.cursor.execute(get_data_from_db)
  return render_template('main.html', a=a)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 1245)