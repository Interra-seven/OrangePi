#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

top_dir = '/sys/bus/w1/devices/'
#log_f = '/var/log/orangepi/sens.log'
sens_amount = len(glob.glob(top_dir + '[0-9][0-9]-*'))
sens_list = glob.glob(top_dir + '[0-9][0-9]-*')
sens_raw_temp = []
sens_temp = []

print "Amount of sensors: ", (sens_amount)

for i in range(sens_amount):
	sens_list_full  = str(sens_list[i] + '/w1_slave')
	print "Sensor",i,"Full path: ",(sens_list_full)
	dev_file = open(sens_list_full, 'r')
	raw_temp = dev_file.readlines()
	dev_file.close()
	sens_raw_temp.append(raw_temp)
	time.sleep(0.1)

for i in range(sens_amount):
	raw_str = str(sens_raw_temp[i])
	char_idx = raw_str.find('t=')
	if char_idx != -1:
		temp_str_value =raw_str[char_idx+2:-4]
		temp_value = float(temp_str_value)/1000
		sens_temp.append(temp_value)

def wr_log():
	log_return = str((time.strftime('%d-%m-%Y %H:%M:%S'))) + " " 
	for i in range(sens_amount):
		sens_list_item = str(sens_temp[i])
		some_ = "Sensor" + str(i) + ": " + sens_list_item +"°C "
		log_return += some_
	log_return +=  "\n"
	return log_return

print wr_log()

#log_file = open(log_f, 'a')
#log_file.write(wr_log())
#log_file.close()

