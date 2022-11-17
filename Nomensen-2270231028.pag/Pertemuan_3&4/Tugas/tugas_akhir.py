# Halaman 57 Modul Praktikum Algoritma Pemrograman
# Create by Nomensen-2270231028


print("Selamat Datang di POM Bensin")
nama = input("Masukan Nama Anda: ")
tanggal = input("Tanggal Pembelian: ")
alamat = input("Masukan Alamat Anda: ")
telpon = input("Masuk No.Telp Anda: ")

def fungsilist():
    global totalbeli
    global jumlah
    global ltr
    print ("\n-----List Bahan Bakar-----\n")
    print("1. Pertalite = Rp 10.000/Liter")
    print("2. Pertamax = Rp 15.000/Liter")
    print("3. Pertamax Turbo = Rp 17.000/Liter")
    nomor=int(input("Masukan Pilihan: "))
    jumlah=int(input("Berapa Liter: "))
    
    if nomor==1:
       totalbeli=jumlah*10000
       print (jumlah," Liter Pertalite = Rp", totalbeli)
       ltr=("Liter Pertalite")
    elif nomor==2:
       totalbeli=jumlah*15000
       print (jumlah," Liter Pertamax = Rp", totalbeli)
       ltr=("Liter Pertamax")
    elif nomor==3:
       totalbeli=jumlah*17000
       print (jumlah, " Liter Pertamax Turbo = Rp", totalbeli)
       ltr=("Liter Pertamax Turbo")
    else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
fungsilist()

print("\nTotal harus Dibayar: Rp",totalbeli)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalbeli)
print("Kembalian :",kembalian)

print("==========Bon Pembayaran==========")
print ("Nama\t\t\t\t:",nama)
print ("Alamat\t\t\t\t:",alamat)
print ("Tanggal Pembelian\t\t:",tanggal)
print ("No.Telp\t\t\t\t:",telpon)
print ("Beli\t\t\t\t:",jumlah,ltr,"( Rp", totalbeli,")")
print ("Tagihan\t\t\t\t: Rp",totalbeli)
print ("Dibayar\t\t\t\t: Rp",uang)
print ("Kembalian\t\t\t: Rp",kembalian)
print("==========Terima Kasih=========")