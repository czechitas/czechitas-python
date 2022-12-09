# -*- coding: utf-8 -*-
"""
Intenzivní kurz Python
Funkce

@author: Nasťa
Cvíčení 4.2

Vytvořte funkci, která má 2 parametry: cena oběda a hodnota stravenky
Funkce vypočítá, kolik je potřeba stravenek a kolik je potřeba doplatit hotově
Příklad
>>> meal_vouchers(500, 74)
Oběd stojí: 500 Kč
Zaplaťte hotově: 56 Kč
Zaplaťte stravenkami: 6 ks po 74 Kč
"""
def meal_vouchers(lunch_price, meal_voucher_value):
    meal_voucher_number = int(lunch_price) // int(meal_voucher_value)
    money = int(lunch_price) - (meal_voucher_number * int(meal_voucher_value))
    print('Oběd stojí:', lunch_price, 'Kč')
    print('Zaplaťte hotově:', money, 'Kč')
    print('Zaplaťte stravenkami:', meal_voucher_number, 'ks po', meal_voucher_value, 'Kč')

meal_vouchers(500, 74)