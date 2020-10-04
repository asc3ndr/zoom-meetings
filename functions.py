# I DET GLOBALE SCOPE
var_1 = "Hallo"
var_2 = "hei"
var_3 = "Ho"
var_4 = "OK"
global_variabel = "Global"


def min_print(param1, param2, param3, param4="IKKE OK"):  # Definert et parameter
    # LOKALT SCOPE
    lokal_variabel = "LOKAL"
    print(param1)
    print(param2)
    print(param3)
    print(param4)
    from string import ascii_letters

    return ascii_letters


min_liste = [1, 2, 3, 4, 5]


print(id(min_liste))
print(min_liste)

min_liste.append(6)

print(id(min_liste))
print(min_liste)

print("\n")

en_tekst = "dette er tekst"

print(en_tekst)
print(id(en_tekst))


def ny():
    ny_tekst = en_tekst + " mere tekst"
    print(ny_tekst)
    print(id(ny_tekst))


ny()

print(en_tekst)
print(id(en_tekst))


hemmelig_ord = list("hemmelig")
hangman = ["___" for x in hemmelig_ord]


bokstav = input("Gi meg en bokstav")

# ALTERNATIV 1: ENUMERATE
for index, verdi in enumerate(hemmelig_ord):
    if bokstav == verdi:
        hangman[index] = verdi


# ALTERNATIV 2: INDEX MANIPULASJON
for index in range(len(hemmelig_ord)):
    if bokstav == hemmelig_ord[index]:
        hangman[index] = bokstav

# ALTERNATIV 3: REKKEFOLGE
# Vanskeligere

