#!/usr/bin/env python

from sklearn import linear_model
import numpy as np
import os

# VARIABLES

DATA_FILE = "data"

f = open(DATA_FILE,"r")

data = []

i = 0
for line in f:
  #print i, line.rstrip(), type(line)
  list = line.rstrip().split(',')
  data.append(list)
  i += 1

predict = "Height"

print(len(data))
print(data([predict]))