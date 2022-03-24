def superposicion(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
            else:
                return False


lis1 = [1, 2, 3, 4, 5, 6]
lis2 = [7, 9, 10]
print(superposicion(lis1, lis2))
