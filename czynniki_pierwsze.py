def main(n):
    k = 2
    tablica = []

    while(n > 1):
        while(n % k == 0):
            tablica.append(k)
            n //= k
        k+=1
    print(f"Czynniki pierwsze liczby {naturalna}: " + ' '.join(map(str, tablica)))

if __name__ == "__main__":
    naturalna = int(input("Podaj liczbę: "))
    main(naturalna)