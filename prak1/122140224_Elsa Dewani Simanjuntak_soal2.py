import math
pi = 3.14

def hitung_luas(jari_jari):
    return pi * jari_jari**2

def hitung_keliling(jari_jari):
    return 2 * pi * jari_jari

if __name__ == "__main__":
    jari_jari = int(input("Masukkan jari-jari lingkaran: "))

    if jari_jari < 0:
        print("Jari-jari lingkaran tidak boleh negatif")
    else:
        luas = hitung_luas(jari_jari)
        keliling = hitung_keliling(jari_jari)
        print(f"Luas lingkaran: {luas}")
        print(f"Keliling lingkaran: {keliling}")