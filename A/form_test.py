from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def shutdown_server() :
    func = request.environ.get('werzeug.server.shutdown')
    if func is None :
        raise RuntimeError('Not running with the Werkzeoug Server')
        func()

@app.route('/shutdown')
def shutdown() : # 콜백함수
    shutdown_server()
    return'Server shutting down..'

@app.route('/mainpage', methods = ['POST']) # 파이썬으로 데이터 전향
def mainpage() : # 콜백함수
    name = request.form['name'] # 네임에 입력치를 받아
    nameData = { 'name' : name } # 사전정의 키:'name'
    return render_template('test5.html', **nameData) # test5로 전송

@app.route('/')
def root() :
    return render_template('test4.html') # mainpage

if __name__ == "__main__" : # 다른 사용자 사용금지
    app.run(host = '0.0.0.0', port = 8888, debug = True) # 서버접속
