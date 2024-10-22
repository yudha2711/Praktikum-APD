# Variabel global
akuns = {}
max_meja = 10

def main():
    while True:
        try:
            print("Hiii! Welcome to resto manuk akal!")
            print("ayokd daftar akun dulu yaa, kalau sudah otw login!")
            print("1. buat akun kaks")
            print("2. Login nich")
            print("3. Exit :(")
            print("――――――――――――――――――――――――")
            opsi = input("Pilih opsi: ")
            print(" ")

            if opsi == "1":
                buat_akun()  # Prosedur untuk membuat akun

            elif opsi == "2":
                login()  # Prosedur untuk login

            elif opsi == "3":
                print("Terima kasih sudah datang!")
                break

            else:
                print("Input tidak valid, coba lagi!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def buat_akun():
    """Prosedur untuk membuat akun"""
    global akuns  # Menggunakan variabel global
    print("Heyyo yuk daftar dulu!")
    Username = input("Username: ")
    if Username in akuns:  # Memeriksa apakah username sudah ada
        print("waduh udh ada yang pake namanya,yuk coba lagi")
    else:
        Password = input("Password: ")
        akuns[Username] = {"password": Password, "reservasi": []}  # Variabel lokal "Password"
        print(f"Sip deh akun udh terdaftar! ID: {Username}")

def login():
    """Prosedur untuk login ke akun"""
    global akuns  # Menggunakan variabel global
    print("heyyo!,kuy login dulu!")
    Username = input("Username: ")
    Password = input("Password: ")
    if Username in akuns and akuns[Username]["password"] == Password:
        menu_reservasi(Username)  # Fungsi dengan parameter
    else:
        print("Username dan password anda salah, silahkan coba lagi\n")

def menu_reservasi(Username):
    """Fungsi utama menu reservasi"""
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
            reservasi_meja(Username)  # Fungsi dengan parameter
        elif status == "2":
            lihat_reservasi(Username)  # Fungsi dengan parameter
        elif status == "3":
            ubah_reservasi(Username)  # Fungsi dengan parameter
        elif status == "4":
            hapus_reservasi(Username)  # Fungsi dengan parameter
        elif status == "5":
            print("DADAH DEEK.\n")
            break
        else:
            print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")

def reservasi_meja(Username):
    """Fungsi untuk menambah reservasi meja"""
    global max_meja  # Menggunakan variabel global
    try:
        nama = int(input("Nomor Meja: "))
        hari = input("Hari Reservasi: ")
        if nama <= 0 or nama > max_meja:
            raise ValueError("Nomor meja tidak valid.")
        akuns[Username]["reservasi"].append([nama, hari])  # Variabel lokal "nama" dan "hari"
        print("yeessh mejanya udh di reservasi!\n")
    except ValueError as ve:
        print(f"Input tidak valid: {ve}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def lihat_reservasi(Username):
    """Fungsi untuk melihat daftar reservasi"""
    if akuns[Username]["reservasi"]:
        for indeks, note in enumerate(akuns[Username]["reservasi"]):  
            print(f"{indeks + 1}. nama {note[0]}, hari: {note[1]}\n")
    else:
        print("ups kamu belum reservasi,yuk reservasi dulu\n")

def ubah_reservasi(Username):
    """Fungsi untuk mengubah reservasi yang sudah ada"""
    if not akuns[Username]["reservasi"]:
        print("tidak ada meja yang di reservasi kak.")
    else:
        try:
            edit = int(input("Meja nomor berapa: ")) - 1
            if 0 <= edit < len(akuns[Username]["reservasi"]):
                nama = int(input("Nomor Meja: "))
                hari = input("Jangan lupa masukkan harinya: ")
                konfirmasi_edit(Username, edit, nama, hari)  # Fungsi rekursif
            else:
                print("ga ada meja yang disebut, coba input ulang.\n")
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.\n")

def konfirmasi_edit(Username, edit, nama, hari):
    """Fungsi rekursif untuk konfirmasi perubahan reservasi"""
    print("yakin nih ganti reservasi?")
    print("1. Iya")
    print("2. Tidak")
    memastikan_edit = input("Pilih: ")
    if memastikan_edit == "1":
        akuns[Username]["reservasi"][edit] = [nama, hari]
        print("yeay meja berhasil di ubah!!\n")
    elif memastikan_edit == "2":
        print("edit reservasi dibatalkan")
    else:
        print("Mohon pilih '1' atau '2'")
        konfirmasi_edit(Username, edit, nama, hari)  # Rekursif jika input salah

def hapus_reservasi(Username):
    """Fungsi untuk menghapus reservasi"""
    if not akuns[Username]["reservasi"]:
        print("ga ada meja yg di hapus.")
    else:
        try:
            hapus = int(input("hapus reservasi meja nomor?: ")) - 1
            if 0 <= hapus < len(akuns[Username]["reservasi"]):
                konfirmasi_hapus(Username, hapus)  # Fungsi rekursif
            else:
                print("yee salah lagi luu kocak, ulang sono!\n")
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.\n")

def konfirmasi_hapus(Username, hapus):
    """Fungsi rekursif untuk konfirmasi penghapusan reservasi"""
    print("yakin mau hapus?")
    print("1. Iya")
    print("2. Tidak")
    memastikan_hapus = input("Pilih: ")
    if memastikan_hapus == "1":
        del akuns[Username]["reservasi"][hapus]
        print("reservasi meja dihapus!\n")
    elif memastikan_hapus == "2":
        print("Aksi untuk menghapus dibatalkan")
    else:
        print("Mohon pilih '1' atau '2'")
        konfirmasi_hapus(Username, hapus)  # Rekursif jika input salah

# Memulai program
main()
