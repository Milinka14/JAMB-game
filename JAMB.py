import random
from datetime import datetime

def od0do1():
    seed = random.randint(1, 1000)
    coin = (429493445 * int(seed) + 907633385) % 4294967296 / 4294967296
    if coin > 0.5:
        return 1
    else:
        return 0


def BacanjeKocke():
    i = od0do1()
    i = i*2 + od0do1()
    i = i*2 + od0do1()
    if i>=6:
        return BacanjeKocke()
    else:
        return i+1

def TransformisiMatricu(Vf,Cf,Rf):
    vrste = 10
    kolone = 3
    matrix = [[0 for j in range(kolone)] for i in range(vrste)]
    for i in range(vrste):
        pocetak = Rf[i]
        kraj = Rf[i + 1]
        for j in range(pocetak, kraj):
            matrix[i][Cf[j]] = Vf[j]
    return matrix
def TransformisiMatricu1(Vf,Cf,Rf):
    vrste = 10
    kolone = 3
    zero = 0
    keco = 0
    rcko = 0
    matrica = [[0 for j in range(kolone)] for i in range(vrste)]
    for i in range(len(Vf)):
        if Cf[i] == 0:
            matrica[zero][0] = Vf[i]
            zero += 1
        if Cf[i] == 1:
            matrica[9 - keco][1] = Vf[i]
            keco += 1
        if Cf[i] == 2:
            matrica[rcko][2] = Vf[i]
            rcko += 1
    print(matrica)
NNZ = 0
V = []
C = []
R = []

