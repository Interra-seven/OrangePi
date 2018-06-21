#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

gpio_path = '/sys/class/gpio/'
gpio_pin = '20'

def gpio(arg):
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

gpio('export')
gpio('out')
gpio('0')
gpio('unexport')

subprocess.call('gpio readall', shell=True)


