# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:36:55 2023

@author: Mostafa
"""

from json import load,dump
from tqdm import tqdm



n=1000000







try:
    open("primes.json","r")
except FileNotFoundError:
    dump([2,3],open("primes.json","w+"))

primes=load(open("primes.json","r"))

new_primes=primes.copy()



def isprime(x,primes):
    for prime in primes:
        if prime>x**0.5:
            return True
        div=x/prime
        if div==int(div):
            return False

x=primes[-1]+2

for _ in tqdm(range(n),total=n,leave=True,position=0):
    
    if isprime(x,new_primes):
        new_primes.append(x)
    
    x+=2

# print(new_primes)

dump(new_primes,open("primes.json","w+"))
