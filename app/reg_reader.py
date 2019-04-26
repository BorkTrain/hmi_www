#!/usr/bin/env python
import time

PLCS = {'FUEL':'192.168.26.120','WATERPUMP':'192.168.26.121','BOILER':'192.168.26.122','TURBINE':'192.168.26.123','GENERATOR':'192.168.26.124','PYLON':'192.168.26.125'}

def send_to_plc(reg_loc,reg_value,ip):
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	modbusClient = ModbusClient(ip, port=5020)
	modbusClient.write_register(reg_loc,reg_value)
	return True

def read_from_plc(reg_start,reg_stop,ip):
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	modbusClient = ModbusClient(ip, port=5020)
	res = modbusClient.read_holding_registers(reg_start,reg_stop).registers
	return res

def get_plc_stat():
	# res = {'FUEL':'off','WATERPUMP':'off','BOILER':'off','TURBINE':'off','GENERATOR':'off','PYLON':'off'}
	res = {}
	for plc_name in PLCS:
		plc_ip = PLCS.get(plc_name)
		plc_vals = read_from_plc(1,16,plc_ip)
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
	plc_sum = sum(plc_vals)
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
	plc_sum = sum(plc_vals)
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_boiler_stat(plc_vals):
	plc_sum = sum(plc_vals)
	if plc_sum == 16:
		rate = 'OPEN'
	else:
		rate = 'CLOSED'
	return rate

def get_turbine_stat(plc_vals):
	plc_sum = sum(plc_vals)
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_generator_stat(plc_vals):
	plc_sum = sum(plc_vals)
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate

def get_pylon_stat(plc_vals):
	plc_sum = sum(plc_vals)
	if plc_sum == 16:
		rate = 'ON'
	else:
		rate = 'OFF'
	return rate





'''
def prod_on():
	x = get_plc_stat()
	y = x.get('WATERPUMP')
	z = x.get('FUEL')
	if y.__contains__('on') and z != 'fuel_off':
		send_to_plc(10,1,PLCS.get('WATERPUMP'))
		send_to_plc(10,1,PLCS.get('BOILER'))
		send_to_plc(10,1,PLCS.get('TURBINE'))
		send_to_plc(10,1,PLCS.get('GENERATOR'))
		send_to_plc(10,1,PLCS.get('PYLON'))
	else:
		pass
	return True 

def plc_rate():
	x = get_plc_stat()
	y = x.get('WATERPUMP')
	z = x.get('FUEL')
	if y.__contains__('on') and z == 'fuel_low':
		send_to_plc(11,1,PLCS.get('BOILER'))
		send_to_plc(11,1,PLCS.get('TURBINE'))
		send_to_plc(11,1,PLCS.get('GENERATOR'))
		send_to_plc(11,1,PLCS.get('PYLON'))
	elif y.__contains__('on') and z == 'fuel_norm':
		send_to_plc(11,2,PLCS.get('BOILER'))
		send_to_plc(11,2,PLCS.get('TURBINE'))
		send_to_plc(11,2,PLCS.get('GENERATOR'))
		send_to_plc(11,2,PLCS.get('PYLON'))
	elif y.__contains__('on') and z == 'fuel_max':
		send_to_plc(11,3,PLCS.get('BOILER'))
		send_to_plc(11,3,PLCS.get('TURBINE'))
		send_to_plc(11,3,PLCS.get('GENERATOR'))
		send_to_plc(11,3,PLCS.get('PYLON'))
	else:
		pass
	return True
'''
