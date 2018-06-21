#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#28-000009f77919 - street, 28-000009f95ba0 - generator
sns_pth = ['/sys/bus/w1/devices/28-000009f77919/w1_slave',
	   '/sys/bus/w1/devices/28-000009f95ba0/w1_slave']
sns_tmp = []

def ds18b20(dev_file_path):
        dev_file = open(dev_file_path, 'r')
        raw = str(dev_file.readlines())
        dev_file.close()
        idx = raw.find('t=')
        if idx != -1:
                temp = float(raw[idx+2:-4])/1000
                time.sleep(0.1)
        else:
                temp = str('Err №1')
        return temp

for i in range (len(sns_pth)):
	tmp = ds18b20(sns_pth[i])
        sns_tmp.append('Sens' + str(i+10) + ': ' + str(tmp))

print (sns_tmp)
