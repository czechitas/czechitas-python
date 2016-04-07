# -*- coding: utf-8 -*-
"""
Intenzivní kurz Python
Funkce 

@author: Nasťa
Cvíčení 4.1

Napište funkci, která bere jako parametr textový řetězec a vrací počet velkých a malých písmen
Nápověda: hodnotu proměnné se dá zvyšovat v každém cyklu pomocí výrazu "proměnná += 1"
Příklad:
>>> string_upper_lower(s)
Řetězec: Byl jeden Řek a ten mi řek, abych mu řek, 
kolik je v Řecku řeckých řek a já mu řek, 
že nejsem Řek abych mu řek kolik je v Řecku řeckých řek.
Počet velkých písmen: 5
Počet malých písmen: 100
"""

def string_upper_lower(s): 
    """ Tato funkce bere řetězec a počítá vlká a malá písmena """
    upper = 0
    lower = 0
    for c in s:  
        if c.isupper():  
           upper +=1  
        if c.islower():  
           lower +=1    
    print ("Řetězec: ", s)  
    print ("Počet velkých písmen: ", upper)  
    print ("Počet malých písmen: ", lower)  
  
s = """Byl jeden Řek a ten mi řek, abych mu řek, 
kolik je v Řecku řeckých řek a já mu řek, 
že nejsem Řek abych mu řek kolik je v Řecku řeckých řek."""

string_upper_lower(s)  
