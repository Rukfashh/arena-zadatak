from doctor import app
from flask import render_template , flash, url_for, redirect
from doctor.models import Patient, Doctor, PatientTomorrow
from doctor.forms import LoginForm
from flask_login import login_user

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form= LoginForm()  
    if form.validate_on_submit():
        attempted_user = Doctor.query.get(form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('dashboard_page'))  
        else:
            flash('Username and password are not matching! Please try again', category='danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard_page():
    patients = Patient.query.all()
    patientsTomorrow = PatientTomorrow.query.all()
    return render_template('dashboard.html', patients=patients, patientsTomorrow=patientsTomorrow)

