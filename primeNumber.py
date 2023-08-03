target_angka = int(input("Masukan angka: "))
angka_prima = []

for angka in range(1, target_angka + 1):
    count = 0
    for i in range(2, angka // 2 + 1):
        if angka % i == 0:
            count += 1
            break
    if count == 0 and angka != 1:
        angka_prima.append(angka)

print(angka_prima)
