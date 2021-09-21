"""Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście."""
lista = [1,3,7,11,2,-6,0]

maksiu = None
miniu = None

for i in lista:
    if miniu == None or miniu > i:
        miniu = i
    if maksiu == None or maksiu < i:
        maksiu = i
print("Maksiu", "to", maksiu)
print("Miniu", "to", miniu)