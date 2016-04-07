# -*- coding: utf-8 -*-
"""
Python kurz
Datové typy

@author: Nasťa
Cvičení 2.3

Vytvořte seznam koníčku pomocí postupného přidávání položek do prázdného seznamu dle oblíbenosti (první nejvíce, poslední nejméně)
Vytiskněte svůj nejoblíbenější koníček
Vytiskněte svůj nejméně oblíbený koníček
Vymažte ho ze seznamu
"""
hobbies = []
hobbies.append('hačkování')
hobbies.append('kreslení')
hobbies.append('pečení')
hobbies.append('čtení')
print('Moje koníčky:', ", ".join(hobbies))
print('Můj nejoblíbenější koníček je ', hobbies[0])
print('Můj nejméně oblíbený koníček je ',hobbies[len(hobbies)-1], ', vymažme ho!')
del hobbies[3]
print('Moje koníčky:', ", ".join(hobbies))
