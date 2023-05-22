# funkcja sumująca listę
# jeśli lista jest pusta -> suma wynosi 0

# funkcja sum list
# is list empty -> 0
# is list not empty -> list[0] + sum[reszta]

def sum(list):
    if not list:
        return 0
    else:
        return list[0] + sum(list[1:])
        
list_1 = [3,2,7]
print(sum(list_1))
