#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import time

bus = smbus.SMBus(0)
gpio_path = '/sys/class/gpio/'
gpio_pin = '20'

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

def adc():
	bus.write_byte(0x48,0x00)
	bus.read_byte(0x48)
	bus.read_byte(0x48)
	adc_raw_data = bus.read_byte(0x48)
	adc_data = round(5*(float(adc_raw_data)/255),2)
	return adc_data

adc_data = adc()
sta = 0

if adc_data >= 3.2:
	state = 0
elif adc_data < 3.2 and adc_data > 1.8:
	sta = adc_data
	relay('unexport')
	relay('export')
	relay('out')
	relay('0')
	time.sleep(6)
	relay('1')
	relay('unexport')
	time.sleep(6)
	adc_data = adc()
	if adc_data >= 3.2:
		state = 10
	elif adc_data < 3.2 and adc_data >= 2.7:
		state = 11
	elif adc_data < 2.7 and adc_data >= 2.35:
		state = 12
	elif adc_data <2.35 and adc_data >= 2.05:
		state = 13
	else:
		state = 199
else:
	state = 99

print "Fire sensor status: " + str(state) + ", Vin: " + str(adc_data) + ", control: " + str(sta)

