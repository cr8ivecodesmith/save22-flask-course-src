from wtforms import Form, TextField
from wtforms.validators import Length, required

class LocationForm(Form):
    name = TextField('Name', [Length(max=128), required()])


if __name__ == '__main__':
    from form_play import play
    play()
