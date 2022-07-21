kina = ["Cinema-City", "Multikino"]
filmy = {"Cinema-City" : ["Matrix", "Avatar", "Shrek"], "Multikino" : ["Piraci z Karaibów", "Król Lew", "Władcy Pierścieni"]}
litery = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
cenaBilet = 18.00
kwota = 0

while(True):
    while(True):
        try:
            kino = kina[int(input("Wybierz kino: 0 - Cinema-City, 1 - Multikino"))]
            print(f"Wybrałeś kino {kino}")
            while(True):
                try:
                    print(f"0 - {filmy[kino][0]}, 1 - {filmy[kino][1]}, 2 - {filmy[kino][2]}")
                    film = filmy[kino][int(input("Wybierz film: "))]
                    print(f"Wybrałeś film {film}.")
                    while(True):
                        try:
                            liczbaOsob = int(input("Podaj liczbę osób:"))
                            kwota = cenaBilet * liczbaOsob
                            while(True):
                                imie = input("Podaj imię do rezerwacji:")
                                noweImie = imie.lower()
                                znaleziono = 0
                                for i in range(len(noweImie)):
                                    for j in litery:
                                        if(noweImie[i] == j):
                                            znaleziono+=1
                                if(znaleziono != len(imie)):
                                    print("Podałeś niedozwolone znaki. Użyj samych liter.")
                                else:
                                    print(f"Cześć, {imie}! Dokonałeś wstępnej rezerwacji w kinie {kino} na film {film}. W celu dokończenia procesu, opłać zamówienie. Całkowita kwota to: {kwota}.")
                                    break
                        except ValueError:
                            print("Zły format")
                        else:
                            break
                except ValueError:
                    print("Zły format")
                except IndexError:
                    print("Nie ma filmu o danym indeksie.")
                else:
                    break
        except ValueError:
            print("Zły format")
        except IndexError:
            print("Nie ma kina o danym indeksie.")
        else:
            break
    break
