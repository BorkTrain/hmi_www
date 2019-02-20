#!/usr/bin/env python

PLCS = {'FUEL':'192.168.26.120','WATERPUMP':'192.168.26.121','BOILER':'192.168.26.122','TURBINE':'192.168.26.123','GENERATOR':'192.168.26.124','PYLON':'192.168.26.125'}

def send_to_plc(reg_loc,reg_value,ip):
	print('++ reg_loc: %s reg_value %s ip %s' % (reg_loc, reg_value, ip))
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	modbusClient = ModbusClient(ip, port=5020)
	modbusClient.write_register(reg_loc,reg_value)
	return True

def emergency_shutoff():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('FUEL'))
		send_to_plc(i,0,PLCS.get('WATERPUMP'))
		send_to_plc(i,0,PLCS.get('BOILER'))
		send_to_plc(i,0,PLCS.get('TURBINE'))
		send_to_plc(i,0,PLCS.get('GENERATOR'))
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def fuel_rate_0():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('FUEL'))
	for i in (10,11):
		send_to_plc(i,0,PLCS.get('WATERPUMP'))
		send_to_plc(i,0,PLCS.get('BOILER'))
		send_to_plc(i,0,PLCS.get('TURBINE'))
		send_to_plc(i,0,PLCS.get('GENERATOR'))
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True

def fuel_rate_1():
	for i in range(1,17):
		send_to_plc(i,1,PLCS.get('FUEL'))
	send_to_plc(10,1,PLCS.get('WATERPUMP'))
	for i in (10,11):
		send_to_plc(i,1,PLCS.get('BOILER'))
		send_to_plc(i,1,PLCS.get('TURBINE'))
		send_to_plc(i,1,PLCS.get('GENERATOR'))
		send_to_plc(i,1,PLCS.get('PYLON'))
	return True

def fuel_rate_2():
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
	return True

def fuel_rate_3():
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
	return True 

def waterpump_off():
	for i in range(1,10):
		send_to_plc(i,0,PLCS.get('WATERPUMP'))
	for i in (10,11):
		send_to_plc(i,0,PLCS.get('BOILER'))
		send_to_plc(i,0,PLCS.get('TURBINE'))
		send_to_plc(i,0,PLCS.get('GENERATOR'))
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def waterpump_on():
	for i in range(1,10):
		send_to_plc(i,1,PLCS.get('WATERPUMP'))
	return True 

def boiler_off():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('BOILER'))
	for i in (10,11):
		send_to_plc(i,0,PLCS.get('TURBINE'))
		send_to_plc(i,0,PLCS.get('GENERATOR'))
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def boiler_on():
	for i in range(1,10):
		send_to_plc(i,1,PLCS.get('BOILER'))
	return True 

def turbine_off():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('TURBINE'))
	for i in (10,11):
		send_to_plc(i,0,PLCS.get('GENERATOR'))
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def turbine_on():
	for i in range(1,10):
		send_to_plc(i,1,PLCS.get('TURBINE'))
	return True 

def generator_off():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('GENERATOR'))
	for i in (10,11):
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def generator_on():
	for i in range(1,10):
		send_to_plc(i,1,PLCS.get('GENERATOR'))
	return True 

def pylon_off():
	for i in range(1,17):
		send_to_plc(i,0,PLCS.get('PYLON'))
	return True 

def pylon_on():
	for i in range(1,10):
		send_to_plc(i,1,PLCS.get('PYLON'))
	return True 
