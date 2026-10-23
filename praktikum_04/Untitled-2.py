
def tampilkan_soal(nomor, teks_soal):
    print("=== Sesi Ujian ===")
    print(f"Soal {nomor}:")
    print(teks_soal)
    print("Pilih jawaban A, B, C, atau D")
    print()


def periksa_jawaban(jawaban_user, kunci_jawaban):
    if jawaban_user.strip().upper() == kunci_jawaban.upper():
        print("Jawaban benar!")
        return True
    else:
        print("Jawaban salah!")
        return False


def hitung_skor(jumlah_benar, total_soal):
    return float((jumlah_benar / total_soal) * 100)


def main():
    nomor = 1

    tampilkan_soal(nomor, "Apa ibukota Indonesia?")

    jawaban = input("Jawaban Anda: ")
    hasil = periksa_jawaban(jawaban, "B")

    if hasil:
        jumlah_benar = 1
    else:
        jumlah_benar = 0

    skor_akhir = hitung_skor(jumlah_benar, 1)
    print(f"Skor akhir: {skor_akhir}")


if __name__ == "__main__":
    main()
