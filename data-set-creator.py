#!/usr/bin/env python

import time
import os
import random

# VARIABLES

DATA_FILE = "data"



X_MIN = 10000
X_MAX = 19999
Y_MIN = 20000
Y_MAX = 29999

for i in range(10):
  print random.randint(1,10)

f = open(DATA_FILE,"w")
f.write("22")
f.write("5678")

f.close()