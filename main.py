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
        str_out += " "
        return str_out

def run_prc(f_name,s_time):
	prc_tmp = subprocess.Popen(f_name, stdout = subprocess.PIPE)
	time.sleep(int(s_time))
	stat = prc_tmp.poll()
	if stat == 0:
		def_data = str(prc_tmp.communicate())
	else:
		def_data = "There is no response from subprocess: ",(f_name)," Kill it. PID:",(prc_tmp.pid),". Status: ",(stat)
		prc_tmp.terminate()
	return def_data

temp_data = str(run_prc(f_temp,18))
fire_data = str(run_prc(f_fire,18))

log_str = str(time.strftime('%d-%m-%Y %H:%M:%S')) + " " + cln_str(temp_data) + " " + cln_str(fire_data) + "\n"

log_file = open(f_log, 'a')
log_file.write(log_str)
log_file.close()

