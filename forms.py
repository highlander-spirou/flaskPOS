from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    bill_number  = StringField('bill_number', validators=[DataRequired()])
    shipper_name  = StringField('shipper_name', validators=[DataRequired()])
    consignee_name   = StringField('consignee_name', validators=[DataRequired()])
    client_name   = StringField('client_name')
    consignee_address   = StringField('client_address', validators=[DataRequired()])
    consignee_telephone   = StringField('client_telephone', validators=[DataRequired()])
    cargo_pcs   = IntegerField('cargo_pcs', validators=[DataRequired()])
    cargo_weight = IntegerField('cargo_weight', validators=[DataRequired()])    
    pp_cc = StringField('pp_cc', validators=[DataRequired()])
    hs_code = IntegerField('hs_code', validators=[DataRequired()])
    cargo_item = StringField('cargo_item', validators=[DataRequired()])
    invoice_value  = IntegerField('invoice_value', validators=[DataRequired()])
    zipcode = StringField('zipcode', validators=[DataRequired()])
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