# -*- coding: utf-8 -*-
"""
Python kurz
Podmínky a cykly

@author: Nasťa
Cvičení 3.3

Máte k dispozici mezinárodní hláskovací abecedu
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Napište kód, který zadané slovo vyhláskuje

"""

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

name = input('Please type your name: ')
name_list = []
for letter in name:
    if letter.lower() in d.keys():
        name_list.append(d[letter.lower()])
    else:
        name_list.append('no such letter')
print(name, '=', ", ".join(name_list))

