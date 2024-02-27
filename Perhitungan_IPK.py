mata_kuliah = ["Algoritma", "Perancangan Objek", "Kalkulus", "Etika Profesi", "Databases", "English 1"]
sks = [3, 3, 4, 2, 3, 3]

total_sks = 0
total_nilai = 0

for i in range(len(mata_kuliah)):
    nilai = float(input(f"Masukkan nilai {mata_kuliah[i]}: "))
    total_nilai += nilai * sks[i]
    total_sks += sks[i]

ipk = total_nilai / total_sks

print("IPK semester ini adalah:", ipk)