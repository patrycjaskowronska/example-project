# Import math Library
import math

# Print the value of pi
print (math.pi)

def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole


# kwadrat, prostokat dla studenta 1
def kwadrat(bok_a):
    obwod = 4 * bok_a
    pole = bok_a * bok_a
    return obwod, pole


def prostokat(bok_a, bok_b):
    obwod = (bok_a*2) + (bok_b*2)
    pole = bok_a*bok_b
    return obwod, pole

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    obwod = 2 * bok_a + 2 * bok_b
    pole = bok_a * wysokosc_a
    return obwod, pole

def romb(bok, wysokosc):
    obwod = bok*4
    pole = bok*wysokosc
    return obwod, pole

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    obwod = bok_a + bok_b + bok_c + bok_d
    pole = ((bok_a + bok_b) * wysokosc_a) / 2
    return obwod, pole


def kolo(promien):
    obwod = 2 * math.pi * promien
    pole = math.pi * pow(promien, 2)
    return obwod, pole


# assert trojkat(10, 15, 16, 8) == (41, 40)
assert kwadrat(20) == (80, 400)
# assert prostokat(12, 10) == (44, 120)
assert rownoleglobok(6, 5, 2) == (22, 12)
# assert romb(10, 5) == (40, 50)
assert trapez(10, 15, 7, 14, 2) == (46, 25)
# assert kwadrat(20) == (80, 400)
assert prostokat(12, 10) == (44, 120)
# assert rownoleglobok(6, 5, 2) == (22, 12)
assert romb(10, 5) == (40, 50)
# assert trapez(10, 15, 7, 14, 2) == (45, 25)
# TODO na koniec (na wyraźne polecenie prowadzącego)! 
# Dla każdej figury powinny znajdować się dwa testy
