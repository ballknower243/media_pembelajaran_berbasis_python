import random

# Soal

bank_soal = {
    "Matematika":[
        ["Berapakah hasil dari 12 x 3?", ["A. 30", "B. 33", "C. 36", "D. 39"], "C", "12 x 3 = 36."],
        ["40% dari 200 adalah...", ["A. 40", "B. 60", "C. 80", "D. 100"], "C", "40% = 0.4; 0.4 x 200 = 80."],
        ["Sederhanakan pecahan 12/24", ["A. 1/3", "B. 1/2", "C. 2/3", "D. 3/4"], "B", "12/24 = 1/2."],
        ["7\u00b2 = ...", ["A. 14", "B. 42","C. 49", "D. 56"], "C", "7 x 7 = 49."],
        ["Hasil dari 15 + 27 adalah...", ["A. 32", "B. 42","C. 40", "D. 52"], "B", "15 + 27 = 42."],
        ["Hasil dari 9 x 8 adalah...", ["A. 64", "B. 72", "C. 81", "D. 98"], "B", "9 x 8 = 72."],
        ["Sederhanakan pecahan 18/54...", ["A. 1/2", "B. 1/3", "C. 2/3", "D. 3/4"], "B", "18 : 18 = 1, 54 : 18 = 3, hasilnya 1/3."],
        ["Hasil dari 125 - 75 adalah...", ["A. 40", "B. 45", "C. 50", "D. 55"], "C", "125 - 75 = 50."],
        ["25% dari 120 adalah...", ["A. 20", "B. 25", "C. 30", "D. 35"], "C", "25% = 0.25; 0.25 x 120 = 30."],
        ["Akar dari 81 adalah...", ["A. 7", "B. 8", "C. 9", "D. 10"], "C", "√81 = 9."],
    ],
    "IPA": [
        ["Bagian tumbuhan tempat fotosintesis terjadi adalah...", ["A. Akar", "B. Batang", "C. Bunga", "D. Daun"], "D", "Fotosintesis berlangsung di daun."],
        ["Benda yang dapat menghantarkan listrik disebut...", ["A. Isolator", "B. Konduktor", "C. Regulator", "D. Reaktor"], "B", "Konduktor = penghantar listrik."],
        ["Planet terdekat dari matahari adalah...", ["A. Venus", "B. Mars", "C. Merkurius", "D. Jupiter"], "C", "Planet terdekat adalah Merkurius."],
        ["Alat pernapasan pada ikan adalah...", ["A. Paru-paru", "B. Kulit", "C. Insang", "D. Trakea"], "C", "Ikan bernapas menggunakan insang."],
        ["Perubahan wujud padat menjadi cair disebut...", ["A. Menguap", "B. Mencair", "C. Membeku", "D. Mengembun"], "B", "Padat menjadi cair disebut dengan mencair."],
        ["Bagian tumbuhan yang berfungsi menyerap air adalah...", ["A. Daun", "B. Akar", "C. Batang", "D. Bunga"], "B", "Akar menyerap air dan mineral."],
        ["Sumber energi terbesar di bumi adalah...", ["A. Angin", "B. Baterai", "C. Matahari", "D. Api"], "C", "Energi utama berasal dari matahari."],
        ["Perubahan cair menjadi gas disebut...", ["A. Mencair", "B. Menguap", "C. Mengembun", "D. Menyublim"], "B", "Proses dari bentuk cair menjadi gas disebut menguap."],
        ["Hewan yang berkembang biak dengan bertelur disebut...", ["A. Mamalia", "B. Vivipar", "C. Ovipar", "D. Ovovivipar"], "C", "Hewan yang berkembang biak dengan bertelur disebut ovipar."],
        ["Gas yang dibutuhkan tumbuhan untuk fotosintesis adalah...", ["A. O2", "B. CO2", "C. N2", "D. H2"], "B", "Fotosintesis membutuhkan CO2."],
    ],
    "IPS": [
        ["Ibu kota Indonesia adalah...", ["A. Jakarta", "B. Bandung", "C. Surabaya", "D. Medan"], "A", "Ibu kota Indonesia adalah Jakarta."],
        ["Kegiatan jual beli disebut...", ["A. Produksi", "B. Konsumsi", "C. Perdagangan", "D. Interaksi"], "C", "Perdagangan adalah kegiatan jual beli."],
        ["Benua terbesar di dunia adalah...", ["A. Afrika", "B. Asia", "C. Eropa", "D. Amerika"], "B", "Asia adalah benua terbesar."],
        ["Alat tukar yang sah disebut...", ["A. Emas", "B. Uang", "C. Saham", "D. Obligasi"], "B", "Uang adalah alat tukar sah."],
        ["Kegiatan menghabiskan barang untuk memenuhi kebutuhan disebut...", ["A. Produksi", "B. Konsumsi", "C. Distribusi", "D. Investasi"], "B", "Konsumsi adalah kegiatan yang menghabiskan barang."],
        ["Mata uang resmi Indonesia adalah...", ["A. Dollar", "B. Peso", "C. Rupiah", "D. Ringgit"], "C", "Mata uang Indonesia adalah rupiah."],
        ["Kegiatan menghasilkan barang disebut...", ["A. Konsumsi", "B. Produksi", "C. Distribusi", "D. Investasi"], "B", "Kegiatan menghasilkan barang disebut produksi."],
        ["Benua terkecil di dunia adalah...", ["A. Asia", "B. Australia", "C. Afrika", "D. Eropa"], "B", "Australia adalah benua paling kecil."],
        ["Yang termasuk sumber daya alam terbarukan adalah...", ["A. Minyak bumi", "B. Batu bara", "C. Air", "D. Gas alam"], "C", "Air termasuk SDA terbarukan."],
        ["Kegiatan menyalurkan barang dari produsen ke konsumen disebut...", ["A. Produksi", "B. Konsumsi", "C. Distribusi", "D. Ekspor"], "C", "Distribusi merupakan kegiatan penyaluran barang."],
    ],
    "PPKn": [
        ["Lambang negara Indonesia adalah...", ["A. Burung Merpati", "B. Garuda Pancasila", "C. Banteng", "D. Bintang"], "B", "Lambang negara Indonesia adalah Garuda Pancasila."],
        ["Sila pertama Pancasila berbunyi...", ["A. Ketuhanan Yang Maha Esa", "B. Kemanusiaan yang Adil dan Beradab", "C. Persatuan Indonesia", "D. Kerakyatan yang dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan"], "A", "Sila pertama berbunyi Ketuhanan Yang Maha Esa."],
        ["Bhinneka Tunggal Ika berarti...", ["A. Berbeda-beda tetapi satu", "B. Bersatu selamanya", "C. Sama Rata", "D. Sama Rasa"], "A", "Arti dari Bhinneka Tunggal Ika ialah Berbeda-beda tetapi tetap satu."],
        ["Hak setiap warga negara adalah...", ["A. Mendapatkan pendidikan", "B. Membayar pajak", "C. Mematuhi hukum", "D. Menjaga lingkungan"], "A", "Mendapatkan pendidikan merupakan hak bagi setiap warga negara."],
        ["Contoh kewajiban warga negara adalah...", ["A. Menerima bantuan", "B. Menjaga kebersihan", "C. Mendapatkan perlindungan", "D. Mendapat kesehatan"], "B", "Menjaga kebersihan adalah kewajiban warga negara."],
        ["Sila kedua Pancasila berbunyi...", ["A. Ketuhanan Yang Maha Esa", "B. Kemanusiaan yang Adil dan Beradab", "C. Persatuan Indonesia", "D. Kerakyatan yang dipimpin oleh hikmat kebijaksanaan"], "B", "Sila ke-2 berbunyi Kemanusiaan yang Adil dan Beradab."],
        ["Contoh perilaku sesuai sila ke-3 adalah...", ["A. Rajin beribadah", "B. Menolong sesama", "C. Menjaga persatuan", "D. Musyawarah"], "C", "Sila ke-3 berbunyi Persatuan Indonesia."],
        ["Kewajiban warga negara adalah...", ["A. Mendapat pendidikan", "B. Bayar pajak", "C. Mendapat perlindungan", "D. Mendapat kesehatan"], "B", "Membayar pajak adalah kewajiban warga negara."],
        ["Lambang sila ke-4 adalah...", ["A. Bintang", "B. Rantai", "C. Pohon beringin", "D. Kepala banteng"], "D", "Sila ke-4 dilambangkan dengan kepala banteng."],
        ["Semboyan Indonesia ‘Bhinneka Tunggal Ika’ berasal dari...", ["A. Sutasoma", "B. Sumpah Pemuda", "C. UUD 1945", "D. Proklamasi"], "A", "Berasal dari kitab Sutasoma."],
    ],
    "Bahasa Indonesia": [
        ["Antonim dari kata 'besar' adalah...", ["A. Tinggi", "B. Luas", "C. Kecil", "D. Panjang"], "C", "Lawan kata dari 'besar' adalah kecil."],
        ["Sinonim kata 'indah' adalah...", ["A. Cantik", "B. Kusam", "C. Buruk", "D. Lelah"], "A", "Persamaan kata dari 'indah' ialah cantik."],
        ["Kata baku dari 'aktifitas' adalah...", ["A. Aktivitas", "B. Aktifitas", "C. Aktiviti", "D. Active"], "A", "Kata baku dari 'aktifitas' adalah aktivitas."],
        ["Bagian yang menceritakan tokoh dan alur disebut...", ["A. Judul", "B. Isi", "C. Sampul", "D. Indeks"], "B", "Isi berisi rangkaian cerita."],
        ["Kalimat tanya ditandai dengan tanda...", ["A. Titik", "B. Koma", "C. Seru", "D. Tanya"], "D", "Kalimat tanya menggunakan tanda tanya."],
        ["Sinonim kata 'cepat' adalah...", ["A. Lambat", "B. Kilat", "C. Jauh", "D. Sempit"], "B", "Sinonim cepat adalah kilat."],
        ["Antonim kata 'gelap' adalah...", ["A. Suram", "B. Redup", "C. Terang", "D. Kelam"], "C", "Lawan kata gelap adalah terang."],
        ["Kata baku dari 'kwalitas' adalah...", ["A. Kualitas", "B. Qualitas", "C. Kwaliti", "D. Quality"], "A", "Bentuk baku dari kata kwalitas adalah kualitas."],
        ["Kalimat yang menggunakan tanda seru adalah...", ["A. Di mana kamu tinggal", "B. Ayo kita belajar!", "C. Siapa namamu?", "D. Ini rumahku."], "B", "Kalimat seruan memakai tanda seru."],
        ["Bagian teks yang berisi penutup disebut...", ["A. Orientasi", "B. Komplikasi", "C. Resolusi", "D. Kodifikasi"], "C", "Resolusi adalah bagian penutup."],
    ],
}

