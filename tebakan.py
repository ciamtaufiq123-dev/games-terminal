import random

def tebakan():
    angka_acak = random.randint(1, 10)
    print("selamat datang di permainan tebakan angka!")
    
    tebakan_me = 0
    
    while tebakan_me != angka_acak:
        try:
            tebakan_me = int(input("tebak angka antara 1-10 :"))
        except ValueError:
            print("gabisa bro, input cuma bisa nagka aja!\n")
            continue
        if tebakan_me < angka_acak:
            print("tebakan kamu terlalu kecil bro!\n")
        elif tebakan_me > angka_acak:
            print("tebakan kamu terlalu besar bro!\n") 
        else:
            print("wah selamat bro tebakan kamu benar, ada di angka ", angka_acak)
            break
def menu():
    while True:
        print("===Menu_Tebak_Angka===")
        print("1. Mulai Tebakan")
        print("2. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan Anda :\n"))
        except ValueError:
            print("gabisa bro, input cuma bisa angka aja!\n")
            continue
        if pilihan == 1:
            tebakan()
        elif pilihan == 2:
            print("terima kasih sudah telah mampir bro\n")
        else:
            print("Error, pilihan kamu gada bro!\n")
menu()