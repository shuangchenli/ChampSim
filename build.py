#!/bin/python
import os

case = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','optAmpm','bestoffset']
test = ['optAmpm','bestoffset']

for key in test:
  cmd = "./shbuild_champsim.sh perceptron no " + key + " lru 1"
  print(cmd)
  os.system(cmd)
