#!/bin/python

import os
import sys

algos = ['bfs','bc','cc','pr','sssp']
datas = {'lj':'soc-LiveJournal1','orkut':'com-orkut','urand':'big_urand','kron':'big_kron','road':'raod'}
fast = {'lj':90,'orkut':60,'urand':80,'kron':155,'road':450}
test = {'test':'/bin/ls'}

s = 10
t = 600

for algo in algos:
  for data in datas.keys():
    cmd = "./pin -ifeellucky -t ./tracer/obj-intel64/champsim_tracer.so -o ./trace_graph/" + algo + "-" + data + ".trace -s " + str(s) + "000000 -t " + str(t+1+fast[data]) + "000000 -- ./gapbs/" + algo + " -f ./gapbs/data/" + datas[data]
    if(algo == 'sssp'):
      cmd += ".wsg"
    else:
      cmd += ".sg"
    cmd += " -n 1"
    if(algo == 'bc'):
      cmd += " -i 1"
    elif(algo == 'pr'):
      cmd += " -i 1 -t1e-4"
    print(cmd)
    if(algo == 'bfs' and data == 'kron'):
      print(cmd)
    else:
      os.system(cmd)
    print("gziping ... ")
    os.system("gzip ./trace_graph/" + algo + "-" + data + ".trace")


