from flask import Flask, render_template
import os
# static_path = os.path.join(project_root, '../templates/static')
app = Flask(__name__)
from datetime import datetime
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
            #self.a = list(cursor.execute(f'SELECT * FROM Novaya').fetchone())
            self.all = list(cursor.execute(f'SELECT * FROM Novaya').fetchall())
            self.all.reverse()
            for i in range(len(self.all)):
                self.all[i]=list(self.all[i])
            self.a = self.all[0]
            self.data = eval(str(self.a[6]))
            self.names1 = list(self.data.keys())
            # self.names1= ''
            # for i in list(self.data.keys()):
            #     self.names1+=i
            #     self.names1+=','

            self.len = len(list(self.data.keys()))
            self.data1=[]
            self.sum=[]
            self.sum_all=[]
            for k in list(self.data.keys()):
                self.sum0 = 0
                for i in range(720):
                    self.sum0+=int(str(eval(str(self.all[i][6]))[k]))
                    if i%24==0:
                        self.sum.append(self.sum0)
                        self.sum0 = 0
                self.sum.pop(0)
                self.sum_all.append(self.sum)
                self.sum=[]

            self.labels_month = []
            for i in range(29,-1,-1):
                self.labels_month.append(datetime.strptime(self.all[i*24][2],"%Y-%m-%d").strftime("%d.%m"))
            self.hour = self.a[3]
            self.labels=[]
            for i in range(self.hour+1,24):
                self.labels.append(i)
            for i in range(self.hour+1):
                self.labels.append(i)

            # for i in range(len(list(self.data.values())[0]) ):
            #     self.labels.append(i)
            # for i in list(self.data.keys()):
            #     self.data1[i] = []
            self.i=0
            for k in list(self.data.keys()):
                self.data1.append([])
                for j in self.all:
                    self.data1[self.i].append(eval(str(j[6]))[k])
                self.i+=1
    novaya = Novaya(cursor)

    return render_template('main_tem.html',points=points,file=f,novaya=novaya)
@app.route('/t')
def index1():
    return render_template('t.html',)


if __name__ == '__main__':
    app.run(debug = True)
