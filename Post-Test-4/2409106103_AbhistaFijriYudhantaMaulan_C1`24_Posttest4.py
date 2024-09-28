attempts = 0
while attempts < 3 :

     username = input("Masukkan username anda :")
     password = int(input("Masukkan pasword :"))
     if username == "Yudha" and password == 103:
        lanjut = print("Kelazz abangkuh mau lanjut ata ga nich?")
        if lanjut == "berhenti" :
            print("program sudah di hentikan")
        else :
            print("Berhasil masuk yaa kakak :D") 
        hari = input("Ingin beli tiket di hari apa?")
        uang = int(input("Masukkan Jumlah Uangnya kak"))
        if hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis" :
            if uang >= 40000:
                print(f"Yuhuu berhasil beli tiketnya di hari {hari} kak")
            else:
                print(f"umm uangnya ga cukup kak hehe..")
                break
        elif hari == "Jumat" :
            if uang >= 45000 :
                print(f"Yuhuu berhasil beli tiketnya di hari {hari} kak")
            else:
                print(f"umm uangnya ga cukup kak hehe..")
                break
        elif hari == "Sabtu" :
            if uang >=55000 :
                print(f"Yuhuu berhasil beli tiketnya di hari {hari} kak")
            else :
                print(f"umm uangnya ga cukup kak hehe..")
                break
        elif hari == "Minggu" :
            if uang >= 60000 :
                print(f"Yuhuu berhasil beli tiketnya di hari {hari} kak")
            else:
                print(f"umm uangnya ga cukup kak hehe..")
                break
        else:
            print(f"hari yang anda masukkan ga jelas!")
            break
else:
        print("Username atau passwordnya salah kak coba lagi awokawok!")
        lanjut = input("Mau lanjut atau ga nich?")
        if lanjut == "berhenti" :
            print("programnya berhenti kak :(")
        else :
            attempts += 1
            print(f"Akses ditolak kak udah gagal {attempts}")