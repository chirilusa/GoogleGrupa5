# Functie care primeste un numar nedefinit de parametrii si calculeaza suma parametrilor care reprezinta numere intregi sau reale

# def suma(*args, **kwargs):
#     s = 0
#     for a in args:
#         if type(a) == int or type(a) == float:
#             s = s + a
#     return s
#
#
# print(suma())

# Functie recursiva


def func_rec(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return func_rec(n - 1)
    else:
        return n + func_rec(n - 1)


print(func_rec(10))

# Functia nr. intreg

# def nr_int(n):
#     if type(n) == int:
#         return n
#     else:
#         return 0
#
# print(nr_int(3))
