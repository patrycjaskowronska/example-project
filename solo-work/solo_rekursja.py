# funkcja sumująca elementy list
# is list empty -> 0
# is list not empty -> list[0] + sum[reszta]

def sum(list):
    if not list:
        return 0
    else:
        return list[0] + sum(list[1:])
        
list_1 = [3,2,7]
print(sum(list_1))

# silnia
# is liczba 0 -> 1
# is liczba not 0 -> liczba * silnia(liczba-1)

def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba-1)
    
print(silnia(5))