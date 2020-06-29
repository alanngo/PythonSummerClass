from flask import *

app = Flask(__name__)


def tag(tg, txt):
    return "<" + tg + ">" + txt + "</" + tg + ">"


# root webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    return tag("h1", "Spongebob")


# localhost:5000/hello
@app.route('/hello')
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
