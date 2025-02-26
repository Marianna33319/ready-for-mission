from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    param = {}
    param['h1'] = 'Миссия Колонизация Марса'
    param['h4'] = 'И на Марсе будут яблони цвести!'
    param['title'] = 'подстановка'
    return render_template("base.html", **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
