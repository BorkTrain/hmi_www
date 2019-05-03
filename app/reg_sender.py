#!/usr/bin/env python

PLCS = {'FUEL':'192.168.26.120','WATERPUMP':'192.168.26.121','BOILER':'192.168.26.122','TURBINE':'192.168.26.123','GENERATOR':'192.168.26.124','PYLON':'192.168.26.125'}

def send_to_plc(ip,start_reg,value,count):
	value_space = str(value) + ' '
	reg_val = str(value_space) * int(count)
	reg_write = "modbus write "+ ip + ' ' + start_reg + ' ' + reg_val
	os.system(reg_write)
	return True

def emergency_shutoff():
	send_to_plc(PLCS.get('FUEL'),'%MW1',0,16)
	send_to_plc(PLCS.get('WATERPUMP'),'%MW1',0,16)
	send_to_plc(PLCS.get('BOILER'),'%MW1',0,16)
	send_to_plc(PLCS.get('TURBINE'),'%MW1',0,16)
	send_to_plc(PLCS.get('GENERATOR'),'%MW1',0,16)
	send_to_plc(PLCS.get('PYLON'),'%MW1',0,16)
	return True 

def fuel_rate_0():
	send_to_plc(PLCS.get('FUEL'),'%MW1',0,16)

def fuel_rate_1():
	send_to_plc(PLCS.get('FUEL'),'%MW1',1,16)

def fuel_rate_2():
	send_to_plc(PLCS.get('FUEL'),'%MW1',2,16)

def fuel_rate_3():
	send_to_plc(PLCS.get('FUEL'),'%MW1',3,16) 

def waterpump_off():
	send_to_plc(PLCS.get('WATERPUMP'),'%MW1',0,16)

def waterpump_on():
	send_to_plc(PLCS.get('WATERPUMP'),'%MW1',1,16) 

def boiler_off():
	send_to_plc(PLCS.get('BOILER'),'%MW1',0,16) 

def boiler_on():
	send_to_plc(PLCS.get('BOILER'),'%MW1',1,16) 

def turbine_off():
	send_to_plc(PLCS.get('TURBINE'),'%MW1',0,16) 

def turbine_on():
	send_to_plc(PLCS.get('TURBINE'),'%MW1',1,16)  

def generator_off():
	send_to_plc(PLCS.get('GENERATOR'),'%MW1',0,16)  

def generator_on():
	send_to_plc(PLCS.get('GENERATOR'),'%MW1',1,16) 

def pylon_off():
	send_to_plc(PLCS.get('PYLON'),'%MW1',0,16)  

def pylon_on():
	send_to_plc(PLCS.get('PYLON'),'%MW1',1,16)   
