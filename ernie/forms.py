from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AskErnie(FlaskForm):
    prompt = StringField("prompt", default="Hello, This is Farmer Ernie. You might wonder why a city kid like me is doing out here in the [MASK]?")
