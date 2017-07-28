# coding : utf-8

import MySQLdb
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown') #http://192,168.1.173:8888/shutdown
def shutdown():
    shutdown_server()
    return 'Server shutting down..'

@app.route('/create') #http://192.168.1.173:8888
def create():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    cur.execute("create table Student(studentid int not null primary key, name varchar(20))")
    return render_template('create.html')
    cur.close()
    db.close()

@app.route('/insert') #http://192.168.1.173:8888
def insert():
    return render_template('insert.html')
#/insert?id=3&name=3


@app.route('/delete/<id>') #http://192.168.1.173:8888
def delete(id):
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    sql = "delete from Student where studentid = '%s'" %(id)
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
    return render_template('delete.html')

    cur.close()
    db.close()

@app.route('/select') #http://192.168.1.173:8888
def select():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    cur.execute("select * from Student")
    row = cur.fetchall()
    templateData = {'data' : row}
    return render_template('select.html',**templateData)

    cur.close()
    db.close()

@app.route('/select/<id>') #http://192.168.1.173:8888
def selecthyo(id):
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    sql = "select * from Student where studentid = '%c'" % (id)
    cur.execute(sql)
    row = cur.fetchall()

    templateData = {'data' : row}
    return render_template('select.html',**templateData)

    cur.close()
    db.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
    
