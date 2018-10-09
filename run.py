#!/bin/python

import os

app = ['']
ap_test = ['astar_23B','lbm_94B','mcf_46B','omnetpp_17B', 'xalancbmk_99B', 'gcc_13B', 'libquantum_964B', 'milc_360B', 'soplex_66B', 'zeusmp_100B']
case = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','optAmpm','bestoffset']
case_test = ['hybridVldp']
n_warm = 10 #1000 #M
n_sim = 10 #500
result = "result" + str(n_warm) + "M" + str(n_sim) + "M"

os.system("mkdir -p " + result)
for ap in ap_test:
  for sim in case_test:
    cmd = "./shrun_champsim.sh perceptron-no-" + sim + "-lru-1core " + str(n_warm) + " " + str(n_sim) + " " + ap + " " + result + " & "
    print(cmd)
    os.system(cmd)
