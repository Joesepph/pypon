def binarne(liczba):
    if liczba >= 1:
        binarne(liczba // 2)
    print(liczba % 2, end='')

liczba = int(input("Podaj liczbę dziesiętną: "))
print(f"Liczba {liczba} po zamianie na postać binarną: {binarne(liczba)}")