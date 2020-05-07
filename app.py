import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "dental_laboratory"
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_patients')
def get_patients():
    return render_template('patients.html', patients=mongo.db.patients.find())


@app.route('/add_patient')
def add_patient():
    return render_template('addpatient.html', jobs=mongo.db.jobs.find())


@app.route('/insert_patient', methods=['POST'])
def insert_patient():
    patients = mongo.db.patients
    patients.insert_one(request.form.to_dict())
    return redirect(url_for('get_patients'))


@app.route('/edit_patient/<patient_id>')
def edit_patient(patient_id):
    the_patient = mongo.db.patients.find_one({"_id": ObjectId(patient_id)})
    all_jobs = mongo.db.jobs.find()
    all_type = mongo.db.type.find()
    return render_template("editpatient.html", patient=the_patient,
                           jobs=all_jobs, type=all_type)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
