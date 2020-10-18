from random import choice

bruker_valg = input("Stein, saks, eller papir?").lower()
pc_valg = choice(["stein", "saks", "papir"])


while bruker_valg != "saks" and bruker_valg != "papir" and bruker_valg != "stein":
    print("PRØV IGJEN!")
    bruker_valg = input("Stein, saks, eller papir?").lower()

if bruker_valg == pc_valg:
    print("UAVGJORT!")

elif bruker_valg == "papir" and pc_valg == "stein":
    print("DU VANT!")
elif bruker_valg == "saks" and pc_valg == "papir":
    print("DU VANT!")
elif bruker_valg == "stein" and pc_valg == "saks":
    print("DU VANT!")
else:
    print("DU TAPTE!")

print("Bruker valgte:", bruker_valg)
print("PC'n valgte:", pc_valg)
