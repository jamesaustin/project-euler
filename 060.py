import math

from primes import is_prime_c as is_prime
from primes import prime_list

l = 8500
primes_list = [3] + prime_list(l)[3:]
len_primes_list = len(primes_list)

def pair_prime(a, b):
    return is_prime(int(a + b)) and is_prime(int(b + a))

def f():
    M = l * 5
    for c1 in xrange(len_primes_list - 4):
        p1 = primes_list[c1]
        s1 = str(p1)
        for c2 in xrange(c1, len_primes_list - 3):
            p2 = primes_list[c2]
            t2 = p1 + p2
            s2 = str(p2)
            if pair_prime(s1, s2):
                for c3 in xrange(c2, len_primes_list - 2):
                    p3 = primes_list[c3]
                    t3 = t2 + p3
                    s3 = str(p3)
                    if pair_prime(s1, s3) and pair_prime(s2, s3):
                        for c4 in xrange(c3, len_primes_list - 1):
                            p4 = primes_list[c4]
                            t4 = t3 + p4
                            if (t4 + p4) >= M:
                                break
                            s4 = str(p4)
                            if pair_prime(s1, s4) and pair_prime(s2, s4) and pair_prime(s3, s4):
                                for c5 in xrange(c4, len_primes_list):
                                    p5 = primes_list[c5]
                                    t5 = t4 + p5
                                    if t5 >= M:
                                        break
                                    s5 = str(p5)
                                    if pair_prime(s1, s5) and pair_prime(s2, s5) and pair_prime(s3, s5) \
                                        and pair_prime(s4, s5):
                                        M = min(M, t5)

    return M

print f()

def pair_prime(a, b, ma, mb):
    return is_prime(b + a *  mb) and is_prime(a + b * ma)

def g():
    M = l * 5
    for c1 in xrange(len_primes_list - 4):
        p1 = primes_list[c1]
        m1 = 10 ** (int(math.log10(p1)) + 1)
        for c2 in xrange(c1, len_primes_list - 3):
            p2 = primes_list[c2]
            t2 = p1 + p2
            m2 = 10 ** (int(math.log10(p2)) + 1)
            if pair_prime(p1, p2, m1, m2):
                for c3 in xrange(c2, len_primes_list - 2):
                    p3 = primes_list[c3]
                    t3 = t2 + p3
                    m3 = 10 ** (int(math.log10(p3)) + 1)
                    if pair_prime(p1, p3, m1, m3) and pair_prime(p2, p3, m2, m3):
                        for c4 in xrange(c3, len_primes_list - 1):
                            p4 = primes_list[c4]
                            t4 = t3 + p4
                            m4 = 10 ** (int(math.log10(p4)) + 1)
                            if (t4 + p4) >= M:
                                break
                            if pair_prime(p1, p4, m1, m4) and pair_prime(p2, p4, m2, m4) and pair_prime(p3, p4, m3, m4):
                                for c5 in xrange(c4, len_primes_list):
                                    p5 = primes_list[c5]
                                    t5 = t4 + p5
                                    if t5 >= M:
                                        break
                                    m5 = 10 ** (int(math.log10(p5)) + 1)
                                    if pair_prime(p1, p5, m1, m5) and pair_prime(p2, p5, m2, m5) and \
                                        pair_prime(p3, p5, m3, m5) and pair_prime(p4, p5, m4, m5):
                                        M = min(M, t5)

    return M

print g()
