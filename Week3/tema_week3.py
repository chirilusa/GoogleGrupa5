# Functie care primeste un numar nedefinit de parametrii si calculeaza suma parametrilor care reprezinta numere intregi sau reale

def Suma(*args, **kwargs):
    s = 0
    for a in args:
        if type(a) == int or type(a) == float:
            s = s + a
    print(s)
    return 0


Suma(2, 4, 'abc', -2, param=2)
