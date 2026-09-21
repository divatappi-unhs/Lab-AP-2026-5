jarak = int (input("Masukkan jarak pengiriman (km): "))
express_input = input("Layanan express (ya/tidak): ").strip().lower()
if jarak < 5:
    tarif_dasar = 10000
elif 5 <= jarak <= 20:
    tarif_dasar = 20000
else:  # jarak > 20 km
    tarif_dasar = 35000
    
biaya_express = 15000 if express_input == "ya" else 0
total_tarif = tarif_dasar + biaya_express
print("Total tarif pengiriman: Rp",  total_tarif)