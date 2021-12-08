#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''ZADANIE: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.'''

op = 't'
while op == 't':
    x, y, z = input('Podaj trzy liczby oddzielone spacją ').split(' ')

    print(f'Wprowadzono liczby {x} {y} {z} ')
    # print(f'Najmniejsza to {najmniejsza}')

    if int(x) < int(y):
        if int(x) < int(z):
            najmniejsza = x
        else:
            najmniejsza = z
    elif int(y) < int(z):
        najmniejsza = y
    else:
        najmniejsza = z

    print(najmniejsza)

    op = input('Jeszcze raz (t/n)? ')

print('Koniec')

#  Inne rozwiazanie z mniejsza iloscia kodu
x, y, z = input('Podaj trzy liczby oddzielone spacją ').split(' ')
smallest = int(x)
if (int(y) < int(x)) and (int(y) < int(z)):
    smallest = y
elif (int(z) < int(x)):
    smallest = z
print(f'Najmniejsza liczba to: {smallest}')