#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import smbus

bus = smbus.SMBus(0)

bus.write_byte(0x48,0x00)
bus.read_byte(0x48)
bus.read_byte(0x48)
value = bus.read_byte(0x48)
print   'Channel AIN 0: ' +  str(value) + ' Vin = ' + str(round(5*(float(value)/255),2)) + 'v'

