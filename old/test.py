#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time
import re

f_log = '/var/log/or_sens_log'
f_temp = "/opt/scripts/sens-temp.py"
f_fire = "/opt/scripts/sens-fire.py"

def cln_str(raw_data):
	regexp = re.compile('[0-9A-Za-z .:]')
	str_list = regexp.findall(raw_data)
	str_out = ("".join(str_list))
	str_out += "\n"
	return str_out

process_temp = subprocess.Popen(f_temp, stdout = subprocess.PIPE)
time.sleep(18)
status = process_temp.poll()
if status == 0:
	data_temp = str(process_temp.communicate())
else:
	data_temp = "Err:2 No respronse from Temp subprocess. Kill it. PID: ",(process_temp.pid),"Status: ",(status)
	process_temp.terminate()

process_fire = subprocess.Popen(f_fire, stdout = subprocess.PIPE)
time.sleep(18)
status = process_fire.poll()
if status == 0:
        data_fire = str(process_fire.communicate())
else:
        data_fire = "Err:3 No respronse from Fire subprocess. Kill it. PID: ",(process_temp.pid),"Status: ",(status)
        process_temp.terminate()

time_st = str(time.strftime('%d-%m-%Y %H:%M:%S')) + "\n"

log_str = time_st +  cln_str(data_temp) +  cln_str(data_fire)

log_file = open(f_log, 'a')
log_file.write(log_str)
log_file.close()
