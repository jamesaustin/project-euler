import math

factorials = [math.factorial(x) for x in range(0,10)]
m = 0
for x in range(3, factorials[9] * 7):
    if x == reduce( lambda a, b: factorials[int(b)] + a, str(x), 0 ):
        m += x
print m