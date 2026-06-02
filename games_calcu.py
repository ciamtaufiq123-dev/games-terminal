print("======================================")
print("Selamat Datang Di Games Mini Terminal!")
print("======================================")

nama = input("Masukkan nama Anda :")
print(f"Halo {nama}, selamat datang di games mini terminal, semoga kamu betah yaa!\n")

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
        print("gabisa bro, input cuma bisa angka aja ya!\n")
def main_tebakan():
    import random
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
def main_kalkulator():
    while True:
        print("==kalkulator_sederhana==")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan Anda :\n"))
        except ValueError:
            print("gabisa bro, input harus angka ya!\n")
            continue
        if pilihan == 1:
            operasi("+")
        elif pilihan == 2:
            operasi ("-")
        elif pilihan == 3:
            operasi("*")
        elif pilihan == 4:
            operasi("/")
        elif pilihan == 5:
            print("Terima kasih telah berkunjung ya!\n")
            break
        else:
            print("Error, pilihan kamu gada bro!\n")
def menu():
    while True:
        print("=====Menu=====")
        print("1. Mulai Tebakan")
        print("2. Kalkukator Sederhana")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan Anda :"))
        except ValueError:
            print("gabisa bro, input cuma bisa angka saja ya!\n")
            continue
        if pilihan == 1:
            main_tebakan()
        elif pilihan == 2:
            main_kalkulator()
        elif pilihan == 3:
            print("Terima kasih telah berkunjung ya!\n")
            break
        else:
            print("Error, pilihan kamu gada bro!\n")
menu()