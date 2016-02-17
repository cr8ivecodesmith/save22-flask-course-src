from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    # long view code
    fruits = 'banana apple orange'.split()
    # long view code
    assert False
    return 'Hello world!'


if __name__ == '__main__':
    # Our app would've run on 127.0.0.1:5000 by default.
    app.run(host='0.0.0.0', port=8000, debug=True)
