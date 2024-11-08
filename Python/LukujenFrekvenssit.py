luvut = []

while True:
    print("Syötä luku 1-99, tai nolla lopettaaksesi:")
    luku = int(input())
    if luku == 0:
        break
    luvut.append(luku)

# Esimerkkilista kokonaisluvuista
# luvut = [3, 7, 12, 15, 22, 25, 29, 31, 36, 42, 48, 53, 59, 62, 71, 83]

# Alustetaan sanakirja frekvenssien tallentamiseksi
frekvenssit = {}

# Lasketaan frekvenssit jakolaskulla
for luku in luvut:
    ryhma = (luku // 10) * 10  # Tämä antaa ryhmän alkuluvun
    if ryhma in frekvenssit:
        frekvenssit[ryhma] += 1
    else:
        frekvenssit[ryhma] = 1

# Tulostetaan tulokset selkeästi
for ryhma in sorted(frekvenssit):
    print(f"Väli {ryhma}-{ryhma + 9}: {frekvenssit[ryhma]}")
