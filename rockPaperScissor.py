# Buat list berisi [Gunting, Batu, Kertas]
# Masukin Input User
# Bikin musuh (komputer)
# print Siapa yang menang

import random


def main_gamsuit():
    pilihan_user = input("Gunting || Batu || Kertas: ").lower()
    pilihan_komputer = random.choice(["gunting", "batu", "kertas"])
    print(pilihan_komputer)
    if pilihan_user == pilihan_komputer:
        print("Seri!!")

    if is_win(pilihan_user, pilihan_komputer):
        print("Kamu Menang")

    return print("Kamu Kalah")


def is_win(user, komputer):
    if (
        (user == "gunting" and komputer == "kertas")
        or (user == "batu" and komputer == "gunting")
        or (user == "kertas" and komputer == "batu")
    ):
        return True


main_gamsuit()
