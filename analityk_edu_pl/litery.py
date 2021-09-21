"""Mamy podany ciąg S. Np „Ala ma kota”. W ramach zadania możemy zostać poproszeni o jedno, lub więcej z poniższych:
1. zliczyć wyrazy. W naszym przypadku będzie ich 3
2. zliczyć litery. Będzie ich 9
3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1"""

#lines = []
with open("/home/sanczo/PycharmProjects/cwiczenia/analityk_edu_pl/maszyna_trurla.txt", "r") as f: #  otwieram plik
    linie = f.readlines()  #  czytam linie
licznik_linii = 0
licznik_wyrazow = 0
licznik_liter = 0
for linia in linie: #  iteruje po liniach
    licznik_linii += 1 # licznik zwieksza swoja wartosc o numer kolejnej linii
    ilosc_wyrazow = len(linia.split(" "))  # rozdzielam linie na podstawie znaku spacji licze elementy po podzieleniu
    licznik_wyrazow += ilosc_wyrazow
    for char in linia:
        char = char.lower()
        if char != " ":
            licznik_liter += 1


    #print(linia)
    #print(ilosc_wyrazow)
print(type(linia))
print(f'linii jest {licznik_linii}: wyrazow jest: {licznik_wyrazow} liter jest: {licznik_liter}')


print(f'liter jest {licznik_liter}: wyrazow jest: {licznik_wyrazow}')


f.close()