#Daftar Nilai

rekap_nilai = []

# Materi
        
materi = {
    "Matematika": """
    Matematika mencakup:
    -Operasi hitung (penjumlahan, pengurangan, perkalian, dan pembagian)
    -Bilangan bulat dan bilangan pecahan
    -Persentase dan perbandingan
    -Pecahan biasa, pecahan campuran, dan desimal
    -Pangkat dan akar
""",
    
    "IPA": """
    IPA mencakup:
    -Ciri-ciri makhluk hidup (bernapas, bergerak, berkembang biak, dan lain-lainnya)
    -Energi dan perubahannya (gerak, panas, listrik)
    -Proses fotosintesis pada tumbuhan
    -Perubahan wujud benda (mencair, membeku, menguap, menyublim)
    -Sistem tata surya dan planet-planet
""",
    
    "IPS": """
    IPS mencakup:
    -Kegiatan ekonomi (produksi, distribusi, konsumsi)
    -Pembagian benua dan karakteristiknya
    -Interaksi sosial dalam kehidupan sehari-hari
    -Geografi dasar seperti cuaca, iklim, peta
""",
    
    "PPKn": """
    PPKn mencakup:
    -Nilai-nilai Pancasila dalam kehidupan sehari-hari
    -Hak dan kewajiban warga negara
    -Simbol negara (Garuda Pancasila, bendera merah putih, lagu kebangsaan)
    -Norma dan aturan yang berlaku di masyarakat
""",
    
    "Bahasa Indonesia": """
    Bahasa Indonesia mencakup:
    -Sinonim (persamaan kata) dan antonim (lawan kata)
    -Kata baku dan tidak baku
    -Struktur teks seperti teks narasi, deskripsi, dan eksposisi
    -Kaidah kebahasaan seperti penggunaan huruf kapital dan tanda baca
"""
}

