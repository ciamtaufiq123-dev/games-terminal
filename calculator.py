nama_user = input("Masukkan nama Anda: ")
print(f"=====halo {nama_user}, selamat datang di program kalkulator sederhana====")

pilihan_user = input("Apakah Anda ingin lanjut ke pembelajaran ? (y/n) :")

if pilihan_user == "y":
    print("Anda memilih untuk lanjut ke pembelajaran.")
elif pilihan_user == "n":
    print("Anda tidak ingin melanjutkan pembelajaran, terimakasih.")
    exit()

#penjumlahan sederhana
print("==========Penjumlahan Sederhana==========")

angka1 = int(input("Masukkan Angka ke 1 :"))
angka2 = int(input("Masukkan Angka ke 2 :"))

hasil = angka1 + angka2

print("Ini adalah Hasilnya :", hasil)

pilihan1 = input("Apakah Anda ingin lanjut ke pengurangan sederhana ? (y/n) :")

if pilihan1 == "y":
    print("Anda memilih untuk lanjut ke pengurangan sederhana.")
elif pilihan1 == "n":
    print("Anda tidak ingin melanjutkannya.")
    exit()

#pengurangan sederhana
print("==========Pengurangan Sederhana==========")

angka3 = int(input("Masukkan Angka Ke 3 :"))
angka4 = int(input("Masukkan Angka Ke 4 :"))

hasil = angka3 - angka4
print("Ini adalah Hasilnya :", hasil)

pilihan2 = input("Apakah Anda ingin melanjutkan ke perkalian sederhana ? (y/n) :")

if pilihan2 == "y":
    print("Anda memilih untuk lanjut ke perkalian sederhana.")
elif pilihan2 == "n":
    print("Anda memilih untuk tidak melanjutkannya.")
    exit()

#perkalian sederhana
print("==========Perkalian Sederhana==========")

angka5 = int(input("Masukkan Angka Ke 5 :"))
angka6 = int(input("Masukkan Angka Ke 6 :"))

hasil = angka5 * angka6

print("Ini adalah Hasilnya :", hasil)

pilihan3 = input("Apakah Anda ingin melanjutkan ke pembagian sederhana ? (y/n) :")

if pilihan3 == "y":
    print("Anda memilih untuk lanjut ke pembagian sederhana.")
elif pilihan3 == "n":
    print("Anda tidak ingin lanjut ke pembagian sederhana.")
    exit()

#pembagian sederhana
print("==========Pembagian Sederhana==========")

angka7 = int(input("Masukkan Angka Ke 7 :"))
angka8 = int(input("Masukkan Angka Ke 8 :"))

hasil = angka7 / angka8

print("Ini adalah Hasilnya :", hasil)

