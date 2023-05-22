# suma wszystkich elementów listy
# jeżeli lista jest pusta zwróć: 0
# w przeciwnym przypadku zwróć: pierwszy element listy + suma reszty elementów

def sum(list):
    if not list:
        return 0
    else:
        return list[0] + sum(list[1:])
        
list_1 = [3,2,7]
print(sum(list_1))

# funkcja silnia
# jeżeli liczba = 0 zwróć: 1
# w przeciwnym przypadku zwróć: liczba * silnia(liczba-1)

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(5))

# wartość maksymalna w liście
# funkcja max_list
# n = długość listy
# jeżeli n = 1 zwróć: pierwszy element listy
# w przeciwnym przypadku zwróć: max(ostatni element listy, max_list(pozostałe elementy listy)) 
 
def max_list(list):
    n = len(list)
    if n == 1:
        return list[0]
    else:
        return max(list[n-1], max_list(list[:(n-2)]))
            
list_2 = [22, 17, 34, 51, 13]
print(max(list_2))

# fibonacci