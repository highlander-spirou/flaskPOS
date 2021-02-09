from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    bill_number = StringField('bill_number', validators=[DataRequired()])
    shipper_name = StringField('shipper_name', validators=[DataRequired()])
    consignee_name = StringField('consignee_name', validators=[DataRequired()])
    client_name = StringField('client_name')
    consignee_address = StringField('client_address', validators=[DataRequired()])
    consignee_telephone = StringField('client_telephone', validators=[DataRequired()])
    cargo_pcs = IntegerField('cargo_pcs', validators=[DataRequired()])
    cargo_weight = FloatField('cargo_weight', validators=[DataRequired()])    
    pp_cc = StringField('pp_cc', validators=[DataRequired()])
    hs_code = IntegerField('hs_code', validators=[DataRequired()])
    cargo_item = StringField('cargo_item', validators=[DataRequired()])
    invoice_value = FloatField('invoice_value', validators=[DataRequired()])
    bag_number = StringField('bag_number', validators=[DataRequired()])
    zipcode = StringField('zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    bill_number = StringField('bill_number', validators=[DataRequired()])
    shipper_name = StringField('shipper_name', validators=[DataRequired()])
    consignee_name = StringField('consignee_name', validators=[DataRequired()])
    client_name = StringField('client_name')
    consignee_address = StringField('client_address', validators=[DataRequired()])
    consignee_telephone = StringField('client_telephone', validators=[DataRequired()])
    cargo_pcs = IntegerField('cargo_pcs', validators=[DataRequired()])
    cargo_weight = FloatField('cargo_weight', validators=[DataRequired()])    
    pp_cc = StringField('pp_cc', validators=[DataRequired()])
    hs_code = IntegerField('hs_code', validators=[DataRequired()])
    cargo_item = StringField('cargo_item', validators=[DataRequired()])
    invoice_value = FloatField('invoice_value', validators=[DataRequired()])
    bag_number = StringField('bag_number', validators=[DataRequired()])
    zipcode = StringField('zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField('DELETE')


class CompanyForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CompanyDeleteForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField('DELETE')


class ProductForm(FlaskForm):
    product = StringField('Product', validators=[DataRequired()])
    hs_code = StringField('hs_code', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProductDeleteForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField('DELETE')



class HansolInputForm(FlaskForm):
    bill_number = StringField('bill_number', validators=[DataRequired()])
    shipper_name = StringField('shipper_name', validators=[DataRequired()])
    consignee_name = StringField('consignee_name', validators=[DataRequired()], widget=TextArea())
    cargo_pcs = IntegerField('cargo_pcs', validators=[DataRequired()])
    cargo_weight = FloatField('cargo_weight', validators=[DataRequired()])    
    cargo_item = StringField('cargo_item', validators=[DataRequired()])
    submit = SubmitField('Submit')


class HansolEditForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    bill_number = StringField('bill_number', validators=[DataRequired()])
    shipper_name = StringField('shipper_name', validators=[DataRequired()])
    consignee_name = StringField('consignee_name', validators=[DataRequired()])
    cargo_pcs = IntegerField('cargo_pcs', validators=[DataRequired()])
    cargo_weight = FloatField('cargo_weight', validators=[DataRequired()])    
    cargo_item = StringField('cargo_item', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HansolDeleteForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField('DELETE')