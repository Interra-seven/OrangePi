#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import smbus

DEV_ADDR = 0x48
adc_channels = {
	'AIN0':0x00,
	'AIN1':0x01,
	'AIN2':0x10,
	'AIN3':0x11,
}

bus = smbus.SMBus(0)

for channel in adc_channels:
	bus.write_byte(DEV_ADDR, adc_channels[channel])
	bus.read_byte(DEV_ADDR)
	bus.read_byte(DEV_ADDR)
	value = bus.read_byte(DEV_ADDR)
	print 	'Channel ' + channel + ': ' +  str(value) + ' Vin = ' + str(round(5*(float(value)/255),2)) + 'v'
	time.sleep(1)

