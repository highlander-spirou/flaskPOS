from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json
from forms import InputForm, EditForm, DeleteForm, FixedForm

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
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    role = db.Column(db.String(64))
    company = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.String(64))


    def __init__(self, name, age, role, company, city, zipcode):
        self.name = name
        self.age = age
        self.role = role
        self.company = company
        self.city = city
        self.zipcode = zipcode

    def __repr__(self):
        return f"id: {self.id}, name:{self.name}, company: {self.company}"

class Companies(db.Model):

    __tablename__ = "companies"
    
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.String(64))

    def __init__(self, company, city, zipcode):
        self.company = company
        self.city = city
        self.zipcode = zipcode

    def __repr__(self):
        return f"id: {self.id}, company: {self.company}"

class InputSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Input


@app.route('/', methods=["GET", "POST"])
def index():
    form=InputForm()
    if form.validate_on_submit():
        new_instance = Input(name=form.name.data,
                age=form.age.data,
                role=form.role.data,
                company=form.company.data,
                city=form.city.data,
                zipcode=form.zipcode.data)
        
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
        new_name=form.name.data
        new_age=form.age.data
        new_role=form.role.data
        new_company=form.company.data
        new_city=form.city.data
        new_zipcode=form.zipcode.data

        instance = Input.query.filter_by(name=new_name).first()
        instance.age = new_age
        instance.role = new_role
        instance.company = new_company
        instance.city = new_city
        instance.zipcode = new_zipcode
        db.session.commit()
    

    form2 = DeleteForm()
    if form2.validate_on_submit():
        del_id = form2.id.data
        instance = Input.query.get(del_id)
        db.session.delete(instance)
        db.session.commit()

    return render_template('table.html', form=form, form2=form2)

@app.route('/fixed')
def fixed():
    data_companies = Companies.query.all()
    return render_template('fix_data.html', data_companies=data_companies)

@app.route('/fixed_data')
def fixed_data():
    companies = Companies.query.all()
    company_list = []
    
    for company in companies:
        company_dict={}
        company_dict['id'] = company.id
        company_dict['company'] = company.company
        company_dict['city'] = company.city
        company_dict['zipcode'] = company.zipcode
        company_list.append(company_dict)
    
    return jsonify(company_list)


@app.route('/fixed/create', methods=["POST", "GET"])
def fixed_create():
    form = FixedForm()
    if form.validate_on_submit():
        fix_company = form.company.data
        fix_city = form.city.data
        fix_zipcode = form.zipcode.data
        new_instance = Companies(fix_company, fix_city, fix_zipcode)
        db.session.add(new_instance)
        db.session.commit()

    return render_template('fix_create.html', form=form)

@app.route('/fixed/delete', methods=["POST", "GET"])
def fixed_delete():
    pass

if __name__ == '__main__':
    app.run(debug=True)
