#!/usr/bin/env python

from flask import Flask
from flask import abort
from flask import flash
from flask import g
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from reg_sender import *
from functools import wraps

app = Flask(__name__, static_url_path='')
app.secret_key = 'secret_key_'
stat = {}

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index_route'))
    return wrap

@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login_route():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if username == 'admin' and password == 'admin':
        session['logged_in'] = 1 
    return redirect(url_for('index_route'))

@app.route('/hmi',methods=['GET','POST'])
@login_required
def hmi_route():
	if request.method == "POST":
		if request.form.get('fuel_rate'):
			print(request.form.get('fuel_rate'))
			if request.form.get('fuel_rate') == '0':
				stat['fuel_stat'] = "OFF"
				fuel_rate_0()
			elif request.form.get('fuel_rate') == '1':
				stat['fuel_stat'] = "LOW"
				fuel_rate_1()
			elif request.form.get('fuel_rate') == '2':
				stat['fuel_stat'] = "NORMAL"
				fuel_rate_2()
			else:
				stat['fuel_stat'] = "MAX"
				fuel_rate_3()
		if request.form.get('waterpump_io'):
			print(request.form.get('waterpump_io'))
			if request.form.get('waterpump_io') == '1':
				stat['waterpump_stat'] = "ON"
				waterpump_on()
			else:
				stat['waterpump_stat'] = "OFF"
				waterpump_off()
		if request.form.get('boiler_io'):
			print(request.form.get('boiler_io'))
			if request.form.get('boiler_io') == '1':
				stat['boiler_stat'] = "ON"
				boiler_on()
			else:
				stat['boiler_stat'] = "OFF"
				boiler_off()
		if request.form.get('turbine_io'):
			print(request.form.get('turbine_io'))
			if request.form.get('turbine_io') == '1':
				stat['turbine_stat'] = "ON"
				turbine_on()
			else:
				stat['turbine_stat'] = "OFF"
				turbine_off()
		if request.form.get('generator_io'):
			print(request.form.get('generator_io'))
			if request.form.get('generator_io') == '1':
				stat['generator_stat'] = "ON"
				generator_on()
			else:
				stat['generator_stat'] = "OFF"
				generator_off()
		if request.form.get('pylon_io'):
			print(request.form.get('pylon_io'))
			if request.form.get('pylon_io') == '1':
				stat['pylon_stat'] = "ON"
				pylon_on()
			else:
				stat['pylon_stat'] = "OFF"
				pylon_off()
		if request.form.get('zero_out'):
			print (request.form.get('zero_out'))
			if request.form.get('zero_out') == '0':
				stat['fuel_stat'] = "OFF"
				stat['waterpump_stat'] = "OFF"
				stat['boiler_stat'] = "OFF"
				stat['turbine_stat'] = "OFF"
				stat['generator_stat'] = "OFF"
				stat['pylon_stat'] = "OFF"
				emergency_shutoff()
		else:
			pass
	return render_template('hmi.html',stat=stat)

@app.route('/status',methods=['GET','POST'])
@login_required
def status_route():
	return render_template('status.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9001)
