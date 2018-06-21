#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time

scr_f = "/opt/scripts/subproc.py"

prc = subprocess.Popen(scr_f, stdout = subprocess.PIPE)
time.sleep(3)

data = prc.communicate()

print(data)

