from telek_adatok import Ingatlan


# 4. feladat
def ado(adosavok, adosav, alapter):
    fizetendo = adosavok[adosav] * alapter
    if fizetendo < 10000:
        fizetendo = 0
    return fizetendo


def main():
    # 1. feladat
    epitmenyek = []
    with open('utca.txt', 'r', encoding='utf-8') as fajl:
        elso = fajl.readline().strip().split()
        adosavok = {'A': int(elso[0]), 'B': int(elso[1]), 'C': int(elso[2])}
        for sor in fajl:
            temp = sor.strip().split()
            epitmenyek.append(Ingatlan(temp[0], temp[1], temp[2], temp[3], int(temp[4])))
            """
            epitmeny = {
                'adoszam': temp[0],
                'utcanev': temp[1],
                'hazszam': temp[2],
                'sav': temp[3],
                'alapter': temp[4]
            }
            epitmenyek.append(epitmeny)
            """
    fajl.close()
    # print(adosavok)
    # print(*epitmenyek, sep="\n")
    # print(epitmenyek[0]['adoszam'])
    # 2. feladat
    print(f"2. feladat. A mintában {len(epitmenyek)} telek szerepel.")

    # 3. feladat
    adoszam = input("3. feladat. Egy tulajdonos adószáma: ")
    talalat = False
    for e in epitmenyek:
        if e.adoszam == adoszam:
            talalat = True
            print(f"{e.utcanev} {e.haszszam}")
    if not talalat:
        print("Nem szerepel az adatállományban.")

    # 5. feladat
    a_ado, b_ado, c_ado, a_db, b_db, c_db = [0, 0, 0, 0, 0, 0]
    for e in epitmenyek:
        if e.sav == "A":
            a_ado += ado(adosavok, e.sav, e.alapter)
            a_db += 1
        elif  e.sav == "B":
            b_ado += ado(adosavok, e.sav, e.alapter)
            b_db += 1
        elif e.sav == "C":
            c_ado += ado(adosavok, e.sav, e.alapter)
            c_db += 1
    print(f"A sávba {a_db} esik, az ado {a_ado} Ft.")
    print(f"B sávba {b_db} esik, az ado {b_ado} Ft.")
    print(f"C sávba {c_db} esik, az ado {c_ado} Ft.")

    # 6. feladat
    utca_sav = {}
    for epitmeny in epitmenyek:
        if epitmeny.utcanev in utca_sav:
            utca_sav[epitmeny.utcanev].add(epitmeny.sav)
        else:
            utca_sav[epitmeny.utcanev] = set(epitmeny.sav)

    # print(utca_sav, sep="\n")
    print("6. feladat. Több sávba sorolt utcák:")
    for utca in utca_sav:
        if len(utca_sav[utca]) > 1:
            print(utca)

    # 7. feladat
    ado_fizetendo = {}
    for epitmeny in epitmenyek:
        if epitmeny.adoszam in ado_fizetendo:
            ado_fizetendo[epitmeny.adoszam] += ado(adosavok, epitmeny.sav, epitmeny.alapter)
        else:
            ado_fizetendo[epitmeny.adoszam] = ado(adosavok, epitmeny.sav, epitmeny.alapter)
    # print(ado_fizetendo, sep="\n")
    with open('fizetendo.txt', 'w', encoding='utf-8') as fizetendo:
        for adoszam in ado_fizetendo:
            print(adoszam, ado_fizetendo[adoszam], file=fizetendo)



if __name__ == '__main__':
    main()
