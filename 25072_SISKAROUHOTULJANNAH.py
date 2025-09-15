nama = "siska roudhotul jannah"
umur = "19 tahun"  
tinggi = 145  
angka_favorit = 7

# Menampilkan data diri
print("Data Diri:")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi, "cm")
print("Angka Favorit:", angka_favorit)
print()

# Menghitung total harga belanja
harga_pensil = 2000
harga_buku = 5000
jumlah_pensil = 4
jumlah_buku = 2

total_harga = (jumlah_pensil * harga_pensil) + (jumlah_buku * harga_buku)
print("Total Harga Belanja: Rp", total_harga)
print()

# Mengecek apakah angka favorit genap atau ganjil
print("Angka Favorit:")
if angka_favorit % 2 == 0:
    print("angka genap")
else:
    print("angka ganjil")