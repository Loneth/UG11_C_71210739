# Odilio Ganesha Nugroho - 71210739
# Unguided 11 Grup C Soal 1

def nilai(joko):
    print("Nilai Tertinggi adalah: ", max(joko))
    print("Nilai Terendah adalah: ", min(joko))
    print("Rata-ratanya adalah: ", '{:.2f}'.format(sum(joko) / len(joko)), "\n")

    return sorted(joko)

daftar_nilai1 = [10,40,30,53,50]
daftar_nilai2 = [99,78,89,85,46]
daftar_nilai3 = [57,90,76,85,78]
print(nilai(daftar_nilai1))
