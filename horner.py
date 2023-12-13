def horner(wsp, st, x):
    if st == 0:
        return wsp[0]
    return x * horner(wsp, st - 1, x) + wsp[st]

st = int(input("Podaj stopien wielomianu: "))

wsp = []

for i in range(st,-1,-1):
    liczba = int(input(f"Podaj współczynniki stojący przy potędze {i}: "))
    wsp.append(liczba)

x = int(input("Podaj argument: "))

print(f"W({x}) = ", horner(wsp, st, x))