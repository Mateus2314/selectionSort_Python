#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def selectionSort(alist):
    for index in range(0, len(alist)):
        ismall = index
        for i in range(index,len(alist)):
            if alist[ismall] > alist[i]:
                ismall = i
        alist[index], alist[ismall] = alist[ismall], alist[index]

filename=input('Enter file path:')
file = open(filename, 'r')


results = [int(i) for i in file]

selectionSort(results)

for i in range(len(results)):
    
    resultado = open('resultado.txt', 'a')
    resultado.write(str(results[i])+ '\n') 
    resultado.close()


    



    
