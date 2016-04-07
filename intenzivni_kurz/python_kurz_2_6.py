# -*- coding: utf-8 -*-
"""
Python kurz
Datové typy

@author: Nasťa
Cvičení 2.6

Opravte slovník a vymažte chybný klíč
d = {'čekitas':'Organizace vzdělávající ženy v oblasti IT'}
"""

d = {'čekitas':'Organizace vzdělávající ženy v oblasti IT'}
print('d=', d)
d['czechitas'] = d['čekitas']
del d['čekitas']
print('d=', d)