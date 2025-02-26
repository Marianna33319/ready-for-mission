from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    param = {}
    param['h1'] = 'Миссия Колонизация Марса'
    param['h4'] = 'И на Марсе будут яблони цвести!'
    param['title'] = 'подстановка'
    return render_template("base.html", **param)


@app.route('/training/<prof>')
def training(prof):
    return  render_template("training.html", prof=prof.lower())


@app.route('/list_prof/<mrk>')
def list_prof(mrk):
    profession = ['врач', 'строитель', 'инженер']
    return  render_template('list_prof.html', profession=profession, mrk=mrk.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)

