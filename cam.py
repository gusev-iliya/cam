from flask import Flask, render_template
app = Flask(__name__)
import data
import sqlite3
import ast
@app.route('/')
def index():
    document = open('main.txt','r', encoding="utf-8")
    f = document.read()
    document.close()
    nov = data.novaya
    all_novaya=data.all_novaya
    teatr = data.teatralnaya
    connect = sqlite3.connect('cam.db')
    cursor = connect.cursor()
    points = list(cursor.execute(f'SELECT * FROM points').fetchall())

    novaya = list(cursor.execute(f'SELECT * FROM Novaya').fetchone())
    class Novaya():
        def __init__(self, novaya):
            self.data = eval(str(novaya[6]))
            self.names = ','.join(list(self.data.keys()))
            self.len = len(list(self.data.keys()))

    novaya = Novaya(novaya)

    return render_template('main_tem.html',points=points,file=f,novaya=novaya)



if __name__ == '__main__':
    app.run(debug = True)
