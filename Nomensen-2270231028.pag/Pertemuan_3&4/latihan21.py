# Halaman 56 Modul Praktikum Algoritma Pemrograman
# Create by Nomensen-2270231028

# Contoh penggunaan Nested Loop
# Catatan: Penggunaan moduLo pada kondisional mengasumsikan nilai selain 0 sebagai True (benar) dan nol sebagai False (Salah)

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not (i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime ")
    i = i + 1

print("Good bye !")