# Menu Materi

def tampilkan_materi():
    while True:
        print("\n=== PEMBAHASAN MATERI ===")
    
        for i, mapel in enumerate(materi, start=1):
            print(f"{i}. {mapel}")
        print("6. Kembali ke Menu Utama")
    
        pilih = input("Pilih materi: ")

        if pilih == "6":
            break

        try:
            mapel = list(materi.keys())[int(pilih)-1]
            print(f"\n--- MATERI {mapel} ---")
            print(materi[mapel])

            input("\nTekan ENTER untuk kembali ke daftar materi...")
        
        except:
            print("Pilihan tidak ada.")

# Menu Contoh Soal

def contoh_soal():
    while True:
        print("\n=== CONTOH SOAL ===")
        for i, mapel in enumerate(bank_soal, start=1):
            print(f"{i}. {mapel}")
        print("6. Kembali ke Menu Utama")
        
        pilih = input("Pilih mapel: ")

        if pilih == "6":
            break

        try:
            mapel = list(bank_soal.keys())[int(pilih)-1]
            print(f"\n--- CONTOH SOAL {mapel} ---")
            for soal in bank_soal[mapel][:3]:
                print(f"\n{soal[0]}")
                print(f"Jawaban benar: {soal[2]}")
                print(f"Pembahasan: {soal[3]}")

            input("\nTekan ENTER untuk kembali ke daftar contoh soal...")
        
        except:
            print("Pilihan tidak ada.")

