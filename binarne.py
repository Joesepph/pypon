def binarne(liczba):
    bin_l = bin(liczba)[2:]
    print(bin_l)

liczba = int(input("Podaj liczbę: "))
binarne(liczba)