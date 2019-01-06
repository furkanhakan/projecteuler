#!/usr/bin/env python
# -*- coding: utf-8 -*-

#QUESTION : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

durum=True
i=3
asal=1
nonasal=[2]
while durum:
    bolensayisi = 0
    for k in nonasal:
        if i%k==0:
            nonasal.append(i)
            i += 1
            break
    for j in range(2,i):
        if i%j==0:
            bolensayisi+=1
    if bolensayisi==0:
        asal+=1
        print(asal)
    if asal==10001:
        durum=False
        print(i)
    nonasal.append(i)
    i+=1
