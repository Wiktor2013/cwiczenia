#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''https://python101.readthedocs.io/pl/latest/podstawy/przyklady/przyklad00.html
ZADANIE: Pobierz od użytkownika imię, wiek i powitaj go komunikatem:
“Mów mi Python, mam x lat. Witaj w moim świecie imie. Jesteś starszy(młodszy) ode mnie.”'''
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
#print(f"Current Year -> {year}")

imie, wiek = input('Podaj swoje imie i wiek oddzielone spacją ').split(' ')
x = int(year)-1989
if x > int(wiek):
    print(f'Mów mi Python, mam {x} lat. Witaj w moim świecie {imie}. Jesteś młodszy ode mnie')
else:
    print(f'Mów mi Python, mam {x} lat. Witaj w moim świecie {imie}. Jesteś starszy ode mnie')


#  Rozwiazanie ze strony:
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# deklarujemy i inicjalizujemy zmienne
aktRok = 2021
pythonRok = 1989
# obliczamy wiek Pythona
wiekPythona = aktRok - pythonRok

# pobieramy dane
imie = input('Jak się nazywasz? ')
wiek = int(input('Ile masz lat? '))

# wyświetlamy komunikaty
print("Witaj", imie)
print("Mów mi Python, mam", wiekPythona, "lat.")

# instrukcja warunkowa
if wiek > wiekPythona:
    print('Jesteś starszy ode mnie.')
else:
    print('Jesteś młodszy ode mnie.')