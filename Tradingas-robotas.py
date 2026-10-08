# Nerijaus Tradingas Robotas
# Sukurta: 2026
# GitHub: NerijusSerepinas

def tradingas_robotas(vardas, balansas):
    print("=== " + vardas + " TRADINGAS ROBOTAS ===")
    print("Balansas: £" + str(balansas))
    print("")

    duomenys = [
        {"ema50": 1850, "ema200": 1800, "rsi": 60},
        {"ema50": 1750, "ema200": 1800, "rsi": 42},
        {"ema50": 1900, "ema200": 1850, "rsi": 50},
        {"ema50": 2000, "ema200": 1900, "rsi": 58},
    ]

    pradinis = balansas
    i = 0
    while i < len(duomenys):
        d = duomenys[i]
        print("Bar " + str(i+1) + ":")
        if d["ema50"] > d["ema200"] and d["rsi"] >= 55:
            balansas -= 100
            print("  📈 PIRKTI! Balansas: £" + str(balansas))
        elif d["ema50"] < d["ema200"] and d["rsi"] <= 45:
            balansas += 150
            print("  📉 PARDUOTI! Balansas: £" + str(balansas))
        else:
            print("  ⏳ LAUKTI!")
        i = i + 1

    print("")
    print("=== REZULTATAI ===")
    print("Pradinis: £" + str(pradinis))
    print("Galutinis: £" + str(balansas))
    print("Pelnas: £" + str(balansas - pradinis))
    if balansas > pradinis:
        print("🎉 LAIMĖJAI!")
    else:
        print("📊 Mokykis toliau!")

vardas = input("Vardas? ")
balansas = int(input("Balansas £? "))
tradingas_robotas(vardas, balansas)
