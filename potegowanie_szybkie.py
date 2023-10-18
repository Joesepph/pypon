def main(a, n):
    w = 1

    while (n > 0):
        if (n % 2 == 1):
            w = w * a

        a = a * a
        n = n // 2
    print(str(a) + " do potęgi " + str(n) + " wynosi: " + str(w))
    return w

if __name__ == "__main__":
    podstawa = int(input("Podaj podstawę: "))
    wykladnik = int(input("Podaj wykładnik: "))
    main(podstawa, wykladnik)
