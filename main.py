# 1.
pole_1 = [10, 45, 78, 22, 91, 63, 30, 57, 89]
print("Pole 1:", pole_1)

# 2.
print("První hodnota:", pole_1[0])
print("Prostřední hodnota:", pole_1[len(pole_1) // 2])
print("Poslední hodnota:", pole_1[-1])

# 3.
pole_1[5] = 34
print("Pole 1 po změně 5. indexu na 34:", pole_1)

# 4.
print("Hodnota na indexu 7:", pole_1[7])

# 5.
print("Délka pole 1:", len(pole_1))

# 6.
print("Minimální hodnota v poli 1:", min(pole_1))
print("Maximální hodnota v poli 1:", max(pole_1))

# 7.
pole_2 = [5, 32, 74, 12, 9, 48, 29]
print("Pole 2:", pole_2)

# 8.
pole_spojene = pole_1 + pole_2
print("Spojené pole 1 a 2:", pole_spojene)

# 9.
soucet_poli = pole_2[1] + pole_2[5]
print("Součet hodnot na indexu 1 a 5 z pole 2:", soucet_poli)

# bonus
import random
random.shuffle(pole_2)
print("Náhodně zamíchané pole 2:", pole_2)