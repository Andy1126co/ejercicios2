def inversa(z):
    newlis = z[::-1]
    return newlis


def es_palindromo(y):
    c = inversa(y)
    if y == c:
        return "es un palindromo"
    else:
        return "no es un palindromo"


print(inversa('me llamo daniel'))
print(es_palindromo('me llamo daniel'))
