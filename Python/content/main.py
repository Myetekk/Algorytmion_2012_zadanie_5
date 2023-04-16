# Algorytmion 2012 zad 5 - "Tabliczka"
import random

tab = [  "1",  "2",  "3",  "4",
         "5",  "6",  "7",  "8",
         "9", "10", "11", "12",
        "13", "14", "15",  "0"  ]

def wypisz():  # funkcja wypisujaca tablice w odpowiedni sposob
    for m in range(16):
        print(tab[m], end=" ")
        if int(tab[m]) < 10:
            print("", end=" ")
        if (m+1)%4 == 0:
            print()

def sprawdz():  # funkcja sprawdzajaca czy tabelka jest wystarczajaco posortowana
    # zakladam, ze wystarczajaco posortowana tabelka to taka, w ktorej dwie nastepne liczby nie leza obok siebie (np. 5, 6)
    for i in range(0, 15):
        if int(tab[i]) + 1 == int(tab[i + 1]):
            return True
        if int(tab[i]) - 1 == int(tab[i + 1]):
            return True
        if i < 11:
            if int(tab[i])+1 == int(tab[i + 4]):
                return True
            if int(tab[i]) - 1 == int(tab[i + 4]):
                return True
    return False


def losuj():
    index = 15  # indeks pustego pola
    prev_index = 15  # poprzedni indeks
    prev = 4  # poprzedni kierunek
    prevprev = 4  # poprzedni poprzedni kieraunek
    count = 0  # licznik ruchow
    kierunek = 0  # wylosowany kierunek

    while sprawdz():
        git = False
        while git is False:
            git = True
            r = random.randint(0, 3)  # losujemy kierunek

            if r is not prev and r is prevprev:
                prevprev = 4
            if r is prevprev:
                git = False
            if (r+2)%4 is prev:
                git = False

            if git is True:
                prev_index = index
                match r:
                    case 0:  # w lewo
                        if index not in {0, 4, 8, 12}:
                            index -= 1
                        else:
                            git = False
                    case 1:  # w gore
                        if index not in {0, 1, 2, 3}:
                            index -= 4
                        else:
                            git = False
                    case 2:  # w prawo
                        if index not in {3, 7, 11, 15}:
                            index += 1
                        else:
                            git = False
                    case 3:  # w dol
                        if index not in {12, 13, 14, 15}:
                            index += 4
                        else:
                            git = False
                if git is True:
                    temp = tab[prev_index]
                    tab[prev_index] = tab[index]
                    tab[index] = temp
                    prevprev = prev
                    prev = r
                    count += 1
    wypisz()
    print("\nŻeby rozwiązać tabliczke potrzeba: ", count, " ruchów \n")
    try:
        plik = open("output/output.txt", "w")
    except IOError:
        print("Blad otwierania pliku")
        exit()
    for i in range(16):
        plik.write(str(tab[i]) + "\n")
    plik.write(str(count))
    plik.close()

losuj()
