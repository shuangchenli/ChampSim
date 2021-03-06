#!/bin/python

import os

case = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','optAmpm','bestoffset']
case_test = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','bestoffset']
batch = 32


ap_test = ['astar_23B','lbm_94B','mcf_46B','omnetpp_17B', 'xalancbmk_99B', 'gcc_13B', 'libquantum_964B', 'milc_360B', 'soplex_66B', 'zeusmp_100B']
n_warm = 10 #1000 #M
n_sim = 10 #500
def run_bench():
  count = 0
  cmd = ''
  result = "result" + str(n_warm) + "M" + str(n_sim) + "M"
  os.system("mkdir -p " + result)
  for ap in ap_test:
    for sim in case_test:
      cmd += "./shrun_champsim.sh perceptron-no-" + sim + "-lru-1core " + str(n_warm) + " " + str(n_sim) + " " + ap + " " + result + " ./trace"
      if(count == batch-1):
        count = 0
        print(cmd)
        os.system(cmd)
        cmd = ''
      else:
        cmd += ' & '
        count += 1
  print(cmd)
  os.system(cmd)

graph_algos = ['bfs','bc','cc','pr','sssp']
graph_data = {'lj':'soc-LiveJournal1','orkut':'com-orkut.ungraph','urand':'big_urand','kron':'big_kron','road':'road'}
graph_warm = {'lj':90,'orkut':60,'urand':80,'kron':155,'road':450}
graph_sim = 500
def run_graph():
  count = 0
  cmd = ''
  result = "result_graph"
  os.system("mkdir -p " + result)
  for algo in graph_algos:
    for data in graph_data.keys():
      for sim in case_test:
        ap = algo + '-' + data
        #cmd += "./shrun_champsim.sh perceptron-no-" + sim + "-lru-1core " + str(graph_warm[data]) + " " + str(graph_sim) + " " + ap + " " + result + " ./trace_graph"
        cmd += "./bin/perceptron-no-" + sim + "-lru-1core" 
        cmd += " -warmup_instructions " + str(graph_warm[data]) + "000000"
        cmd += " -simulation_instructions " + str(graph_sim) + "000000"
        cmd += " -traces ./trace_graph/" + ap + ".trace.gz"
        cmd += " > \"./" + result + "/" + ap + "-" + "perceptron-no-" + sim + "-lru-1core.txt\""
        if(count == batch - 1):
          count = 0
          print(cmd)
          os.system(cmd)
          cmd = ''
        else:
          cmd += ' & '
          count += 1
  #cmd += 'ls'
  print(cmd)
  os.system(cmd)

def main():
  run_graph()

if __name__ == "__main__":
  main()
