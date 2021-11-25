# Odilio Ganesha Nugroho - 71210739
# Unguided 11 Grup C Soal 2

def check_data_type(a, b):
    a = a.__class__.__name__
    b = b.lower()

    if a == b:
        print("Jawaban Anda benar")
        return True

    print("Jawaban Anda salah, seharusnya adalah: ", a)
    return False


print(check_data_type(True,"Bool"))
print(check_data_type(True,"bool"))
print(check_data_type({},"TUPLE"))
print(check_data_type({},"DIct"))
print(check_data_type([],""))
