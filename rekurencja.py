def silnia(n): 
    if n > 1:
        return n*silnia(n-1)
    else:
        return 1

n = int(input("Podaj liczbę: "))
print(f"{n}! = {silnia(n)}")