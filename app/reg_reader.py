#!/usr/bin/env python
import time
import os
import subprocess

PLCS = {'FUEL':'192.168.26.120','WATERPUMP':'192.168.26.121','BOILER':'192.168.26.122','TURBINE':'192.168.26.123','GENERATOR':'192.168.26.124','PYLON':'192.168.26.125'}

def send_to_plc(ip,start_reg,value,count):
	value_space = str(value) + ' '
	reg_val = str(value_space) * int(count)
	reg_write = "modbus write "+ ip + ' ' + start_reg + ' ' + reg_val
	os.system(reg_write)

def read_from_plc(ip,start_reg,count):
	reg_read = "modbus read "+ ip + ' ' + start_reg + ' ' + str(count)
	os.system(reg_read)

def read_16(plc_ip):
	vals = subprocess.check_output(['modbus', 'read', plc_ip, '%MW1', '16'])
	return vals

def plc_reg_sum(plc_ip):
	registers = subprocess.check_output(['modbus', 'read', plc_ip, '%MW1', '16'], shell=True)
	vals = ([int(y[-1].strip()) for y in registers.split('\n') if y.strip() != ''])
	reg_sum = sum(vals)
	return reg_sum

def get_plc_stat():
	# res = {'FUEL':'off','WATERPUMP':'off','BOILER':'off','TURBINE':'off','GENERATOR':'off','PYLON':'off'}
	res = {}
	for plc_name in PLCS:
		plc_ip = PLCS.get(plc_name)
		plc_vals = read_16(plc_ip)
		if plc_name is 'FUEL':
			res[plc_name] = get_fuel_stat(plc_vals)
		elif plc_name is 'WATERPUMP':
			res[plc_name] = get_water_stat(plc_vals)
		elif plc_name is 'BOILER':
			res[plc_name] = get_boiler_stat(plc_vals)
		elif plc_name is 'TURBINE':
			res[plc_name] = get_turbine_stat(plc_vals)
		elif plc_name is 'GENERATOR':
			res[plc_name] = get_generator_stat(plc_vals)
		elif plc_name is 'PYLON':
			res[plc_name] = get_pylon_stat(plc_vals)
	return res

def get_fuel_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 64:
		rate = 'MAX'
	elif plc_sum == 32:
		rate = 'Normal'
	elif plc_sum == 16:
		rate = 'Low'
	else:
		rate = 'OFF'
	return rate

def get_water_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_boiler_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 16:
		rate = 'OPEN'
	else:
		rate = 'CLOSED'
	return rate

def get_turbine_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_generator_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_pylon_stat(plc_vals):
	plc_sum = sum([int(y[-1].strip()) for y in plc_vals.split('\n') if y.strip() != ''])
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate
