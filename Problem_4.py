#!/usr/bin/env python
# -*- coding: utf-8 -*-

#QUESTION : A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome=[];
for i in range(999,99,-1):
    for j in range(999,99,-1):
        sonuc = i * j
        tempsonuc = sonuc
        a = sonuc % 10
        sonuc = sonuc / 10
        b = sonuc % 10
        sonuc = sonuc / 10
        c = sonuc % 10
        sonuc = sonuc / 10
        d = sonuc % 10
        sonuc = sonuc / 10
        e = sonuc % 10
        sonuc = sonuc / 10
        f = sonuc % 10
        if f==0:
            if int(a) == int(e) and int(b) == int(d):
                palindrome.append(tempsonuc)
                break
        else:
            if int(a) == int(f) and int(b) == int(e) and int(c) == int(d):
                palindrome.append(tempsonuc)
                break
enbuyuk=palindrome[0]
for i in palindrome:
    if enbuyuk < i:
        enbuyuk = i
print(enbuyuk)
