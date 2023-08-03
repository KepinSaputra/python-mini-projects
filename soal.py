def payroll():
    saldo_awal = 5000
    hutang = 50_000

    deposito = int(input("Masukan Deposito: "))
    saldo_total = saldo_awal + deposito

    if saldo_awal > hutang:
        print("Kamu tidak memiliki utang.")

    sisa_hutang = hutang - saldo_total

    while sisa_hutang != 0:
        print(f"Sisa hutang kamu adalah {sisa_hutang}")
        deposito = int(input("Belum Cukup, Masukan Deposito: "))
        sisa_hutang -= deposito
        saldo_total = deposito - sisa_hutang
    else:
        print("Yeay Sudah Lunas")
