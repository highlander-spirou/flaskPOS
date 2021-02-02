from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Sign In')