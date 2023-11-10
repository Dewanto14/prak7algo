# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:05:07 2023

@author: Huawei
"""

def ordinal_number(ordinal):
    while True:
        if ordinal % 10 == 1:
            return 'st'
        elif ordinal % 10 == 2:
            return 'nd'
        elif ordinal % 10 == 3:
            return 'rd'
        else:
            return 'th'
        
bosan = False
while not bosan:
    print("Masukkan 0 untuk menghentikan program")
    nilai = int(input("masukkan angka : "))
    hasil = ordinal_number(nilai)
    print(f"{nilai} '{hasil}'")
    if nilai == 0:
        bosan = True