# Menu Tambah Soal

def tambah_soal():
    while True:
        print("\n=== TAMBAH SOAL BARU ===")
        for i, mapel in enumerate(bank_soal, start=1):
            print(f"{i}. {mapel}")
        print("6. Kembali ke Menu Utama")

        pilih = input("Masukkan nomor mapel: ")

        if pilih == "6":
            return
        

        try:
            mapel = list(bank_soal.keys())[int(pilih)-1]
        except:
            print("Pilihan tidak ada.")
            continue

        print(f"\nMenambah soal untuk mapel: {mapel}")

        pert = input("Masukkan pertanyaan: ")
        opsiA = input("Opsi A: ")
        opsiB = input("Opsi B: ")
        opsiC = input("Opsi C: ")
        opsiD = input("Opsi D: ")

        kunci = input("Masukkan kunci jawaban (A/B/C/D): ").upper()
        while kunci not in ["A", "B", "C", "D"]:
            print("Kunci tidak valid.")
            kunci = input("Masukkan kunci jawaban (A/B/C/D): ").upper()
        
        pemb = input("Masukkan pembahasan: ")

        bank_soal[mapel].append([
            pert,
            [f"A. {opsiA}", f"B. {opsiB}", f"C. {opsiC}", f"D. {opsiD}"],
            kunci,
            pemb
        ])
    
        print("\nSoal berhasil ditambahkan!")
        input("Tekan ENTER untuk kembali ke menu tambah soal...")
          
# Menu Kuis

def jalankan_kuis(mapel):
    print(f"\n=== KUIS {mapel.upper()} ===")
    
    soal_terpilih = random.sample(bank_soal[mapel], 10)
    skor = 0
    hasil_jawaban = []

    for nomor, soal in enumerate(soal_terpilih, start=1):
        print(f"\n{nomor}. {soal[0]}")
        for opsi in soal[1]:
            print(opsi)

        jawab = input("Jawabanmu: ").strip().upper()


        while jawab not in ["A", "B", "C", "D"]:
            print("Masukkan A, B, C, atau D")
            jawab = input("Jawabanmu: ").strip().upper()

        benar = jawab == soal[2]
        if benar:
            skor += 10

        hasil_jawaban.append({
            "pertanyaan": soal[0],
            "jawaban_user": jawab,
            "jawaban_benar": soal[2],
            "pembahasan": soal[3],
            "status": benar
        })

    print("\n=== HASIL KUIS ===")
    print(f"\nNilai akhir kamu: {skor}")

    
    if skor == 100:
        kategori = "Sangat Baik"
    elif skor >= 80:
        kategori = "Baik"
    elif skor >= 60:
        kategori = "Cukup"
    else:
        kategori = "Perlu Latihan Lagi"

    print(f"Kategori: {kategori}")


    rekap_nilai.append({
        "Jenis": "Kuis",
        "Mapel": mapel,
        "Nilai": skor
    })

    print("\n=== PEMBAHASAN JAWABAN ===")
    for i, data in enumerate(hasil_jawaban, start=1):
        print(f"\n{i}. {data['pertanyaan']}")
        print(f"Jawaban kamu   : {data['jawaban_user']}")
        print(f"Jawaban benar  : {data['jawaban_benar']}")
        print("Status         :", "Benar" if data["status"] else "Salah")
        print(f"Pembahasan     : {data['pembahasan']}")


