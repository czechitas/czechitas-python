# -*- coding: utf-8 -*-
"""
Intenzivní kurz Python
Chyby a výjimky 

@author: Nasťa
Cvíčení 6.2

Napište kód, který se uživatele zeptá na jméno souboru a ten soubor vypíše
Pokud soubor neexistuje, program to řekne uživateli a zeptá se ho znovu, dokud nezadá jméno existujícího souboru
Nápověda
Použijte try - except a while
"""

repeat = True
while repeat:
    try:
        file_name = input('Zadejte jméno souboru: ')
        with open(file_name, 'r', encoding='utf-8') as f:
            repeat = False
            print(f.read())
    except FileNotFoundError:
        print('Soubor neexistuje, tak si to dáme ještě jednou!')
