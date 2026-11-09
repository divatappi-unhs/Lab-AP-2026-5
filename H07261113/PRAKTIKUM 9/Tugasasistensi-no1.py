class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):  
        self.nama = nama 
        self.id_pemain = id_pemain               
        self.role = role                         
        self.nilai_kill = nilai_kill             
        self.nilai_assist = nilai_assist        
        self.nilai_objective = nilai_objective   

#memakai 3 method

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor 

    def status_performa(self):  
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi" 

    def tampilkan_data(self):
        print(f"{self.nama:<15} {self.id_pemain:<10} {self.role:<12} "
              f"{self.nilai_kill:<8} {self.nilai_assist:<8} "
              f"{self.hitung_skor_akhir():<10.2f} | "
              f"{self.status_performa()}")


# List untuk menyimpan objek pemain
daftar_pemain = []

# Input jumlah pemain

while True:
    try:
        jumlah = int(input("Masukkan jumlah pemain: "))
        if jumlah >0:
            break
        else :
            print ("Angka tidak boleh nol atau negatif!!")
        
    except:
        print ("Inputan tidak boleh nol atau negatif!!")

# Perulangan input data pemain
for i in range(jumlah): 
    print(f"\nData pemain ke-{i + 1}") 

    nama = input("Nama pemain: ")
    id_pemain = input("ID pemain: ")
    role = input("Role/posisi: ")

    
    while True:
        try:
            nilai_kill = float(input("Nilai Kill: ")) 
            if nilai_kill >= 0:
                break 
            else :
                print ("Angka tidak boleh nol atau negatif!!")
            
        except:
            print ("Inputan tidak boleh nol atau negatif!!")
    
    while True:
        try:
            nilai_assist = float(input("Nilai Assist: "))
            if nilai_assist >= 0 :
                break 
            else :
                print ("Angka tidak boleh nol atau negatif!!")
            
        except:
            print ("Inputan tidak boleh nol atau negatif!!")

    while True:
            try:
                nilai_objective = float(input("Nilai Objective: "))
                if nilai_objective >= 0 :
                    break 
                else :
                    print ("Angka tidak boleh nol atau negatif!!")
                
            except:
                print ("Inputan tidak boleh nol atau negatif!!")

    pemain = Pemain(
        nama,
        id_pemain,
        role,
        nilai_kill,
        nilai_assist,
        nilai_objective
    )

    daftar_pemain.append(pemain) 


# Menampilkan tabel data pemain
print("\n" + "=" * 100)
print("                 TABEL PERFORMA PEMAIN")
print("=" * 100)

print(f"{'Nama':<15} {'ID':<10} {'Role':<12} {'Kill':<8} "
      f"{'Assist':<8} {'Objective':<10} {'Skor Akhir':<10} {'Status'}")

print("-" * 100)

for pemain in daftar_pemain:
    pemain.tampilkan_data()

print("=" * 100)