# Menu Latihan

def latihan_campuran():
    print("\n=== LATIHAN (20 SOAL) ===")
    
    semua_soal = []
    for mapel in bank_soal:
        semua_soal.extend(random.sample(bank_soal[mapel], 4))

    skor = 0
    hasil_jawaban = []

    for nomor, soal in enumerate(semua_soal, start=1):
        print(f"\n{nomor}. {soal[0]}")
        for opsi in soal[1]:
            print(opsi)

        jawab = input("Jawabanmu: ").strip().upper()
    

        while jawab not in ["A", "B", "C", "D"]:
            print("Masukkan A, B, C, atau D")
            jawab = input("Jawabanmu: ").strip().upper()

        benar = jawab == soal[2]
        if benar:
            skor += 5

        hasil_jawaban.append({
            "pertanyaan": soal[0],
            "jawaban_user": jawab,
            "jawaban_benar": soal[2],
            "pembahasan": soal[3],
            "status": benar
        })
        
    print("\n=== HASIL LATIHAN ===")
    print(f"\nNilai akhir kamu: {skor}")

    
    if skor == 100:
        kategori = "Sangat Baik"
    elif skor >= 80:
        kategori = "Baik"
    elif skor >= 60:
        kategori = "Cukup"
    else:
        kategori = "Perlu Latihan Lagi"

    print(f"Kategori: {kategori}")


    rekap_nilai.append({
        "Jenis": "Latihan",
        "Mapel": "Campuran 5 Mapel",
        "Nilai": skor
    })

    print("\n=== PEMBAHASAN JAWABAN ===")
    for i, data in enumerate(hasil_jawaban, start=1):
        print(f"\n{i}. {data['pertanyaan']}")
        print(f"Jawaban kamu   : {data['jawaban_user']}")
        print(f"Jawaban benar  : {data['jawaban_benar']}")
        print("Status         :", "Benar" if data["status"] else "Salah")
        print(f"Pembahasan     : {data['pembahasan']}")

    input("\nTekan ENTER untuk kembali ke menu utama...")

# Menu Informasi Pembuat

def info_pembuat():
    print("\n=== INFORMASI PEMBUAT PROGRAM ===")
    print("Nama pembuat: Muhammad Aditiya Mursalin")
    print("Nim: 2510131310007")
    print("Prodi: Pendidikan Komputer")
    print("Mata Kuliah: Pemrograman Dasar 1")
    print("Progam dibuat untuk projek tugas akhir 'Media Pembelajaran Kuis Interaktif Berbasis Python'")

# Menu Rekap Nilai

def tampilkan_rekap():
    print("\n=== REKAP NILAI ===")
    if not rekap_nilai:
        print("Belum ada nilai yang tersimpan.")
        return

    for i, item in enumerate(rekap_nilai, start=1):
        print(f"{i}. {item['Jenis']} - {item['Mapel']} : {item['Nilai']}")

# Menu Utama

def menu_utama():
    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Pembahasan Materi")
        print("2. Contoh Soal")
        print("3. Tambah Soal")
        print("4. Kuis (Pilih Mata Pelajaran)")
        print("5. Latihan (20 Soal)")
        print("6. Informasi Pembuat")
        print("7. Daftar Nilai / Rekap Nilai")
        print("8. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_materi()
        elif pilih == "2":
            contoh_soal()
        elif pilih == "3":
            tambah_soal()
        elif pilih == "4":
            while True:
                print("\n=== MENU KUIS ===")
                for i, mapel in enumerate(bank_soal, start=1):
                    print(f"{i}. {mapel}")
                print("6. Kembali ke Menu Utama")

                pilih_mapel = input("Pilih mapel untuk memulai kuis: ")

                if pilih_mapel == "6":
                    break
                
                try:
                    mapel = list(bank_soal.keys())[int(pilih_mapel)-1]
                    jalankan_kuis(mapel)

                    input("\nTekan ENTER untuk kembali ke menu kuis....")
                
                except:
                    print("Pilihan tidak ada.")
        elif pilih == "5":
            latihan_campuran()
        elif pilih == "6":
            info_pembuat()
        elif pilih == "7":
            tampilkan_rekap()
        elif pilih == "8":
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak ada.")

# Untuk Menjalankan Program

menu_utama()
