# -*- coding: utf-8 -*-
"""
Python kurz
Moduly a práce se soubory

@author: Nasťa
Cvičení 5.1

Vytvořte seznam věcí, které byste vzali na pustý ostrov
Tento seznam zapište do souboru tak, aby byly řádky očíslovány a mezi číslem a textem byl tabulátor
Příklad
1	hrnec
2	plachta
3	kapesní nůž
4	léky
5	rybářský prut
"""

island_list = ['hrnec', 'plachta', 'kapesní nůž', 'léky', 'rybářský prut', 'solární generátor', 'zápalky', 'notebook', 'spacák', 'kamarád/ka']
print('island_list =', island_list)
island_file = open('ostrov_seznam.txt','w', encoding ='utf-8')
count = 1
for line in island_list:
    line_to_file = str(count) + '\t' + line
    print(line_to_file)
    island_file.write(line_to_file+ '\n')
    count = count + 1
island_file.close()