# -*- coding: utf-8 -*-
"""
Python kurz
Podmínky a cykly

@author: Nasťa
Cvičení 3.3

Vytvořte nákupní seznam
Pomocí příkazu for a break napište kód, který se zeptá na novou položku, 
projde seznam a když položku najde, vypíše ji a nehledá dál


"""

shopping_list = ['mléko', 'rum', 'rohlíky', 'salám', 'pomeranče', 'pivo']
print('shopping_list =', shopping_list)
new_item = input('Co mám ještě koupit? ')
for item in shopping_list:
    if new_item.lower() == item:
        print('Už to mám na seznamu!')
        break
    else:
        print('Mám na seznamu ' + item)