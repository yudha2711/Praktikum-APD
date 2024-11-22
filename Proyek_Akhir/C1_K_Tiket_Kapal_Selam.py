import pandas as pd   #Buat Dataframes
import os   #untuk mengelola sistem files
from tabulate import tabulate  #format data dalam bentuk tabel
from datetime import datetime   #menangani waktu dan tanggal.
from colorama import Fore, Style, init  #memberi warna dan style pada teks

#untuk warna
init()

#fungsi untuk membersihkan layar
def clear():
    os.system('cls || clear')


#fungsi untuk login
def login():
    while True:
        try:
            #baca data csv
            Dfuser = pd.read_csv('users.csv') 
            username = input("Masukkan username: ").strip()
            if not username:
                raise ValueError(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
            
            password = input("Masukkan password: ").strip()
            if not password:
                raise ValueError(Fore.RED + "Password tidak boleh kosong!" + Style.RESET_ALL)
            
            #cek apakah username dan password cocok
            user = Dfuser[(Dfuser['username'] == username) & (Dfuser['password'] == password)]
            
            if not user.empty:
                return username, user.iloc[0]['role']
            print(Fore.RED + "Username atau password salah!" + Style.RESET_ALL)
        except ValueError as e:
            print(e)
        input("Tekan Enter untuk melanjutkan...")

#fungsi untuk register
def register():
    try:
        Dfuser = pd.read_csv('users.csv')
        print("\n=== REGISTER ===")
        username = input("Masukkan username baru: ").strip()
        if not username:
            raise ValueError(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
        
        #cek apakah username sudah ada
        if username in Dfuser['username'].values:
            raise ValueError(Fore.RED + "Username sudah digunakan!" + Style.RESET_ALL)
        
        password = input("Masukkan password: ").strip()
        if not password:
            raise ValueError(Fore.RED + "Password tidak boleh kosong!" + Style.RESET_ALL)
        
        #tambah user baru sebagai pengguna biasa
        User_baru = pd.DataFrame({
            'username': [username],
            'password': [password],
            'role': ['user']
        })
        Dfuser = pd.concat([Dfuser, User_baru], ignore_index=True)
        Dfuser.to_csv('users.csv', index=False)
        input(Fore.GREEN + "Registrasi berhasil! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan...")

#fungsi untuk menampilkan tiket
def Tiket():
    Dftiket = pd.read_csv('tiket.csv')
    if Dftiket.empty:
        print(Fore.YELLOW + "Tidak ada tiket tersedia" + Style.RESET_ALL)
    else:
        print("\\nDaftar Tiket:")
        print(tabulate(Dftiket, headers='keys', tablefmt='grid', showindex=True))
#fungsi untuk menambah tiket
def add_ticket():
    try:
        tujuan = input("Masukkan tujuan: ").strip()
        if not tujuan:
            raise ValueError(Fore.RED + "Tujuan tidak boleh kosong!" + Style.RESET_ALL)
        
        while True:
            kelas = input("Masukkan kelas (business/first/vip): ").strip().lower()
            if not kelas:
                raise ValueError(Fore.RED + "Kelas tidak boleh kosong!" + Style.RESET_ALL)
            if kelas in ['business', 'first', 'vip']:
                break
            print(Fore.RED + "Kelas tidak valid!" + Style.RESET_ALL)
        
        Harga_Input = input("Masukkan harga: ").strip()
        if not Harga_Input:
            raise ValueError(Fore.RED + "Harga tidak boleh kosong!" + Style.RESET_ALL)
        if not Harga_Input.isdigit():
            raise ValueError(Fore.RED + "Harga harus berupa angka!" + Style.RESET_ALL)
        harga = int(Harga_Input)
        
        Stok_Input = input("Masukkan stok: ").strip()
        if not Stok_Input:
            raise ValueError(Fore.RED + "Stok tidak boleh kosong!" + Style.RESET_ALL)
        if not Stok_Input.isdigit():
            raise ValueError(Fore.RED + "Stok harus berupa angka!" + Style.RESET_ALL)
        stok = int(Stok_Input)
        
        Dftiket = pd.read_csv('tiket.csv')
        Tiket_Baru = pd.DataFrame({
            'tujuan': [tujuan],
            'kelas': [kelas],
            'harga': [harga],
            'stok': [stok]
        })
        Dftiket = pd.concat([Dftiket, Tiket_Baru], ignore_index=True)
        Dftiket.to_csv('tiket.csv', index=False)
        input(Fore.GREEN + "Tiket berhasil ditambahkan! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan...")

#fungsi untuk memperbarui tiket
def Ubah_Tiket():
    try:
        Tiket()
        Dftiket = pd.read_csv('tiket.csv')
        if Dftiket.empty:
            raise ValueError(Fore.YELLOW + "Tidak ada tiket untuk diperbarui!" + Style.RESET_ALL)
        
        Nomor = input(f"Masukkan nomor tiket yang akan diperbarui (0-{len(Dftiket)-1}): ").strip()
        if not Nomor:
            raise ValueError(Fore.RED + "Nomor tiket tidak boleh kosong!" + Style.RESET_ALL)
        if not Nomor.isdigit():
            raise ValueError(Fore.RED + "Nomor tiket harus berupa angka!" + Style.RESET_ALL)
        
        index = int(Nomor)
        if index < 0 or index >= len(Dftiket):
            raise ValueError(Fore.RED + "Nomor tiket tidak valid!" + Style.RESET_ALL)
        
        #ambil data tiket
        Tiket_Sekarang = Dftiket.iloc[index]
        
        #data baru
        tujuan = input("Masukkan tujuan baru (kosongkan jika tidak diubah): ").strip()
        kelas = input("Masukkan kelas baru (business/first/vip) (kosongkan jika tidak diubah): ").strip().lower()
        Harga_Input = input("Masukkan harga baru (kosongkan jika tidak diubah): ").strip()
        Stok_Input = input("Masukkan stok baru (kosongkan jika tidak diubah): ").strip()
        
        #pakai data lama jika input kosong
        tujuan_baru = tujuan if tujuan else Tiket_Sekarang['tujuan']
        kelas_baru = kelas if kelas in ['business', 'first', 'vip'] else Tiket_Sekarang['kelas']
        
        
        if Harga_Input:
            if not Harga_Input.isdigit():
                raise ValueError(Fore.RED + "Harga harus berupa angka!" + Style.RESET_ALL)
            harga_baru = int(Harga_Input)
        else:
            harga_baru = Tiket_Sekarang['harga']
        
        
        if Stok_Input:
            if not Stok_Input.isdigit():
                raise ValueError(Fore.RED + "Stok harus berupa angka!" + Style.RESET_ALL)
            Stok_Baru = int(Stok_Input)
        else:
            Stok_Baru = Tiket_Sekarang['stok']
        
        #update tiket
        Dftiket.loc[index] = [tujuan_baru, kelas_baru, harga_baru, Stok_Baru]
        Dftiket.to_csv('tiket.csv', index=False)
        input(Fore.GREEN + "Tiket berhasil diperbarui! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan...")

#fungsi untuk menghapus tiket
def Hapus_Tiket():
    try:
        Tiket()
        Dftiket = pd.read_csv('tiket.csv')
        if Dftiket.empty:
            raise ValueError(Fore.YELLOW + "Tidak ada tiket untuk dihapus!" + Style.RESET_ALL)
        
        Nomor = input(f"Masukkan nomor tiket yang akan dihapus (0-{len(Dftiket)-1}): ").strip()
        if not Nomor:
            raise ValueError(Fore.RED + "Nomor tiket tidak boleh kosong!" + Style.RESET_ALL)
        if not Nomor.isdigit():
            raise ValueError(Fore.RED + "Nomor tiket harus berupa angka!" + Style.RESET_ALL)
        
        index = int(Nomor)
        if index < 0 or index >= len(Dftiket):
            raise ValueError(Fore.RED + "Nomor tiket tidak valid!" + Style.RESET_ALL)
        
        Dftiket = Dftiket.drop(index)
        Dftiket.to_csv('tiket.csv', index=False)
        input(Fore.GREEN + "Tiket berhasil dihapus! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan...")

#fungsi untuk membeli tiket
def Beli_Tiket(username):
    try:
        Tiket()
        Dftiket = pd.read_csv('tiket.csv')
        if Dftiket.empty:
            raise ValueError(Fore.YELLOW + "Tidak ada tiket tersedia untuk dibeli!" + Style.RESET_ALL)
        
        Nomor = input(f"Masukkan nomor tiket yang akan dibeli (0-{len(Dftiket)-1}): ").strip()
        if not Nomor:
            raise ValueError(Fore.RED + "Nomor tiket tidak boleh kosong!" + Style.RESET_ALL)
        if not Nomor.isdigit():
            raise ValueError(Fore.RED + "Nomor tiket harus berupa angka!" + Style.RESET_ALL)
        
        index = int(Nomor)
        if index < 0 or index >= len(Dftiket):
            raise ValueError(Fore.RED + "Nomor tiket tidak valid!" + Style.RESET_ALL)
        
        if Dftiket.iloc[index]['stok'] > 0:
            #kurangi stok
            Dftiket.loc[index, 'stok'] -= 1
            Dftiket.to_csv('tiket.csv', index=False)
            
            #catat transaksi
            DFtransaksi = pd.read_csv('transaksi.csv') #baca file csv
            TransaksiBaru = pd.DataFrame({
                'username': [username],
                'tujuan': [Dftiket.iloc[index]['tujuan']],
                'kelas': [Dftiket.iloc[index]['kelas']],
                'harga': [Dftiket.iloc[index]['harga']],
                'tanggal': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            }) #masukkan kee dataframe
            DFtransaksi = pd.concat([DFtransaksi, TransaksiBaru], ignore_index=True) #menggabungkan data baru
            DFtransaksi.to_csv('transaksi.csv', index=False) #mengubah data ke csv
            input(Fore.GREEN + "Pembelian tiket berhasil! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
        else:
            raise ValueError(Fore.RED + "Maaf, tiket sudah habis!" + Style.RESET_ALL)
    
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan...")

#riwayat pembelian
def Riwayat_Pembelian(username):
    DFtransaksi = pd.read_csv('transaksi.csv')
    Transaksi = DFtransaksi[DFtransaksi['username'] == username]
    if Transaksi.empty:
        print(Fore.YELLOW + "Belum ada riwayat pembelian" + Style.RESET_ALL)
    else:
        print("\\nRiwayat Pembelian:")
        print(tabulate(Transaksi, headers='keys', tablefmt='grid', showindex=False))
    input("\\nTekan Enter untuk melanjutkan...")

#menu admin
def admin_menu():
    while True:
        clear()
        
        # Lebar tabel
        width = 30
        
        # Header
        print("╔" + "═" * (width) + "╗")
        print("║" + " " * ((width - 10) // 2) + "MENU ADMIN" + " " * ((width - 10) // 2) + "║")
        print("╠" + "═" * (width) + "╣")
        # Menu Items
        Bagian_Menu = [
            "1. Lihat Tiket",
            "2. Tambah Tiket",
            "3. Perbarui Tiket",
            "4. Hapus Tiket",
            "5. Keluar"
        ]
        
        for item in Bagian_Menu:
            padding = width - len(item)  #hitung padding untuk meratakan teks di tengah
            print("║" + " " * (padding // 2) + item + " " * (padding - padding // 2) + "║")
        
        # Footer
        print("╚" + "═" * (width) + "╝")
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            Tiket()
            input("\nTekan Enter untuk melanjutkan...")
        elif choice == '2':
            add_ticket()
        elif choice == '3':
            Ubah_Tiket()
        elif choice == '4':
            Hapus_Tiket()
        elif choice == '5':
            break
        else:
            input(Fore.RED + "Menu tidak valid! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)

#menu user
def user_menu(username):
    while True:
        clear()
        
        width = 30
        
        print("╔" + "═" * (width) + "╗")
        print("║" + " " * ((width - 10) // 2) + "MENU USER" + " " * ((width - 10) // 2) + "║")
        print("╠" + "═" * (width) + "╣")
        
        menu_items = [
            "1. Lihat Tiket Tersedia",
            "2. Beli Tiket",
            "3. Riwayat Pembelian",
            "4. Keluar"
        ]
        
        for item in menu_items:
            padding = width - len(item)
            print("║" + " " * (padding // 2) + item + " " * (padding - padding // 2) + "║")
        
        print("╚" + "═" * (width) + "╝")
        
        choice = input("Pilih menu (1-4): ")
        
        if choice == '1':
            Tiket()
            input("\nTekan Enter untuk melanjutkan...")
        elif choice == '2':
            Beli_Tiket(username)
        elif choice == '3':
            Riwayat_Pembelian(username)
        elif choice == '4':
            break
        else:
            input(Fore.RED + "Menu tidak valid! Tekan Enter untuk melanjutkan..." + Style)

def main():
    while True:
        clear()
        
        width = 35
        
        print("╔" + "═" * width + "╗")
        print("║" + "SISTEM TIKET KAPAL SELAM".center(width) + "║")
        print("╠" + "═" * width + "╣")
        
        menu_items = [
            "1. Login",
            "2. Register",
            "3. Keluar"
        ]
        
        for item in menu_items:
            print("║" + item.center(width) + "║")
        
        # Footer
        print("╚" + "═" * width + "╝")

        choice = input("\nPilih menu (1-3): ").strip()
        
        if choice == '1':
            username, role = login()
            if role == 'admin':
                admin_menu()
            else:
                user_menu(username)
        elif choice == '2':
            register()
        elif choice == '3':
            print(Fore.GREEN + "Terima kasih telah menggunakan sistem kami!" + Style.RESET_ALL)
            break
        else:
            input(Fore.RED + "Menu tidak valid! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()