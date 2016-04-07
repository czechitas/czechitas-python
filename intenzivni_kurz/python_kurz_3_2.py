# -*- coding: utf-8 -*-
"""
Python kurz
Podmínky a cykly

@author: Nasťa
Cvičení 3.2

Vytvořte seznam svých pěti kamarádů
Pomocí list comprehensions vytvořte z tohoto seznamu další seznam, který ke každému jménu přidá ' je super!'
Vytiskněte vytvořený seznam

"""

friends = ['Lena', 'Vero', 'Karina', 'Martina', 'Veronika']
print('friends =', friends)
friends_super = [x + ' je super!' for x in friends]
print('friends_super =', friends_super)