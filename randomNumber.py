import random

user_input = int(input("Input angka: "))
random_number = random.randint(0, user_input)
tebakan_user_input = int(input(f"Silahkan tebak dari 0 - {user_input}: "))


def nebak(tebakan_user):
    pengulangan = 1
    while tebakan_user != random_number:
        pengulangan += 1
        tebakan_user = int(input("coba lagi: "))
        if tebakan_user == random_number:
            print(f"Kamu Berhasil dalam {pengulangan}x")
            break
        elif tebakan_user > random_number:
            print("Tebakan lebih besar")
        else:
            print("Tebakan Lebih Kecil")
            continue


if tebakan_user_input == random_number:
    print("BENARR")
else:
    nebak(tebakan_user_input)
