from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/top')
def top():
    return "ここはトップだよ〜(๑>◡<๑)"


@app.route('/hello/<text>')
def namehello(text):
    return text + "さんこんにちは"


@app.route('/index')
def index():
    name="sunabaco"
    age = 20
    address = "田町"
    return render_template('index2.html',user_name = name,user_address = address, user_age = age)


@app.route('/weather')
def weather():
    weather = "晴れ"
    return render_template('weather.html',html_weather = weather)


@app.route('/dbtest')
def dbtest():
    #dbに接続
    conn = sqlite3.connect('flasktest2.db')
    c = conn.cursor()
    #SQLの命令を書く
    c.execute("SELECT name,age,address FROM user WHERE id = 1")
    user_info = c.fetchone()
    #dbの処理終了
    c.close()
    print(user_info)
    return render_template('dbtest.html', db_userinfo = user_info)









if __name__ == '__main__':
    app.run(debug=True)