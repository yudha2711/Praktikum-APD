nama = str(input("Masukkan nama Anda: "))
hari = str(input("Masukkan nama hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): "))
uang = int(input("Masukkan jumlah uang yang Anda miliki: Rp "))


harga_tiket = {
    'Senin': 40000,
    'Selasa': 40000,
    'Rabu': 40000,
    'Kamis': 40000,
    'Jumat': 45000,
    'Sabtu': 55000,
    'Minggu': 60000
}

if hari in harga_tiket:
    if uang <= harga_tiket[hari]:
        print(f"Maaf uang yang anda miliki tidak cukup,silahkan periksa kembali pemesanan tiket anda dan pastikan uang yang anda miliki cukup")
    else:
        print(f"Selamat,Pembelian Tiket berhasil! silahkan cek kembali tiket anda di hari{hari}.")
else:
    print("Hari yang Anda masukkan tidak valid. Silakan masukkan hari yang benar.")
