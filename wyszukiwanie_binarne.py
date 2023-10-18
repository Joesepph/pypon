def wyszukiwanie_binarne(szukana, tab):
    l = 0
    r = len(tab) - 1

    while l <= r:
        sr = (l + r) // 2

        if tab[sr] == szukana:
            return sr

        if tab[sr] > szukana:
            r = sr - 1
        else:
            l = sr + 1

    return -1

def main():
    szukana = int(input("Wyszukaj liczbę: "))
    tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    wynik = wyszukiwanie_binarne(szukana, tab)

    if wynik == -1:
        print("Taka liczba nie istnieje")
    else:
        print(f"Liczba {szukana} występuje w indeksie {wynik}")

if __name__ == "__main__":
    main()
