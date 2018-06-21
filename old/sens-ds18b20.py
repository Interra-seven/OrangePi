#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import time
import smbus

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

log_f = '/var/log/or_sens_log'
bus = smbus.SMBus(0)
sens_raw_temp_list = []
sens_name_list = ['/sys/bus/w1/devices/28-000009f951c7/w1_slave',
		  '/sys/bus/w1/devices/28-000009f85fb8/w1_slave',
		  '/sys/bus/w1/devices/28-000009f7c200/w1_slave',
		  '/sys/bus/w1/devices/28-000009f7703b/w1_slave',
		  '/sys/bus/w1/devices/28-000009f8dff6/w1_slave',
		  '/sys/bus/w1/devices/28-000009f7be3c/w1_slave',
		  '/sys/bus/w1/devices/28-000009f7d87c/w1_slave',
		  '/sys/bus/w1/devices/28-000009f77919/w1_slave'
		 ]

sens_raw_temp_list.append(time.strftime('%d-%m-%Y %H:%M:%S'))

for i in range (len(sens_name_list)):
	device_file = open(sens_name_list[i], 'r')
	raw_temp = str(device_file.readlines())
	device_file.close()
	char_idx = raw_temp.find('t=')
	if char_idx != -1:
		temp = float(raw_temp[char_idx+2:-4])/1000
	sens_raw_temp_list.append('Sens' + str(i) + ': ' + str(temp))
	time.sleep(0.1)

print (sens_raw_temp_list)


bus.write_byte(0x48,0x00)
bus.read_byte(0x48)
bus.read_byte(0x48)
value = bus.read_byte(0x48)
log_string_ip212 = str('Channel AIN 0: ' +  str(value) + ' Vin = ' + str(round(5*(float(value)/255),2)) + 'v ' )
print (log_string_ip212)

log_file = open(log_f, 'a')
#log_file.write(log_string_ip212)
log_file.write(str(sens_raw_temp_list) + '\n')
log_file.write(log_string_ip212)
log_file.close()
