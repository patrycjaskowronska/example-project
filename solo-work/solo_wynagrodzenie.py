class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        pass

    def oblicz_netto(self):
        # https://ksiegowosc-budzetowa.infor.pl/kadry-i-place/wynagrodzenia/5533738,Wzor-obliczania-pensji-netto-z-brutto-przyklad-kroki-algorytm-kalkulator-brutto-netto.html
        ub_spoleczne = self.wynagrodzenie_brutto * 0.1371
        ub_zdrowotne = (self.wynagrodzenie_brutto - ub_spoleczne) * 0.09
        dochod = self.wynagrodzenie_brutto - ub_spoleczne - 250
        podatek = (dochod * 0.12) - 300
        return self.wynagrodzenie_brutto - ub_spoleczne - ub_zdrowotne - podatek
    
    def oblicz_koszty(self):
        # https://pragmago.pl/porada/calkowity-koszt-zatrudnienia-pracownika/
        # return self.wynagrodzenie_brutto * 0.2198
        sk_emerytalna = self.wynagrodzenie_brutto * 0.0976
        sk_rentowa = self.wynagrodzenie_brutto * 0.065
        sk_wypadkowa = self.wynagrodzenie_brutto * 0.0176
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        fundusz_gsp = self.wynagrodzenie_brutto * 0.001
        ppk = self.wynagrodzenie_brutto * 0.015
        return sk_emerytalna + sk_rentowa + sk_wypadkowa + fundusz_pracy + fundusz_gsp + ppk

import csv
file = open('solo-work\salary.csv', "r")
pracownicy = list(csv.reader(file, delimiter=","))
file.close()
pracownicy.pop(0)

koszty_wszystkich_pracownikow = 0
i = 0
for i in range(len(pracownicy)):
    pracownik_i = Pracownik(pracownicy[i][0], pracownicy[i][1], int(pracownicy[i][2]))
    print("Pracownik: "+pracownik_i.imie+" "+pracownik_i.nazwisko)
    print("- pensja brutto: "+str(pracownik_i.wynagrodzenie_brutto))
    print("- pensja netto "+str(pracownik_i.oblicz_netto()))
    print("- koszty pracodawcy: "+str(pracownik_i.oblicz_koszty()))
    koszt_calk = pracownik_i.wynagrodzenie_brutto + pracownik_i.oblicz_koszty()
    print("- koszt całkowity: "+str(koszt_calk))

    koszty_wszystkich_pracownikow = koszty_wszystkich_pracownikow + koszt_calk

print("Suma kosztów wynosi: "+str(koszty_wszystkich_pracownikow))