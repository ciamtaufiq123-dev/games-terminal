import random

def operasi(operasi_str):
    try:
        angka1 = float(input("Masukkan angka ke 1 :"))
        angka2 = float(input("Masukkan angka ke 2 :"))
        if operasi_str == "/" and angka2 == 0:
            print("gabisa bro, pembagian gabisa di bagi 0 ya!\n")
            return
        hasil = eval(f" {angka1} {operasi_str} {angka2}\n")
        print(hasil)
    except ValueError:
        print("gabisa bro, input CUMA bisa angka aja ya!\n")
def tebakan():
    angka_acak = random.randint(1, 10)
    print("selamat datang di permainan tebakan angka!")
    tebakan_me = 0
    while tebakan_me != angka_acak:
        try:
            tebakan_me = int(input("tebak angka antara 1-10 :"))
        except ValueError:
            print("gabisa bro, input cuma bisa angka doang ya!\n")
            continue
        if tebakan_me < angka_acak:
            print("tebakan kamu terlalu kecil bro!\n")
        elif tebakan_me > angka_acak:
            print("tebakan kamu terlalu besar bro!\n")
        else:
            print("wahh, selamat bro tebakan kamu benar, ada di angka", angka_acak)
            break
def menu():
    while True:
        print("===Games_Tebak_Angka===")
        print("1. Mulai Tebakan\n")
        print("===Kalkulator_Sederhana===")
        print("2. Penjumlahan")
        print("3. Pengurangan")
        print("4. Perkalian")
        print("5. Pembagian")
        print("6. Keluar")
        try:
            pilihan = int(input("Masukka pilihan Anda :\n"))
        except ValueError:
            
            print("gabisa bro, input cuma bisa angka saja ya!\n")
            continue
        if pilihan == 1:
            tebakan()
        elif pilihan == 2:
            operasi("+")
        elif pilihan == 3:
            operasi("-")
        elif pilihan == 4:
            operasi("*")
        elif pilihan == 5:
            operasi("/")
        elif pilihan == 6:
            print("Terima kasih telah berkunjung ya !\n")
            break
        else:
            print("Error, pilihan kamu gada bro!\n")
menu()