#!/usr/bin/env python

PLCS = {'FUEL':'192.168.26.120','WATERPUMP':'192.168.26.121','BOILER':'192.168.26.122','TURBINE':'192.168.26.123','GENERATOR':'192.168.26.124','PYLON':'192.168.26.125'}

def send_to_plc(reg_loc,reg_value,ip):
	print('++ reg_loc: %s reg_value %s ip %s' % (reg_loc, reg_value, ip))
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	modbusClient = ModbusClient(ip, port=5020)
	modbusClient.write_register(reg_loc,reg_value)
	return True

