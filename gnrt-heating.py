#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import smbus
import os.path

gpio_path = '/sys/class/gpio/'
gpio_pin = '10'
f = open('/var/log/or_sens_log','r')
last_str = f.readlines()[-1]

def relay(arg):
        if arg == 'export':
                tmpval = gpio_path + arg
                pin_file = open(tmpval, 'w')
                pin_file.write(gpio_pin)
                pin_file.close()
        elif arg == 'unexport':
                tmpval = gpio_path + arg
                pin_file = open(tmpval, 'w')
                pin_file.write(gpio_pin)
                pin_file.close()
        elif arg == 'in' or arg == 'out':
                tmpval = gpio_path + 'gpio' + gpio_pin + '/direction'
                pin_file = open(tmpval, 'w')
                pin_file.write(arg)
                pin_file.close()
        elif arg == '0' or arg == '1':
                tmpval = gpio_path + 'gpio' + gpio_pin + '/value'
                pin_file = open(tmpval, 'w')
                pin_file.write(arg)
                pin_file.close()
        else:
                tmpval = str("Wrong argument for function, it must be: export, unexport, in, out, 1,0")
        return tmpval

def sens(raw_str):
	list = []
	i = 7
	for i in range(7,9):
		string = 'Sens' + str(i) + ': ([0-9.]+)'
		regexp = re.compile(string)
		search = regexp.search(raw_str)
		list.append(search.group(1))
	return list

#street
sens10 = float(sens(last_str)[0])
#generator
sens11 = float(sens(last_str)[1])

print_str ="Temp's street/generator are: " + str(sens10) + " C°/ " + str(sens11) + " C°. The heating is going "

if os.path.exists('/sys/class/gpio/gpio10') == True:
	relay('unexport')

relay('export')
relay('out')

if sens10 <= 5 and sens11 <= 45:
	relay('0')
	print print_str + "ON. State 1"
elif sens10 <= 5 and sens11 > 45:
	relay('1')
	print print_str + "OFF. State 2"
elif sens10 > 5 and sens10 <= 10 and sens11 <= 25:
        relay('0')
	print print_str + "ON. State 3"
elif sens10 > 5 and sens10 <= 10 and sens11 > 25:
        relay('1')
	print print_str + "OFF. State 3"
else:
        relay('1')
	print print_str + "OFF. State 0"

relay('unexport')
