from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json
from forms import InputForm, EditForm, DeleteForm, CompanyForm, CompanyDeleteForm, ProductForm, ProductDeleteForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Input(db.Model):

    __tablename__ = 'input'

    id = db.Column(db.Integer, primary_key = True)
    bill_number = db.Column(db.String(64), index=True)
    shipper_name = db.Column(db.String(64), index=True)
    consignee_name = db.Column(db.String(64), index=True) #company name
    client_name = db.Column(db.String(64))  #optional
    consignee_address = db.Column(db.String(500))
    consignee_telephone = db.Column(db.String(64))
    cargo_pcs = db.Column(db.Integer) 
    cargo_weight = db.Column(db.Float) 
    pp_cc = db.Column(db.String(5))
    hs_code = db.Column(db.Integer)
    cargo_item = db.Column(db.String(500))
    invoice_value = db.Column(db.Float)
    bag_number = db.Column(db.String(64))
    zipcode = db.Column(db.String(64))


    def __init__(self, bill_number, shipper_name, consignee_name, consignee_address, consignee_telephone, cargo_pcs, cargo_weight, pp_cc, hs_code, cargo_item, invoice_value, bag_number, zipcode, client_name ="None"):
        self.bill_number = bill_number
        self.shipper_name = shipper_name
        self.consignee_name = consignee_name #company name
        self.consignee_address = consignee_address
        self.consignee_telephone = consignee_telephone
        self.cargo_pcs = cargo_pcs
        self.cargo_weight = cargo_weight
        self.pp_cc = pp_cc
        self.hs_code = hs_code
        self.cargo_item = cargo_item
        self.invoice_value = invoice_value
        self.bag_number = bag_number
        self.zipcode = zipcode
        self.client_name = client_name #keyword argument "None"

    def __repr__(self):
        return f"id: {self.id}, bill:{self.bill_number}, from: {self.shipper_name}, to: {self.consignee_name}"

class Companies(db.Model):

    __tablename__ = "companies"
    
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(64))
    address = db.Column(db.String(500))
    telephone = db.Column(db.String(64))
    zipcode = db.Column(db.String(64))

    def __init__(self, company, address, telephone, zipcode):
        self.company = company
        self.address = address
        self.telephone = telephone
        self.zipcode = zipcode

    def __repr__(self):
        return f"id: {self.id}, company: {self.company}"

