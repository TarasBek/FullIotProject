from flask import Flask, render_template,request
import mysql.connector
import database
app = Flask(__name__)


@app.route("/data")
def get_data():
    while True:
        cur = database.mycursor
        cur.execute('SELECT MAX(id) FROM temperature')
        (last_id) = cur.fetchone()
        get_last_recond_id = ("SELECT *  FROM temperature WHERE id = %s")
        cur.executemany(get_last_recond_id, (last_id,))
        data = cur.fetchall()
        return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)