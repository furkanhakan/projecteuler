#!/usr/bin/env python
# -*- coding: utf-8 -*-

#QUESTION : The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?


def PrimeList(ustsinir):
    prime=[True for i in range(ustsinir + 1)]
    p=2

    while p * p <= ustsinir:
        if prime[p] == True:
            for i in range(p * 2, ustsinir + 1, p):
                prime[i] = False
        p += 1
    return prime

prime = PrimeList(13195)

for p in range(2,13195):
        if prime[p]:
            if 13195%p==0:
                print(p)
