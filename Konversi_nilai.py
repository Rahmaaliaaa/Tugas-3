nilai = float(input("Masukkan nilai Anda: "))

if nilai < 50:
    konversi = 'E'
elif 50 <= nilai < 60:
    konversi = 'D'
elif 60 <= nilai < 70:
    konversi = 'C'
elif 70 <= nilai < 80:
    konversi = 'B'
else:
    konversi = 'A'

print("Konversi nilai anda:", konversi)