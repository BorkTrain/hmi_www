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
				fuel_rate_0()
			elif request.form.get('fuel_rate') == '1':
				fuel_rate_1()
			elif request.form.get('fuel_rate') == '2':
				fuel_rate_2()
			else:
				fuel_rate_3()
		if request.form.get('waterpump_io'):
			print(request.form.get('waterpump_io'))
			if request.form.get('waterpump_io') == '0':
				waterpump_off()
			else:
				waterpump_on()
		if request.form.get('boiler_io'):
			print(request.form.get('boiler_io'))
			if request.form.get('boiler_io') == '0':
				boiler_off()
			else:
				boiler_on()
		if request.form.get('turbine_io'):
			print(request.form.get('turbine_io'))
			if request.form.get('turbine_io') == '0':
				turbine_off()
			else:
				turbine_on()
		if request.form.get('generator_io'):
			print(request.form.get('generator_io'))
			if request.form.get('generator_io') == '0':
				generator_off()
			else:
				generator_on()
		if request.form.get('pylon_io'):
			print(request.form.get('pylon_io'))
			if request.form.get('pylon_io') == '0':
				pylon_off()
			else:
				pylon_on()
	return render_template('hmi.html')

@app.route('/status',methods=['GET','POST'])
@login_required
def status_route():
	if request.method == 'POST':
		print(request.form.get('zero_out'))
		if request.form.get('zero_out') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('FUEL'))
				send_to_plc(i,0,PLCS.get('WATERPUMP'))
				send_to_plc(i,0,PLCS.get('BOILER'))
				send_to_plc(i,0,PLCS.get('TURBINE'))
				send_to_plc(i,0,PLCS.get('GENERATOR'))
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			return render_template('status.html')
	return render_template('status.html')

@app.route('/fuel',methods=['GET','POST'])
@login_required
def fuel_route():
	if request.method == 'POST':
		print(request.form.get('fuel_rate'))
		if request.form.get('fuel_rate') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('FUEL'))
			for i in (10,11):
				send_to_plc(i,0,PLCS.get('WATERPUMP'))
				send_to_plc(i,0,PLCS.get('BOILER'))
				send_to_plc(i,0,PLCS.get('TURBINE'))
				send_to_plc(i,0,PLCS.get('GENERATOR'))
				send_to_plc(i,0,PLCS.get('PYLON'))
		elif request.form.get('fuel_rate') == '1':
			for i in range(1,17):
				send_to_plc(i,1,PLCS.get('FUEL'))
			send_to_plc(10,1,PLCS.get('WATERPUMP'))
			for i in (10,11):
				send_to_plc(i,1,PLCS.get('BOILER'))
				send_to_plc(i,1,PLCS.get('TURBINE'))
				send_to_plc(i,1,PLCS.get('GENERATOR'))
				send_to_plc(i,1,PLCS.get('PYLON'))
		elif request.form.get('fuel_rate') == '2':
			for i in range(1,17):
				send_to_plc(i,2,PLCS.get('FUEL'))
			send_to_plc(10,1,PLCS.get('WATERPUMP'))
			send_to_plc(10,1,PLCS.get('BOILER'))
			send_to_plc(10,1,PLCS.get('TURBINE'))
			send_to_plc(10,1,PLCS.get('GENERATOR'))
			send_to_plc(10,1,PLCS.get('PYLON'))
			send_to_plc(11,2,PLCS.get('BOILER'))
			send_to_plc(11,2,PLCS.get('TURBINE'))
			send_to_plc(11,2,PLCS.get('GENERATOR'))
			send_to_plc(11,2,PLCS.get('PYLON'))
		elif request.form.get('fuel_rate') == '3':
			for i in range(1,17):
				send_to_plc(i,3,PLCS.get('FUEL'))
			send_to_plc(10,1,PLCS.get('WATERPUMP'))
			send_to_plc(10,1,PLCS.get('BOILER'))
			send_to_plc(10,1,PLCS.get('TURBINE'))
			send_to_plc(10,1,PLCS.get('GENERATOR'))
			send_to_plc(10,1,PLCS.get('PYLON'))
			send_to_plc(11,3,PLCS.get('BOILER'))
			send_to_plc(11,3,PLCS.get('TURBINE'))
			send_to_plc(11,3,PLCS.get('GENERATOR'))
			send_to_plc(11,3,PLCS.get('PYLON'))
		else:
			return render_template('fuel.html')
	return render_template('fuel.html')

@app.route('/waterpump',methods=['GET','POST'])
@login_required
def waterpump_route():
	if request.method == 'POST':
		print(request.form.get('on_off'))
		if request.form.get('on_off') == '0':
			for i in range(1,10):
				send_to_plc(i,0,PLCS.get('WATERPUMP'))
			for i in (10,11):
				send_to_plc(i,0,PLCS.get('BOILER'))
				send_to_plc(i,0,PLCS.get('TURBINE'))
				send_to_plc(i,0,PLCS.get('GENERATOR'))
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			for i in range(1,10):
				send_to_plc(i,1,PLCS.get('WATERPUMP'))
	return render_template('waterpump.html')
	
@app.route('/boiler',methods=['GET','POST'])
@login_required
def boiler_route():
	if request.method == 'POST':
		print(request.form.get('on_off'))
		if request.form.get('on_off') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('BOILER'))
			for i in (10,11):
				send_to_plc(i,0,PLCS.get('TURBINE'))
				send_to_plc(i,0,PLCS.get('GENERATOR'))
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			for i in range(1,10):
				send_to_plc(i,1,PLCS.get('BOILER'))
	return render_template('boiler.html')

@app.route('/turbine',methods=['GET','POST'])
@login_required
def turbine_route():
	if request.method == 'POST':
		print(request.form.get('on_off'))
		if request.form.get('on_off') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('TURBINE'))
			for i in (10,11):
				send_to_plc(i,0,PLCS.get('GENERATOR'))
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			for i in range(1,10):
				send_to_plc(i,1,PLCS.get('TURBINE'))
	return render_template('turbine.html')

@app.route('/generator',methods=['GET','POST'])
@login_required
def generator_route():
	if request.method == 'POST':
		print(request.form.get('on_off'))
		if request.form.get('on_off') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('GENERATOR'))
			for i in (10,11):
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			for i in range(1,10):
				send_to_plc(i,1,PLCS.get('GENERATOR'))
	return render_template('generator.html')

@app.route('/pylon',methods=['GET','POST'])
@login_required
def pylon_route():
	if request.method == 'POST':
		print(request.form.get('on_off'))
		if request.form.get('on_off') == '0':
			for i in range(1,17):
				send_to_plc(i,0,PLCS.get('PYLON'))
		else:
			for i in range(1,10):
				send_to_plc(i,1,PLCS.get('PYLON'))
	return render_template('pylon.html')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9001)
