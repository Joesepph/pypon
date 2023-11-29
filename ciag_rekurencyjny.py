def ciag(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 0.5
    else:
        return -ciag(n-1) * ciag(n-2)

n = int(input("Podaj nr wyrazu ciągu, którego wartość chcesz policzyć: "))
print(f"{n} wyraz ciągu ma wartość: ", end="")
print(ciag(n))