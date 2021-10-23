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
        def __init__(self, cursor):
            self.a = list(cursor.execute(f'SELECT * FROM Novaya').fetchone())
            self.all = list(cursor.execute(f'SELECT * FROM Novaya').fetchall())
            self.data = eval(str(self.a[6]))
            self.names = ','.join(list(self.data.keys()))
            self.names1= ''
            for i in list(self.data.keys()):
                self.names1+=i
                self.names1+=','
            self.len = len(list(self.data.keys()))
            self.data1 = ''
            self.max=0
            self.labels=[]
            # for i in range(len(list(self.data.values())[0]) ):
            #     self.labels.append(i)
            # for i in list(self.data.keys()):
            #     self.data1[i] = []
            for i in self.all:
                self.max+=1
            for k in list(self.data.keys()):

                for j in self.all:
                    self.data1+= str(eval(str(j[6]))[k])
                    self.data1+=','
                self.data1+='$'

            for i in range(self.max):

                self.labels.append(i)
    novaya = Novaya(cursor)

    return render_template('main_tem.html',points=points,file=f,novaya=novaya)
@app.route('/t')
def index1():
    return render_template('t.html',)

if __name__ == '__main__':
    app.run(debug = True)
