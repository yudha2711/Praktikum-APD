NAMA = "Abhista Fijri Yudhanta Maulana"
NIM = "2409106103"
Harga_gula = 21000

Diskon_gulaku = 0.07
Diskon_manis_kita = 0.11
Diskon_gunung_madu = 0.13

Diskon_gulaku = Harga_gula * Diskon_gulaku
Diskon_manis_kita = Harga_gula * Diskon_manis_kita
Diskon_gunung_madu = Harga_gula * Diskon_gunung_madu

harga_setelah_diskon_gulaku = Harga_gula - Diskon_gulaku
harga_setelah_diskon_manis_kita = Harga_gula - Diskon_manis_kita
harga_setelah_diskon_gunung_madu = Harga_gula - Diskon_gunung_madu

print(f"{NAMA} dengan NIM) ingin membeli gula seharga Rp {Harga_gula}")
print(f"jika dia membeli gulaku maka dia harus membayar {harga_setelah_diskon_gulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli manis kita maka dia  harus membayar {harga_setelah_diskon_manis_kita} setelah mendapat diskon 11%")
print(f"jika dia membeli gunung madu maka dia harus membayar {harga_setelah_diskon_gunung_madu} setelah mendapat diskon 13%")