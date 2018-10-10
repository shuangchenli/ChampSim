#!/bin/python
import os

case = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','optAmpm','bestoffset']
case_test = ['no','spp_dev','next_line','kpcp','vldp','slimAmpm','hybridVldp','bestoffset']

ap_test = ['astar_23B','lbm_94B','mcf_46B','omnetpp_17B', 'xalancbmk_99B', 'gcc_13B', 'libquantum_964B', 'milc_360B', 'soplex_66B', 'zeusmp_100B']
n_warm = 10 #M
n_sim = 10
def parser_benchmark():
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

graph_algos = ['bfs','bc','cc','pr','sssp']
graph_data = {'lj':'soc-LiveJournal1','orkut':'com-orkut.ungraph','urand':'big_urand','kron':'big_kron','road':'road'}
graph_warm = {'lj':90,'orkut':60,'urand':80,'kron':155,'road':450}
graph_sim = 5
def parser_graph():
  result = "result_graph"
  print "Algo-Data, Prefetcher, IPC, Accuracy, MPKI"
  for algo in graph_algos:
    for data in graph_data.keys():
      print algo + '-' + data + ', ',
      first = True
      for sim in case_test:
        if(first == False):
          print ' , ', 
        else:
          first = False
        print sim + ', ',
        f = open('./' + result + '/' + algo + '-' + data  + '-perceptron-no-' + sim + '-lru-1core.txt', 'r')
        for line in f:
          if(line.find("Prediction Accuracy:") != -1):
            print line.split()[5] + ', ',
            print line.split()[7]
            break
          if(line.find("Finished") != -1):
            print line.split()[9] + ', ',
        f.close()

def main():
  parser_graph()
  #parser_benchmark()

if __name__ == "__main__":
  main()
