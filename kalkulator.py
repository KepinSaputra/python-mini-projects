angka1 = input("Silahkan masukan angka pertama: ")
angka2 = input("Silahkan masukan angka kedua: ")


def calc(num1, num2):
    if num1.isdigit() and num2.isdigit():
        operator = input("Masukan Operator Perhitungan: ")
        match operator:
            case "+":
                hasil_perhitungan = int(num1) + int(num2)
                print(f"{num1} + {num2} adalah {hasil_perhitungan}")
            case "-":
                hasil_perhitungan = int(num1) - int(num2)
                print(f"{num1} - {num2} adalah {hasil_perhitungan}")
            case "*":
                hasil_perhitungan = int(num1) * int(num2)
                print(f"{num1} X {num2} adalah {hasil_perhitungan}")
            case "/":
                hasil_perhitungan = int(num1) / int(num2)
                print(f"{num1} / {num2} adalah {hasil_perhitungan}")
    else:
        print("Silahkan masukan nomor")


calc(angka1, angka2)
