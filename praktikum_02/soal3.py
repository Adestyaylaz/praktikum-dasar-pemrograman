harga_satuan = float(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah: "))
persen_diskon = float(input("Masukkan diskon (%): "))

subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * persen_diskon / 100
total_bayar = subtotal - nominal_diskon

print("Subtotal = Rp", subtotal)
print("Diskon = Rp", nominal_diskon)
print("Total bayar = Rp", total_bayar)