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

"""-----------------------------Read----------------------------------"""


@app.route('/')
@app.route('/get_patients')
def get_patients():
    return render_template('patients.html', patients=mongo.db.patients.find())


"""-----------------------------Create--------------------------------"""


@app.route('/add_patient')
def add_patient():
    return render_template('addpatient.html', jobs=mongo.db.jobs.find())


@app.route('/insert_patient', methods=['POST'])
def insert_patient():
    patients = mongo.db.patients
    patients.insert_one(request.form.to_dict())
    return redirect(url_for('get_patients'))


"""-----------------------------Update---------------------------------"""


@app.route('/edit_patient/<patient_id>')
def edit_patient(patient_id):
    the_patient = mongo.db.patients.find_one({"_id": ObjectId(patient_id)})
    all_jobs = mongo.db.jobs.find()
    all_type = mongo.db.type.find()
    return render_template("editpatient.html", patient=the_patient,
                           jobs=all_jobs, type=all_type)


@app.route('/update_patient/<patient_id>', methods=['POST'])
def update_patient(patient_id):
    patients = mongo.db.patients
    patients.update({'_id': ObjectId(patient_id)},
                    {'patient_name': request.form.get('patient_name'),
                    'patient_dob': request.form.get('patient_dob'),
                     'gender': request.form.get('gender'),
                     'type_patient': request.form.get('type_patient'),
                     'due_date': request.form.get('due_date'),
                     'job_name': request.form.get('job_name'),
                     'is_urgent': request.form.get('is_urgent')})
    return redirect(url_for('get_patients'))


"""-------------------------------Delete---------------------------------"""


@app.route('/delete_patient/<patient_id>')
def delete_patient(patient_id):
    mongo.db.patients.remove({'_id': ObjectId(patient_id)})
    return redirect(url_for('get_patients'))


"""-------------------------------Read-----------------------------------"""


@app.route('/get_jobs')
def get_jobs():
    return render_template('jobs.html', jobs=mongo.db.jobs.find())


@app.route('/get_type')
def get_type():
    return render_template('type.html', type=mongo.db.type.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
