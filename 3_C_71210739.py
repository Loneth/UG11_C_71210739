# Odilio Ganesha Nugroho - 71210739
# Unguided 11 Grup C Soal 3

def ambil_dan_sisipkan(a1, b1=1, c1=2):
    kata = list(a1)
    return print(a1 + kata[b1 - 1] + kata[c1 - 1])


a = input("Masukan Kalimat: ")
b = input("Masukan Index 1: ")
c = input("Masukan Index 2: ")

ambil_dan_sisipkan(a, int(b), int(c))
