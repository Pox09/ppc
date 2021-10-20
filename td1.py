#!/usr/bin/env python3 
import time
from multiprocessing import Process
import sys as sys
import os

if len(sys.argv)<2:
	indice=0

elif int(sys.argv[1])<0:
	print("Vous avez donné une valeur négative")
	
else:
	indice=int(sys.argv[1])

def fibo(n):
	
	if n==0:
		return(0)
	elif n==1:
		return(1)
	else:
		a=0
		b=1
		for i in range(1,n):
			c=a+b
			a=b
			b=c
		return(c)

def fibo2(n):
	print("Id parent",os.getppid())
	print("Id fils",os.getpid())
	for i in range(n+1):
		print(fibo(i))
	time.sleep(10)

if __name__ == "__main__":
    	p = Process(target=fibo2, args=(indice,))
    	p.start()
    	p.join()
		
		
		
