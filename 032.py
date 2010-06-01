numbers = "123456789"
m = 0
products = { }
for x in xrange(0, 50):
    for y in xrange(0, 2000):
        z = x * y
        p = str(x) + str(y) + str(z)
        if len(p) == 9:
            if z not in products:
                if numbers.strip(p) == "":
                    m += z
                    products[z] = 1
print m
            