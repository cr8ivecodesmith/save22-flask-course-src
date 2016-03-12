from wtforms import Form, TextField
from wtforms.validators import Length, required

class UserForm(Form):
    """
    Form classes are typically a reflection of the model
    they operate in.
    """
    username = TextField('Username', [Length(max=128), required()])

if __name__ == '__main__':
    from form_play import play
    play()
