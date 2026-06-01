def penjumlahan():
    try:
        print("========Penjumlahan_Sederhana=========")
        angka1 = float(input("Masukkan Angka ke 1 :"))
        angka2 = float(input("Masukkan angka ke 2 :"))
        
        hasil = angka1 + angka2
        print(f"hasil {angka1} + {angka2} = {hasil}")
    except ValueError:
        print("Error: Masukkan Angka saja ya broo!\n")
    
    
def pengurangan():
    try:
        print("========Pengurangan_Sederhana=========")
        angka3 = float(input("Masukkan angka ke 3 :"))
        angka4 = float(input("Masukkan angka ke 4 :"))
        
        hasil = angka3 - angka4
        print(f"hasil {angka3} - {angka4} = {hasil}")
    except ValueError:
        print("Error: Masukkan angka saja ya bro!\n")
    
    
def perkalian():
    try:
        print("========Perkalian_Sederhana=========")
        angka5 = float(input("Masukkan angka ke 5 :"))
        angka6 = float(input("Masukkan angka ke 6 :"))
        
        hasil = angka5 * angka6
        print(f"hasil {angka5} * {angka6} = {hasil}")
    except ValueError:
        print("Error: Masukkan angka saja ya bro!\n")

    
def pembagian():
    try:
        print("========Pembagian_Sederhana=========")
        angka7 = float(input("Masukkan angka ke 7 :"))
        angka8 = float(input("Masukkan angka ke 8 :"))
    except ValueError:
        print("Error: Masukkan angka saja ya bro!\n")
    try:
        hasil = angka7 / angka8
        print(f"hasil {angka7} / {angka8} = {hasil}")
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan!\n")
        
def menu():
    while True:
        print("========Menu_Kalkulator_Sederhana=========")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
    
        try:
            pilihan_user = int(input("Masukkan pilihan Anda :"))
        except ValueError:
            print("Error: pilihan harus angka 1-5 aja ya bro!\n")
            continue
    
        if pilihan_user == 1:
            penjumlahan()
        elif pilihan_user == 2:
            pengurangan()
        elif pilihan_user == 3:
            perkalian()
        elif pilihan_user == 4:
            pembagian()
        elif pilihan_user == 5:
            print("Terima kasih telah menggunakan kalkulator sederhana kami :)")
            break
        else:
            print("pilihan yang Anda masukkan tidak ada di dalam menu")
        
menu()