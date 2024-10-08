import os
akuns = []

while True:
    print("Hiii! Welcome to resto manuk akal!")
    print("ayokd daftar akun dulu yaa,kalau sudah otw login!")
    print("1. buat akun kaks")
    print("2. Login nich")
    print("3. Exit :(")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Heyyo yuk daftar dulu!")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
           print("waduh udh ada yang pake namanya,yuk coba lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  
            print(f"Sip deh akun udh terdaftar! ID: {Username}")
 

    elif opsi == "2":
        print("heyyo!,kuy login dulu!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
                    print(f"\nwelkam to mebel lejen! {Username}!")
                    print("―――SYILAHKAN PUH!―――")
                    print("1. Reservasi Meja")
                    print("2. nak tengok reservasi")
                    print("3. nak ubah meja")
                    print("4. nak hapus reservasi")
                    print("5. KELUAR!")
                    print("―――――――――――――――――――――――――――――")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        nama = int(input("nama reservasi: "))
                        hari = str(input("Hari Reservasi: "))
                        akun[2].append([nama, hari])  
                        print("yeessh mejanya udh di reservasi!\n")

                    elif status == "2":
                        for indeks, note in enumerate(akun[2]):  
                            print(f"{indeks + 1}. nama {note[1]}\hari: {note[1]}\n")
                        if not akun[2]:
                            print("ups kamu belum reservasi,yuk reservasi dulu\n")

                    elif status == "3":
                        if not akun[2]:
                            print("tidak ada meja yang di reservasi kak.")
                        else:
                            edit = int(input("Meja nomor berapa: ")) - 1
                            if 0 <= edit < len(akun[2]):
                                nama= int(input("Nomor Meja: "))
                                hari = str(input("Jangan lupa masukkan harinya:"))
                                print("yakin nih ganti reservasi?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    akun[2][edit] = [nama, hari]  
                                    print("yeay meja berhasil di ubah!!\n")
                                elif memastikan_edit == "2":
                                    print("edit reservasi dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("ga ada meja yang disebut,coba input ulang.\n")
                    
                    elif status == "4":
                        if not akun[2]:
                            print("ga ada meja yg di hapus.")
                        else:
                            hapus = int(input("hapus reservasi meja nomor?: ")) 
                            if 0 <= hapus < len(akun[2]):
                                print(f"yakin mau hapus? ")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del akun[2][hapus]  
                                    print("reservasi meja dihapus!\n")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("yee salah lagi luu kocak,ulang sono!\n")

                    elif status == "5":
                        print("DADAH DEEK.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")