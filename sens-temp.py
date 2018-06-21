#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

sens_path = ['/sys/bus/w1/devices/28-000009f951c7/w1_slave',
             '/sys/bus/w1/devices/28-000009f85fb8/w1_slave',
             '/sys/bus/w1/devices/28-000009f7c200/w1_slave',
             '/sys/bus/w1/devices/28-000009f7703b/w1_slave',
             '/sys/bus/w1/devices/28-000009f8dff6/w1_slave',
             '/sys/bus/w1/devices/28-000009f7be3c/w1_slave',
             '/sys/bus/w1/devices/28-000009f7d87c/w1_slave',
             '/sys/bus/w1/devices/28-000009f77919/w1_slave',
             '/sys/bus/w1/devices/28-000009f95ba0/w1_slave']

sens_temp = []

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

for i in range (len(sens_path)):
        sens_temp.append('Sens' + str(i) + ': ' + str(ds18b20(sens_path[i])))

print (sens_temp)

