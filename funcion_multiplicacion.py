def multip(z):
    c = 1
    r = len(z)
    for i in range(r):
        c *=z[i]

    return c

print(multip([1,2,3,4,5]))