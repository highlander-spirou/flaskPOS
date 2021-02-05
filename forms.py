from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField('DELETE')


class FixedForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')