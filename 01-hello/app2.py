from flask import (
    Flask,
    render_template,
    request,
    session,
    url_for,
)
app = Flask(__name__)




@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/<name>/<int:answer>')
def guess(name=None, answer=0):
    name = name or 'Anonymous'

    correct = (answer == 42)
    foo = {'name': 'foo', 'location': (234, 234)}
    fruits = 'apple banana orange'.split()
    if name == 'foo':
        session['logged_in'] = True

    return render_template(
        'guess2.html',
        name=name,
        correct=correct,
        foo=foo,
        fruits=fruits,
    )


app.secret_key = '4ga4gasrgh5usths5'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
