def operasi(operasi_str):
    try:
        angka1 = float(input("Masukkan Angka ke 1 :"))
        angka2 = float(input("Masukkan Angka ke 2 :"))
        if operasi_str == "/" and angka2 == 0:
            print("Error, Pembagian tidak boleh dengan 0\n")
            return
        hasil = eval(f"{angka1} {operasi_str} {angka2}\n")
        print(hasil)
    except ValueError:
        print("gabisa bro, input harus angka ya!\n")
        
def main():
    nama = input("Masukkan nama Anda :")
    print(f"Selamat datang {nama} di kalkulator sederhana ini\n")
    menu(nama)
        
def menu(nama):
    while True:
        print("=====Menu_Kalkulator_Sederhana=====")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan Anda :"))
        except ValueError:
            print(f"Error, pilihan {nama} harus angka 1-5 ya bro!\n")
            continue
        if pilihan == 1:
            operasi("+")
        elif pilihan == 2:
            operasi("-")
        elif pilihan == 3:
            operasi("*")
        elif pilihan == 4:
            operasi("/")
        elif pilihan == 5:
            print(f"Terima kasih {nama} telah menggunakan kalkulator sederhana ini\n")
            break
        else:
            print(f"Error, pilihan {nama} gada di menu bro!\n")
            
main()