#!/usr/bin/env python3

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
from reg_reader import *
from reg_sender import *
from functools import wraps

app = Flask(__name__, static_url_path='')
app.secret_key = 'secret_key_'

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
	get_plc = get_plc_stat()
	if request.method == "POST":
		if request.form.get('fuel_rate'):
			print(request.form.get('fuel_rate'))
			if request.form.get('fuel_rate') == '0':
				fuel_rate_0()
			elif request.form.get('fuel_rate') == '1':
				fuel_rate_1()
			elif request.form.get('fuel_rate') == '2':
				fuel_rate_2()
			else:
				fuel_rate_3()
		if request.form.get('waterpump_io'):
			print(request.form.get('waterpump_io'))
			if request.form.get('waterpump_io') == '1':
				waterpump_on()
			else:
				waterpump_off()
		if request.form.get('boiler_io'):
			print(request.form.get('boiler_io'))
			if request.form.get('boiler_io') == '1':
				boiler_on()
			else:
				boiler_off()
		if request.form.get('turbine_io'):
			print(request.form.get('turbine_io'))
			if request.form.get('turbine_io') == '1':
				turbine_on()
			else:
				turbine_off()
		if request.form.get('generator_io'):
			print(request.form.get('generator_io'))
			if request.form.get('generator_io') == '1':
				generator_on()
			else:
				generator_off()
		if request.form.get('pylon_io'):
			print(request.form.get('pylon_io'))
			if request.form.get('pylon_io') == '1':
				pylon_on()
			else:
				pylon_off()
		if request.form.get('zero_out'):
			print (request.form.get('zero_out'))
			if request.form.get('zero_out') == '0':
				emergency_shutoff()
			else:
				pass
		else:
			pass
	print (get_plc_stat)
	return render_template('hmi.html',get_plc_stat=get_plc)

@app.route('/status',methods=['GET','POST'])
@login_required
def status_route():
	return render_template('status.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9001)
