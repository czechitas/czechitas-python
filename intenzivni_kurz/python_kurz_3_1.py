# -*- coding: utf-8 -*-
"""
Python kurz
Podmínky a cykly

@author: Nasťa
Cvičení 3.1

Máte k dispozici seznam 20 nejčastějších jmen v ČR
names_list = ['Jiří', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomáš', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdeněk', 'František', 'Václav', 'Michal', 'Lenka', 'Kateřina']
Napište kód, který se Vás zeptá na jméno a zkontroluje, zda je v seznamu a vypíše vtipnou hlášku
"""

names_list = ['Jiří', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomáš', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdeněk', 'František', 'Václav', 'Michal', 'Lenka', 'Kateřina']
print('Nejčastější jména', ", ".join(names_list))
name = input('Jak se jménuješ? ')
if name in names_list:
    print(name, '? Nůůůůda')
else:
    print(name, '? To je ale hezké jméno!')

