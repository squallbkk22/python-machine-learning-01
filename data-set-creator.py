#!/usr/bin/env python

import time
import os
import random

# INPUT DATA
# Gender, Age, Height, Weight

# VARIABLES

DATA_FILE = "data"

AGE_MIN = 10
AGE_MAX = 99
HEIGHT_MIN = 110
HEIGHT_MAX = 180
WEIGHT_MIN = 110
WEIGHT_MAX = 180
f = open(DATA_FILE,"w")

f.write("Gender,Age,Height,Weight\n")
for i in range(10000):
  f.write(random.choice(["M","F"]))
  f.write(",")
  f.write(str(random.randint(AGE_MIN,AGE_MAX)))
  f.write(",")
  f.write(str(random.randint(HEIGHT_MIN,HEIGHT_MAX)))
  f.write(",")
  f.write(str(random.randint(WEIGHT_MIN,WEIGHT_MAX)))
  f.write("\n")

f.close()