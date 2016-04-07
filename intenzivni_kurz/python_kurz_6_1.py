# -*- coding: utf-8 -*-
"""
Intenzivní kurz Python
Chyby a výjimky 

@author: Nasťa
Cvíčení 6.1

Zeptejte se uživatele na jméno a vyvolejte výjimku s odpovídající chybovou hláškou, když
Jméno obsahuje číslice
Jméno obsahuje mezery
Jméno nezačíná velkým písmenem
"""
name = input('Napiš svoje jméno, prosím: ')
if any(i.isdigit() for i in name):
    raise Exception('Nepiš jmeno s číslicemi, prosím')
if ' ' in name:
    raise Exception('Nepiš jméno s mezerami, prosím')
if not name[0].isupper():
    raise Exception('Ále no tak, jméno se píše s velkým písmenem')
