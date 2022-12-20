txt = 'Hello World'
print(txt)

# Hitung jumlah karakternya
print(len(txt))

# Ambil karakter terakhir
print(txt[-1])

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print(txt[2:5])

# Hilangkan spasi pada text tersebut (HelloWorld)
print(txt.lstrip())

# Ubah text menjadi huruf besar
print(txt.upper())

# Ubah text menjadi huruf kecil
print (txt.lower())

# Ganti karakter H dengan karakter J
print (txt.replace('H','J'))