nama = input("Masukan nama anda: ")
tempat_lahir = input ("Masukan tempat lahir anda: ")
tanggal_lahir = int(input("Masukan tanggal lahir anda: "))
bulan_lahir = int(input("Masukan bulan lahir anda: "))
tahun_lahir = int(input("Masukan tahun lahir anda: "))
nilai_inggris = float(input("Masukan nilai inggris anda: "))
nilai_mtk = float(input("Masukan nilai mtk anda: "))
nilai_indonesia = float(input("Masukan nilai Indonesia anda: "))
jenis_kelamin = input("Masukan jenis kelamin anda: ")

rata_rata = (nilai_inggris + nilai_mtk + nilai_indonesia) /3

tahun_sekarang = 2024
usia = tahun_sekarang - tahun_lahir

if rata_rata >= 80:
    if jenis_kelamin == "laki-laki":
        jurusan = "Teknik Informatika"
    elif jenis_kelamin == "perempuan":
        jurusan = "Sistem informasi" 
    else:
        jurusan = "DKV"      
else:
        jurusan = "DKV"  

if usia < 25:
     diterima = True
else: 
     diterima = False  

if diterima:
     print("Selamat, anda ditwrima di jurusan", jurusan) 
else:
     print("maaf, umur anda tidak memenuhi syarat untuk mendafftar.")                   




