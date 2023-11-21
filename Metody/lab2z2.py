import numpy as np

def oblicz_roznice_procentowe():
    x = np.arange(0, 1.1, 0.1)
    x_d = np.zeros_like(x, dtype=np.float32)

    wartosci = np.float32(0)
    for i in range(len(x)):
        x_d[i] = wartosci
        wartosci += np.float32(0.1)

    roznice_procentowe = np.abs((x - x_d) / x) * 100
    roznice_procentowe = np.nan_to_num(roznice_procentowe)

    return x_d, roznice_procentowe

x_d, roznice_procentowe = oblicz_roznice_procentowe()

print("Obliczone wartości:")
for a in x_d:
    print(a)

print("\nRóżnice procentowe:")
for roznica in roznice_procentowe:
    print(roznica)
