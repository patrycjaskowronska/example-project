class Trojkat:
    def __init__ (self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c + d
    
    def obwod(self):
        return self.a + self.b + self.c
    
    def pole(self):
        return (self.a * self.h_a) / 2

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_patrycji = Trojkat(16, 5, 8, 12)
# print(trojkat_rownoboczny.obwod())
# print(trojkat_patrycji.pole())

class Trapez:
    def __init__ (self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def obwod(self):
        return self.a + self.b + self.c + self.d
    
    def pole(self):
        return ((self.a + self.b) * self.h) / 2
    
trapez = Trapez(7, 11, 6, 5, 4)
# print(trapez.obwod())
# print(trapez.pole())

print("--------------------------")

class Student:
    def __init__ (self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__ (self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)


student_patrycja = Student("Patrycja", "Skowrońska", 120126)
student_patrycja.dodaj_ocene(4.5)
student_patrycja.dodaj_ocene(5)
# print(student_patrycja.oceny)

class Mieszkanie:
    def __init__ (self, cena, powierzchnia, liczba_pokoi, pietro, adres, czynsz, rynek, rok_budowy):
        self.cena = cena
        self.powierzchnia = powierzchnia
        self.liczba_pokoi = liczba_pokoi
        self.pietro = pietro
        self.adres = adres
        self.czynsz = czynsz
        self.rynek = rynek
        self.rok_budowy = rok_budowy

    def __str__ (self):
        return f"{self.cena} {self.powierzchnia} {self.liczba_pokoi} {self.pietro} {self.adres} {self.czynsz} {self.rynek} {self.rok_budowy}"
    
    def oblicz_cene_za_m2 (self):
        return self.cena / self.powierzchnia
    
    def oblicz_rate_kredytu (self, wklad_wlasny, oprocentowanie, liczba_lat):
        kwota = self.cena - wklad_wlasny
        oproc = oprocentowanie / 100
        liczba_rat = 12 * liczba_lat
        return (kwota * oproc) / (12 * (1-pow(12/(12+oproc), liczba_rat)))
    
mieszkanie = Mieszkanie(450000, 50, 2, 3, "bukowska 14", 430, "wtórny", 2019)
print(mieszkanie.oblicz_cene_za_m2())
print(mieszkanie.oblicz_rate_kredytu(90000, 8.35, 30))