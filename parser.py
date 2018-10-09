#!/bin/python
import os

app = ['']
ap_test = ['astar_23B','lbm_94B','mcf_46B','omnetpp_17B', 'xalancbmk_99B', 'gcc_13B', 'libquantum_964B', 'milc_360B', 'soplex_66B', 'zeusmp_100B']
case = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','optAmpm','bestoffset']
case_test = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp']
n_warm = 10 #M
n_sim = 10
result = "result" + str(n_warm) + "M" + str(n_sim) + "M"

print "App, Prefetcher, IPC, Accuracy, MPKI"
for ap in ap_test:
  print ap + ', ',
  first = True
  for sim in case_test:
    if(first == False):
      print ' , ', 
    else:
      first = False
    print sim + ', ',
    f = open('./' + result + '/' + ap + '-perceptron-no-' + sim + '-lru-1core.txt', 'r')
    for line in f:
      if(line.find("Prediction Accuracy:") != -1):
        print line.split()[5] + ', ',
        print line.split()[7]
        break
      if(line.find("Finished") != -1):
        print line.split()[9] + ', ',
    f.close()
