from flask import Flask, render_template, redirect, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from app.models import Base, Location
from app.forms import LocationForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite3'
db = SQLAlchemy(app)
db.Model = Base


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LocationForm(request.form)
    if request.method == 'POST' and form.validate():
        location = Location()
        form.populate_obj(location)
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('welcome.html', form=form)


if __name__ == '__main__':
    app.run()
