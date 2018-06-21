#!/usr/bin/env python
# -*- coding: utf-8 -*-

#("['Sens0: 12.312', 'Sens1: 8.0', 'Sens2: 7.875', 'Sens3: 21.562', 'Sens4: 19.062', 'Sens5: 15.875', 'Sens6: 15.5', 'Sens7: 21.875']\n", None) ('Fire sensor status: 0, Vin: 3.59, control: 0\n', None)

import re

a = ("['Sens0: 12.312', 'Sens1: 8.0', 'Sens2: 7.875', 'Sens3: 21.562', 'Sens4: 19.062', 'Sens5: 15.875', 'Sens6: 15.5', 'Sens7: 21.875']\n", None)
b = ('Fire sensor status: 0, Vin: 3.59, control: 0\n', None)

regexp = re.compile('[0-9A-Za-z .:]')

str = regexp.findall(str(a))


#def clean_out(raw_data):
#	cln_str = ""
#	string = str(raw_data)
#	for i in range(len(string)):
#		if string[i] == [0-9A-Za-z .:]:
#		if string[i] != "'" or string[i] != "(" or string[i] != "," or  string[i] != ")":
#			cln_str += string[i]
#	return cln_str

print("".join(str))