class Products(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    code = db.Column(db.String(64))
    

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"id: {self.id}, product name: {self.name}"


class InputSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Input


@app.route('/', methods=["GET", "POST"])
def index():
    form=InputForm()
    if form.validate_on_submit():
        bill_number=form.bill_number.data
        shipper_name = form.shipper_name.data
        consignee_name = form.consignee_name.data
        client_name = form.client_name.data
        consignee_address = form.consignee_address.data
        consignee_telephone = form.consignee_telephone.data
        cargo_pcs = form.cargo_pcs.data
        cargo_weight = form.cargo_weight.data
        pp_cc = form.pp_cc.data
        hs_code = form.hs_code.data
        cargo_item = form.cargo_item.data
        invoice_value = form.invoice_value.data
        bag_number = form.bag_number.data
        zipcode = form.zipcode.data

        new_instance = Input(bill_number, shipper_name, consignee_name, consignee_address, consignee_telephone, cargo_pcs, cargo_weight, pp_cc, hs_code, cargo_item, invoice_value, bag_number, zipcode, client_name)
        
        db.session.add(new_instance)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('form.html', form=form)

@app.route('/tabledata', methods=["GET", "POST"])
def tabledata():
    inputs = Input.query.all()
    input_schema = InputSchema(many=True)
    output = input_schema.dump(inputs)
    return jsonify(output)

@app.route('/table', methods=["GET", "POST"])
def table():
    form = EditForm()
    if form.validate_on_submit():
        id = form.id.data
        bill_number=form.bill_number.data
        shipper_name = form.shipper_name.data
        consignee_name = form.consignee_name.data
        client_name = form.client_name.data
        consignee_address = form.consignee_address.data
        consignee_telephone = form.consignee_telephone.data
        cargo_pcs = form.cargo_pcs.data
        cargo_weight = form.cargo_weight.data
        pp_cc = form.pp_cc.data
        hs_code = form.hs_code.data
        cargo_item = form.cargo_item.data
        invoice_value = form.invoice_value.data
        bag_number = form.bag_number.data
        zipcode = form.zipcode.data

        instance = Input.query.get(id)
        instance.bill_number = bill_number
        instance.shipper_name = shipper_name
        instance.consignee_name = consignee_name #company name
        instance.consignee_address = consignee_address
        instance.consignee_telephone = consignee_telephone
        instance.cargo_pcs = cargo_pcs
        instance.cargo_weight = cargo_weight
        instance.pp_cc = pp_cc
        instance.hs_code = hs_code
        instance.cargo_item = cargo_item
        instance.invoice_value = invoice_value
        instance.bag_number = bag_number
        instance.zipcode = zipcode
        instance.client_name = client_name
        db.session.commit()
    

    form2 = DeleteForm()

    return render_template('table.html', form=form, form2=form2)

@app.route('/delete', methods=["GET", "POST"])
def delete():
    del_id = request.form['id']
    instance = Input.query.get(del_id)
    db.session.delete(instance)
    db.session.commit()
    return redirect(url_for('table'))


@app.route('/companytable', methods=["POST", "GET"])
def companytable():
    data_companies = Companies.query.all()
    form = CompanyForm()
    form2 = CompanyDeleteForm()
    return render_template('companyTable.html', data_companies=data_companies, form=form, form2=form2)

@app.route('/companydata') #JSON file here
def companydata():
    companies = Companies.query.all()
    company_list = []
    
    for company in companies:
        company_dict={}
        company_dict['id'] = company.id
        company_dict['company'] = company.company
        company_dict['address'] = company.address
        company_dict['telephone'] = company.telephone
        company_dict['zipcode'] = company.zipcode
        company_list.append(company_dict)
    
    return jsonify(company_list)


@app.route('/company/create', methods=["POST", "GET"])
def company_create():
    company = request.form['company']
    address = request.form['address']
    telephone = request.form['telephone']
    zipcode = request.form['zipcode']
    new_instance = Companies(company, address, telephone, zipcode)
    db.session.add(new_instance)
    db.session.commit()

    return redirect(url_for("companytable"))

@app.route('/company/delete', methods=["POST", "GET"])
def company_delete():

    del_id = request.form['id']
    instance = Companies.query.get(del_id)
    db.session.delete(instance)
    db.session.commit()

    return redirect(url_for('companytable'))



@app.route('/producttable', methods=["POST", "GET"])
def producttable():
    data_products = Products.query.all()
    form = ProductForm()
    form2 = ProductDeleteForm()
    return render_template('productTable.html', data_products=data_products, form=form, form2=form2)

@app.route('/productdata') #JSON file here
def productdata():
    products = Products.query.all()
    product_list = []
    
    for product in products:
        product_dict={}
        product_dict['id'] = product.id
        product_dict['product'] = product.name
        product_dict['hs_code'] = product.code
        product_list.append(product_dict)
    
    return jsonify(product_list)


@app.route('/product/create', methods=["POST", "GET"])
def product_create():
    product = request.form['product']
    hs_code = request.form['hs_code']
    new_instance = Products(product, hs_code)
    db.session.add(new_instance)
    db.session.commit()

    return redirect(url_for("producttable"))

@app.route('/product/delete', methods=["POST", "GET"])
def product_delete():

    del_id = request.form['id']
    instance = Products.query.get(del_id)
    db.session.delete(instance)
    db.session.commit()

    return redirect(url_for('producttable'))


if __name__ == '__main__':
    app.run(debug=True)
