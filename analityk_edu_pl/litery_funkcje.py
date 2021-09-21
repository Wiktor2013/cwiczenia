"""Mamy podany ciąg S. Np „Ala ma kota”. W ramach zadania możemy zostać poproszeni o jedno, lub więcej z poniższych:
1. zliczyć wyrazy. W naszym przypadku będzie ich 3
2. zliczyć litery. Będzie ich 9
3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1"""

with open("/home/sanczo/PycharmProjects/cwiczenia/analityk_edu_pl/maszyna_trurla.txt", "r") as f: #  otwieram plik
    wersy = f.readlines()  #  czytam linie

def licznik_tekstowy(t):
    linie = 0
    slowa = 0
    litery = 0
    slownik = {}

    for x in t:  # iteruje po liniach
        linie += 1  # licznik zwieksza swoja wartosc o numer kolejnej linii
        ilosc_wyrazow = len(x.split(" "))  # rozdzielam linie na podstawie znaku spacji licze elementy po podzieleniu
        slowa += ilosc_wyrazow # do zmiennej slowa dodaje liczbe elementow z poprzedniej linii
        for char in x: # iteruje po znakach w elementach linii
            char = char.lower() # zmieniam na male litery
            if char != " ":
                litery += 1
            if char in slownik:
                slownik[char] += 1
            else:
                slownik[char] = 1

    return linie, slowa, litery, slownik
print(licznik_tekstowy(wersy))