while True:
    if len(V)+len(C)+len(R)<33:
        print("JAMB")
        print("Unesite 1. za stvaranje praznog talona:")
        print("Unesite 2. za ispis talona i trenutni broj bodova:")
        print("Unesite 3. da bacite kockice")
        print("Unesite 4. da izaberete pomoc prijatelja")
        print('Unesite 5. da zavrsite program')
        unos = int(input())
        if unos == 1:
            V = []
            C = []
            R = []
            matrica1 = []
            matrica = []
        if unos == 2:
                matrica1 = TransformisiMatricu(V, C, R)
                for i in range(3):
                    s = 0
                    for j in range(10):
                        s += matrica1[j][i]
                    lista[-1][i] = s
                print(matrica1)
        if unos == 3:
            s=0
            j = 0
            ruka = []
            for i in range(5):
                kocka = BacanjeKocke()
                ruka.append(kocka)
            print(ruka)
            while s<3:
                if s == 2:
                    print("Ne mozete ponovo da bacate, ukoliko nemate nijednu kombinaciju unesite 1(izaberite polje koje zelite da prekrizite), ako zelite da unesete 2")
                    unos4 = int(input())
                    if unos4 == 1:
                        print("Koju kolonu zelite da krizate NA DOLE ili NA GORE")
                        unos8 = input()
                        if unos8 == "NA DOLE":
                            V.append("X")
                            C.append(0)
                        if unos8 == "NA GORE":
                            V.append("X")
                            C.append(1)
                    if unos4 == 2:
                        print("Da li zelite da uneste u kolonu na gore ili na dole: ")
                        unos5 = input()
                        if unos5 == "NA DOLE":
                            unos6 = int(input("U koju vrstu na dole ocete da uneste: "))
                            if unos6 == 1:
                                if C.count(0) == 0:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 1:
                                            brojKeceva += 1
                                    V.append(brojBrojeva)
                                    C.append(0)
                            if unos6 == 2:
                                if C.count(0) == 1:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 2:
                                            brojBrojeva += 2
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 3:
                                if C.count(0) == 2:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 3:
                                            brojBrojeva += 3
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 4:
                                if C.count(0) == 3:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 4:
                                            brojBrojeva += 4
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 5:
                                if C.count(0) == 4:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 5:
                                            brojBrojeva += 5
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 6:
                                if C.count(0) == 5:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 6:
                                            brojBrojeva += 6
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "KENTA":
                                if C.count(0) == 6:
                                    ruka1 = sorted(ruka)
                                    jesteKenta = True
                                    for k in range(4):
                                        if ruka1[k] + 1 != ruka1[k + 1]:
                                            jesteKenta = False
                                    if jesteKenta == False:
                                        print("Nemate kombinaciju za kentu")
                                        continue
                                    else:
                                        brojBrojeva = 66
                                        V.append(brojBrojeva)
                                        C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue

                            if unos6 == "FULL":
                                if C.count(0) == 6:
                                    jedanFull = 0
                                    dvaFull = 0
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] and ruka1[2] == ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[2]
                                        brojBrojeva = [jedanFull*2 + dvaFull*3] + 30
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    elif ruka1[0] == ruka1[1] == ruka1[2] and ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[3]
                                        brojBrojeva = [jedanFull * 3 + dvaFull * 2] + 30
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE FULL RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "POKER":
                                if C.count(0) == 8:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1]==ruka1[2]==ruka1[3]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva =4*int(brojBrojeva1)+40
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE POKER RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "JAMB":
                                if C.count(0) == 9:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3]==ruka1[4]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva = 5 * int(brojBrojeva1) + 50
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE JAMB RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                        if unos5 == "NA GORE":
                            unos6 = int(input("U koju vrstu na gore ocete da uneste: "))
                            if unos6 == 1:
                                if C.count(1) == 9:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 1:
                                            brojKeceva += 1
                                    V.append(brojBrojeva)
                                    C.append(1)
                            if unos6 == 2:
                                if C.count(1) == 8:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 2:
                                            brojBrojeva += 2
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 3:
                                if C.count(1) == 7:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 3:
                                            brojBrojeva += 3
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 4:
                                if C.count(1) == 6:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 4:
                                            brojBrojeva += 4
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 5:
                                if C.count(1) == 5:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 5:
                                            brojBrojeva += 5
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 6:
                                if C.count(1) == 4:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 6:
                                            brojBrojeva += 6
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "KENTA":
                                if C.count(1) == 3:
                                    ruka1 = sorted(ruka)
                                    jesteKenta = True
                                    for k in range(4):
                                        if ruka1[k] + 1 != ruka1[k + 1]:
                                            jesteKenta = False
                                    if jesteKenta == False:
                                        print("Nemate kombinaciju za kentu")
                                        continue
                                    else:
                                        brojBrojeva = 66
                                        V.append(brojBrojeva)
                                        C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue

                            if unos6 == "FULL":
                                if C.count(1) == 2:
                                    jedanFull = 0
                                    dvaFull = 0
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] and ruka1[2] == ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[2]
                                        brojBrojeva = [jedanFull*2 + dvaFull*3] + 30
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    elif ruka1[0] == ruka1[1] == ruka1[2] and ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[3]
                                        brojBrojeva = [jedanFull * 3 + dvaFull * 2] + 30
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE FULL RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "POKER":
                                if C.count(1) == 1:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1]==ruka1[2]==ruka1[3]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva =4*int(brojBrojeva1)+40
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE POKER RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "JAMB":
                                if C.count(1) == 0:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3]==ruka1[4]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva = 5 * int(brojBrojeva1) + 50
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE JAMB RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                    break
                print("Ako zelite da upisete rezultat unesite 1, ako zelite da ponovo bacate unesite 2")
                unos1 = int(input())
                if unos1 == 1:
                    if s ==0 :
                        input("Ako zelite da uneste u rucnu ukucajte RUCNA, ako ne zelite NE")
                        unos2 = input()
                        if unos2 == "RUCNA":
                            unos3 = input("U koje polje rucne zelite da unesete:")
                            if unos3 == "1":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 1:
                                        brojKeceva +=  1
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(0)
                            if unos3 == "2":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 2:
                                        brojBrojeva +=  2
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(1)
                            if unos3 == "3":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 3:
                                        brojBrojeva +=  3
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(2)
                            if unos3 == "4":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 4:
                                        brojBrojeva +=  4
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(3)
                            if unos3 == "5":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 5:
                                        brojBrojeva += 5
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(4)
                            if unos3 == "6":
                                brojBrojeva = 0
                                for k in range(5):
                                    if ruka[k] == 6:
                                        brojBrojeva += 6
                                V.append(brojBrojeva)
                                C.append(2)
                                R.append(5)
                            if unos3 == "KENTA":
                                ruka1 = sorted(ruka)
                                jesteKenta = True
                                for k in range(4):
                                    if ruka1[k] + 1 != ruka1[k + 1]:
                                        jesteKenta = False
                                if jesteKenta == False:
                                    print("Nemate kombinaciju za kentu")
                                    continue
                                else:
                                    brojBrojeva = 66
                                    V.append(brojBrojeva)
                                    C.append(2)
                                    R.append(6)

                            if unos3 == "FULL":
                                jedanFull = 0
                                dvaFull = 0
                                ruka1 = sorted(ruka)
                                if ruka1[0] == ruka1[1] and ruka1[2] == ruka1[3] == ruka1[4]:
                                    jedanFull = ruka1[0]
                                    dvaFull = ruka1[2]
                                    brojBrojeva = [jedanFull*2 + dvaFull*3] + 30
                                    V.append(brojBrojeva)
                                    C.append(2)
                                    R.append(7)
                                elif ruka1[0] == ruka1[1] == ruka1[2] and ruka1[3] == ruka1[4]:
                                    jedanFull = ruka1[0]
                                    dvaFull = ruka1[3]
                                    brojBrojeva = [jedanFull * 3 + dvaFull * 2] + 30
                                    V.append(brojBrojeva)
                                    C.append(2)
                                    R.append(7)
                                else:
                                    print("NEMATE FULL RUKU")
                                    continue
                            if unos3 == "POKER":
                                ruka1 = sorted(ruka)
                                if ruka1[0] == ruka1[1]==ruka1[2]==ruka1[3]:
                                    brojBrojeva1 = ruka1[0]
                                    brojBrojeva =4*int(brojBrojeva1)+40
                                    V.append(brojBrojeva)
                                    C.append(2)
                                    R.append(8)
                                else:
                                    print("NEMATE POKER RUKU")
                                    continue
                            if unos3 == "JAMB":
                                ruka1 = sorted(ruka)
                                if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3]==ruka1[4]:
                                    brojBrojeva1 = ruka1[0]
                                    brojBrojeva = 5 * int(brojBrojeva1) + 50
                                    V.append(brojBrojeva)
                                    C.append(2)
                                    R.append(8)
                                else:
                                    print("NEMATE JAMB RUKU")
                                    continue
                            break
                    if s == 0 or s == 1:
                        print("U koju kolonu zelite da uneste NA GORE ili NA DOLE")
                        unos7 = input()
                        if unos7 == "NA DOLE":
                            unos6 = input("U koju vrstu na dole ocete da uneste: ")
                            if unos6 == "1":
                                if C.count(0) == 0:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 1:
                                            brojKeceva += 1
                                    V.append(brojBrojeva)
                                    C.append(0)
                            if unos6 == "2":
                                if C.count(0) == 1:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 2:
                                            brojBrojeva += 2
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "3":
                                if C.count(0) == 2:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 3:
                                            brojBrojeva += 3
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "4":
                                if C.count(0) == 3:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 4:
                                            brojBrojeva += 4
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "5":
                                if C.count(0) == 4:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 5:
                                            brojBrojeva += 5
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "6":
                                if C.count(0) == 5:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 6:
                                            brojBrojeva += 6
                                    V.append(brojBrojeva)
                                    C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "KENTA":
                                if C.count(0) == 6:
                                    ruka1 = sorted(ruka)
                                    jesteKenta = True
                                    for k in range(4):
                                        if ruka1[k] + 1 != ruka1[k + 1]:
                                            jesteKenta = False
                                    if jesteKenta == False:
                                        print("Nemate kombinaciju za kentu")
                                        continue
                                    else:
                                        brojBrojeva = 66
                                        V.append(brojBrojeva)
                                        C.append(0)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue

                            if unos6 == "FULL":
                                if C.count(0) == 6:
                                    jedanFull = 0
                                    dvaFull = 0
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] and ruka1[2] == ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[2]
                                        brojBrojeva = [jedanFull * 2 + dvaFull * 3] + 30
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    elif ruka1[0] == ruka1[1] == ruka1[2] and ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[3]
                                        brojBrojeva = [jedanFull * 3 + dvaFull * 2] + 30
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE FULL RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "POKER":
                                if C.count(0) == 8:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva = 4 * int(brojBrojeva1) + 40
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE POKER RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "JAMB":
                                if C.count(0) == 9:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3] == ruka1[4]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva = 5 * int(brojBrojeva1) + 50
                                        V.append(brojBrojeva)
                                        C.append(0)
                                    else:
                                        print("NEMATE JAMB RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                        if unos7 == "NA GORE":
                            unos6 = int(input("U koju vrstu na gore ocete da uneste: "))
                            if unos6 == 1:
                                if C.count(1) == 9:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 1:
                                            brojKeceva += 1
                                    V.append(brojBrojeva)
                                    C.append(1)
                            if unos6 == 2:
                                if C.count(1) == 8:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 2:
                                            brojBrojeva += 2
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 3:
                                if C.count(1) == 7:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 3:
                                            brojBrojeva += 3
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 4:
                                if C.count(1) == 6:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 4:
                                            brojBrojeva += 4
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 5:
                                if C.count(1) == 5:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 5:
                                            brojBrojeva += 5
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == 6:
                                if C.count(1) == 4:
                                    brojBrojeva = 0
                                    for k in range(5):
                                        if ruka[k] == 6:
                                            brojBrojeva += 6
                                    V.append(brojBrojeva)
                                    C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "KENTA":
                                if C.count(1) == 3:
                                    ruka1 = sorted(ruka)
                                    jesteKenta = True
                                    for k in range(4):
                                        if ruka1[k] + 1 != ruka1[k + 1]:
                                            jesteKenta = False
                                    if jesteKenta == False:
                                        print("Nemate kombinaciju za kentu")
                                        continue
                                    else:
                                        brojBrojeva = 66
                                        V.append(brojBrojeva)
                                        C.append(1)
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue

                            if unos6 == "FULL":
                                if C.count(1) == 2:
                                    jedanFull = 0
                                    dvaFull = 0
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] and ruka1[2] == ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[2]
                                        brojBrojeva = [jedanFull*2 + dvaFull*3] + 30
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    elif ruka1[0] == ruka1[1] == ruka1[2] and ruka1[3] == ruka1[4]:
                                        jedanFull = ruka1[0]
                                        dvaFull = ruka1[3]
                                        brojBrojeva = [jedanFull * 3 + dvaFull * 2] + 30
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE FULL RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "POKER":
                                if C.count(1) == 1:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1]==ruka1[2]==ruka1[3]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva =4*int(brojBrojeva1)+40
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE POKER RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue
                            if unos6 == "JAMB":
                                if C.count(1) == 0:
                                    ruka1 = sorted(ruka)
                                    if ruka1[0] == ruka1[1] == ruka1[2] == ruka1[3]==ruka1[4]:
                                        brojBrojeva1 = ruka1[0]
                                        brojBrojeva = 5 * int(brojBrojeva1) + 50
                                        V.append(brojBrojeva)
                                        C.append(1)
                                    else:
                                        print("NEMATE JAMB RUKU")
                                        continue
                                else:
                                    print("Nemate pravo upisa u ovu vrstu pokusajte ponovo.")
                                    continue


                else:
                    print("Koje kockice zelite da izbacite, i da ih ponovo bacite:")
                    IzbacitiKockice = input().split()
                    for i in range(len(IzbacitiKockice)):
                        ruka.pop(int(IzbacitiKockice[i]) - 1)
                        ruka.insert(int(IzbacitiKockice[i]) - 1, BacanjeKocke())
                    print(ruka)
                    s+=1
        if unos == 5:
            exit()
        pass
    else:
        matrica = TransformisiMatricu(V,C,R)
        print("JAMB")
        print("Unesite 1. za stvaranje praznog talona:")
        print("Unesite 2. za ispis talona i trenutni broj bodova:")
        print("Unesite 3. da bacite kockice")
        print("Unesite 4. da izaberete pomoc prijatelja")
        print('Unesite 5. da zavrsite program')
        unos = int(input())
        if unos == 1:
            ruka = []
            V = []
            C = []
            R = []
            NNZ = 0
            matrica1 = []
            matrica = []
        if unos == 2:
            for i in range(3):
                s = 0
                for j in range(10):
                    s += matrica[j][i]
                lista[-1][i] = s
            print(matrica)
        if unos == 3:
            j = 0
            ruka = []
            for i in range(5):
                kocka = BacanjeKocke()
                ruka.append(kocka)
            print(ruka)
            for s in range(3):
                if s == 2:
                    print("Ne mozete ponovo da bacate, ako zelite da krizate polje unesite 1, ako zelite da unesete 2")
                    pass
                print("Ako zelite da upisete rezultat unesite 1, ako zelite da ponovo bacate unesite 2")
                unos1 = int(input())
                if unos == 1:
                    if s == 0:
                        print("Imate pravo upisa u rucnu:")
                    break
                else:
                    print("Koje kockice zelite da izbacite, i da ih ponovo bacite:")
                    IzbacitiKockice = input().split()
                    for i in range(len(IzbacitiKockice)):
                        ruka.pop(int(IzbacitiKockice[i])-1)
                        ruka.insert(int(IzbacitiKockice[i])-1,BacanjeKocke())
                    print(ruka)
        if unos ==5:
            exit()