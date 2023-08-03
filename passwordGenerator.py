import secrets
import string
import clipboard

letter = string.ascii_letters
symbols = string.punctuation
number = string.digits

availablePass = letter + symbols + number

randomPass = ""


def create():
    passLength = int(
        input("Masukan mau berapa banyak digit password (Min: 6) (Max: 12): ")
    )
    while passLength < 6 or passLength > 12:
        passLength = int(input("Masukan Min 6 - Max 12 digit "))
    else:
        for i in range(passLength):
            global randomPass
            randomPass += "".join(secrets.choice(availablePass))
        print("Password Created!")


user_input = input("Maukah anda men-generate password?[Y|N] ").lower()
if user_input == "y":
    create()
    user_input = input("Maukah anda melihat password anda?[Y|N] ").lower()
    if user_input == "y":
        print(f"Berikut adalah password anda: {randomPass}")
        clipboard.copy(randomPass)
    else:
        clipboard.copy(randomPass)
        print("Your Password has been copied to your clipboard! Thank You!")
else:
    print("Bye!")
