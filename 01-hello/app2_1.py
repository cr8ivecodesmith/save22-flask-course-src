from flask import Flask, make_response, request


app = Flask(__name__)


@app.route('/string/')
def return_string():
    return 'hello world!'


@app.route('/object/')
@app.route('/object/<foo>/')
def return_object(foo=None):
    response = make_response('hello world', 401)
    response.headers['Content-Type'] = 'text/plain'
    assert False
    return response


@app.route('/tuple/')
def return_tuple():
    headers = {'Content-Type': 'text/plain'}
    return ('hello world!', 200, headers)
    # return ('hello world!', 200)
    # return ('hello world!', headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
