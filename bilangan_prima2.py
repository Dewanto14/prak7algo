# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:07:57 2023

@author: Huawei
"""


def angka_prima(x):
    if((x == 0) or (x == 1)):
        return False
    for i in range(2,(x//2)):
        if ((x % i) == 0):
            return False
    return True

def Main():
    x = int(input('Input satu angka bulat: '))
    if angka_prima(x):
        print(x,'adalah angka prima')
    else:
      print(x,'bukan angka prima')
      
Main()