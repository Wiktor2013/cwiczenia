"""mamy podaną listę liczb. Np. A = [2,1,5,3,6]. Należy posortować ją rosnąco, za pomocą algorytmu bąbelkowego."""
lista = [7, 3, 5, 1]
n = len(lista)
while n > 1:
    zamiana = False
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            zamiana = True
    n -= 1
    print(lista)
    if zamiana == False: break

print(lista)