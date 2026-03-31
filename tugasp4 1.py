# Input
x = int(input("Masukkan jumlah hari: "))

# Proses 
tahun = x // 365
sisa = x % 365

bulan = sisa // 30
hari = sisa % 30

# Output 
print("Hasil konversi:")
print(tahun, "tahun,", bulan, "bulan,", hari, "hari")