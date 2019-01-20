#!/usr/bin/env python
# -*- coding: utf-8 -*-

#QUESTION : The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def PrimeList(ustsinir):
    sonuc = 0
    prime=[True for i in range(ustsinir + 1)]
    p=2

    while p * p <= ustsinir:
        if prime[p] == True:
            for i in range(p * 2, ustsinir + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, ustsinir + 1):
        if prime[p]:
            sonuc += p
    print(sonuc)
PrimeList(2000000)
