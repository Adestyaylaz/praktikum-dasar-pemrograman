kalimat = input("Masukkan sebuah kalimat: ")
hitung_vokal = 0

for huruf in kalimat.lower():
    if huruf in "aiueo":
        hitung_vokal += 1

print("Jumlah huruf vokal:", hitung_vokal)