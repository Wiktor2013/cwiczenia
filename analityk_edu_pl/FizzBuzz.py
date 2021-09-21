"""Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’,
liczby podzielne przez 5, zastąp słowem ‘Buzz’, natomiast liczby podzielne i przez 3
i przez 5 zastąp słowem ‘FizzBuzz’."""
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)