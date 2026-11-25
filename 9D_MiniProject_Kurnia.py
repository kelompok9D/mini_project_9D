JUDUL = ["Analisis Hubungan Penggunaan Diskon",
    "dengan Tingkat Kepuasan Pelanggan",
    "Menggunakan Python",
]
MATA_KULIAH = "PEMROGRAMAN KOMPUTER"
KELOMPOK = "Kelompok 9D"
ANGGOTA = [("Sayyid Nabil Ramadhan", "2610932039"), ("Dinara Savitri", "2610932027"), ("Najla Mutia Adiba", "2610931008")]
ASISTEN = "Kurnia Rahmat Illahi"
DOSEN = "Ikhwan Arief, S.T., M.Sc."
LABOR = "Laboratorium Sistem informasi dan keputusan"
DEPARTEMEN = "DEPARTEMEN TEKNIK INDUSRTI"
FAKULTAS = "FAKULTAS TEKNIK"
KAMPUS = "UNIVERSITAS ANDALAS"
TAHUN = "2026"
LEBAR = 60


def baris(teks=""):
    return "|" + teks.center(LEBAR - 2) + "|"


def buat_cover():
    garis = "+" + "=" * (LEBAR - 2) + "+"
    isi = [garis, baris(), baris("MINI PROJECT"), baris(MATA_KULIAH), baris()]
    for potongan in JUDUL:
        isi.append(baris(potongan.upper()))
    isi += [baris(), baris("Oleh:"), baris(KELOMPOK), baris(), baris("Anggota")]
    for nama, nim in ANGGOTA:
        isi.append(baris(f"{nama} {(nim)}"))
    isi += [baris(), baris("Asisten Pembimbing:"), baris(ASISTEN), baris(), baris("Dosen Pengampu:"), baris(DOSEN), baris(),
            baris(), baris(LABOR.upper()), baris(DEPARTEMEN.upper()), baris(FAKULTAS.upper()), baris(KAMPUS.upper()),  baris(TAHUN), garis]
    return isi



for a in buat_cover():
    print(a)

# login
USERNAME = ("SAYYID NABIL RAMADHAN", "DINARA SAVITRI", "NAJLA MUTIA ADIBA")
PASSWORD =("2610932039", "2610932027", "2610931008")
MAKS_PERCOBAAN = 3

def login():
    for percobaan in range(1, MAKS_PERCOBAAN+1):
        usn = input("Username:")
        pw = input("Password:")
        sisa = MAKS_PERCOBAAN - percobaan

        for i in range(len(USERNAME)):
            if usn == USERNAME[i] and pw == PASSWORD[i]:
                print("LOGIN BERHASIL")
                return True
        print(f"Username/Password salah silahkan coba lagi, Sisa Percobaan: {sisa}\n")
print()

#menu
import os
import csv
import shutil
import math

NAMA_FILE = "e-commerce_csv.csv"
NAMA_LAPORAN = "laporan_analisis_diskon.txt"

def baca_dataset(nama_file):
    with open(nama_file, newline="", encoding="utf-8-sig")as file:
        pembaca = csv.DictReader(file)
        kolom = pembaca.fieldnames
        data = list(pembaca)
    for wajib in ("Id", "Discount_offered", "Customer_rating"):
        if wajib not in kolom:
            raise ValueError(f"Kolom {wajib} tidak ditemukan dalam dataset")
    return kolom, data

def simpan_dataset(nama_file, kolom, data):
    backup = nama_file.replace(".csv", "") + "_backup.csv"

    if os.path.exists(nama_file): 
        if not os.path.exists(backup): 
            shutil.copyfile(nama_file, backup)

    with open(nama_file, "w", newline="", encoding="utf-8-sig") as file:
        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(data)

    return backup

KOLOM_WAJIB = ("Discount_offered", "Customer_rating")
BATAS_R = 0.2

def cari_kolom_numerik(kolom, data):
    numerik = list(KOLOM_WAJIB)
    for nama in kolom:
        if nama in numerik:
            continue
        isi = []

        for b in data:
            if b[nama].strip() == "":
                isi.append(b[nama])

        if not isi:
            continue
        try:
            for nilai in isi:
                float(nilai)
                numerik.append(nama)
        except ValueError:
                pass 
    return numerik

def validasi_data(data): 
    x = []
    y = []
    masalah = {"kosong": [], "bukan angka": [],
               "diskon negatif": [], "rating di luar 1-5": []}

    for baris in data:
        id_baris = baris["Id"]
        diskon_teks = baris["Discount_offered"].strip()
        rating_teks = baris["Customer_rating"].strip()

        if diskon_teks == "" or rating_teks == "":
            masalah["kosong"].append(id_baris) 
            continue
        try:
            diskon = float(diskon_teks)
            rating = float(rating_teks)
        except ValueError:
            masalah["bukan angka"].append(id_baris) 
            continue
        if diskon < 0:
            masalah["diskon negatif"].append(id_baris)
            continue
        if rating not in (1, 2, 3, 4, 5):
            masalah["rating di luar 1-5"].append(id_baris)
            continue
        x.append(diskon) 
        y.append(rating)
    return x, y, masalah


def ringkas_validasi(data):
    x, y, masalah = validasi_data(data)

    status = f"Validasi otomatis: {len(x)} dari {len(data)} baris valid"

    jumlah_kosong = len(masalah["kosong"])
    jumlah_bukan_angka = len(masalah["bukan angka"])
    jumlah_diskon_negatif = len(masalah["diskon negatif"])
    jumlah_rating_salah = len(masalah["rating di luar 1-5"])

    
    rincian = ""
    if jumlah_kosong > 0:
        rincian = rincian + f"{jumlah_kosong} kosong, "
    if jumlah_bukan_angka > 0:
        rincian = rincian + f"{jumlah_bukan_angka} bukan angka, "
    if jumlah_diskon_negatif > 0:
        rincian = rincian + f"{jumlah_diskon_negatif} diskon negatif, "
    if jumlah_rating_salah > 0:
        rincian = rincian + f"{jumlah_rating_salah} rating di luar 1-5, "

    
    if rincian != "":
        status = status + " (data_tidak_valid: " + rincian[:-2] + ")"

    return x, y, status          

def tampilkan_validasi(data):
    x, y, masalah = validasi_data(data) 
    total = len(data)
    data_tidak_valid = total - len(x)

    print("=" * 50)
    print("  HASIL VALIDASI DATA")
    print("=" * 50)
    print(f"Jumlah baris data : {total}")
    print("Kolom diperiksa   : Discount_offered, Customer_rating")
    print("-" * 50)
    print(f"{'Pemeriksaan':<30}{'Hasil':>12}")
    for jenis, daftar in masalah.items():
        print(f"{jenis.capitalize():<30}{len(daftar):>7} baris") #.capitalize ini untuk membuat huruf awal menjadi kapital.
    print("-" * 50)
    persen = len(x) / total * 100 if total else 0
    print(f"Data valid        : {len(x)} baris ({persen:.1f}%)")
    print(f"Data tidak valid      : {data_tidak_valid} baris")

    if data_tidak_valid > 0:
        print("\nID baris bermasalah (maks. 5 per jenis):")
        for jenis, daftar in masalah.items():
            if daftar:
                print(f"  - {jenis}: {', '.join(daftar[:5])}") 
        print("\nStatus            : baris bermasalah data_tidak_valid dari analisis")
        print("Perbaiki lewat menu 3 (Kelola data).")
    else:
        print("\nStatus            : DATA SIAP DIANALISIS")

def tampilkan_satu_baris(baris):
    for nama in baris:
        nilai = baris[nama]
        if nilai == "":
            nilai = "(kosong)"
        print(f"  {nama:<22}: {nilai}")

def cari_berdasarkan_id(data, id_cari):
    for baris in data:
        if baris["ID"] == id_cari:
            return baris
    return None

def id_baru(data):
    terbesar = 0
    for baris in data:
        try:
            id_sekarang = int(baris["ID"])
        except ValueError:
            continue                    
        if id_sekarang > terbesar:
            terbesar = id_sekarang
    return terbesar + 1

def minta_nilai(nama_kolom, numerik, boleh_kosong):
    while True:
        if boleh_kosong:
            teks = input(f"{nama_kolom} (Enter = kosong): ").strip() 
        else:
            teks = input(f"{nama_kolom} (Enter = batal): ").strip()

        if teks == "":
            if boleh_kosong:
                return ""
            return None

        if nama_kolom == "Customer_rating":
            if teks in ["1", "2", "3", "4", "5"]:
                return teks
            print("Rating harus bilangan bulat 1 sampai 5.")
        elif nama_kolom in numerik:
            teks = teks.replace(",", ".") 
            try:
                nilai = float(teks)
            except ValueError:
                print(f"{nama_kolom} harus berupa angka.")
                continue
            if nama_kolom == "Discount_offered" and nilai < 0:
                print("Diskon tidak boleh negatif.")
                continue
            return teks
        else:
            return teks

def tambah_baris(data, kolom, numerik):
    baris = {}
    for k in kolom:
        baris[k] = ""
    baris["ID"] = str(id_baru(data))
    print(f"Data baru akan diberi ID {baris['ID']}.")
    for k in kolom:
        if k != "ID":
            baris[k] = minta_nilai(k, numerik, True)
    data.append(baris)
    return baris  

def ubah_baris(baris, kolom, numerik):
    berubah = False
    while True:
        print("\nKolom yang bisa diubah:")
        for i in range(len(kolom)):
            if kolom[i] != "ID":
                isi = baris[kolom[i]]
                if isi == "":
                    isi = "(kosong)"
                print(f"  {i + 1:>2}. {kolom[i]:<22} = {isi}")
        pilih = input("Nomor kolom yang diubah (Enter = selesai): ").strip()
        if pilih == "":
            return berubah
        try:
            nomor = int(pilih)
        except ValueError:
            print("Nomor tidak valid.")
            continue
        if nomor < 1 or nomor > len(kolom) or kolom[nomor - 1] == "ID":
            print("Nomor tidak valid.")
            continue
        nama = kolom[nomor - 1]
        nilai = minta_nilai(nama, numerik, False)
        if nilai is None:
            print("Dibatalkan.")
            continue
        lama = baris[nama]
        baris[nama] = nilai
        berubah = True
        if lama == "":
            lama = "(kosong)"
        print(f"{nama}: {lama}  ->  {nilai}")     

def hapus_semua_isi(kolom, data, file_aktif):
    print(f"\nPERINGATAN: Anda akan menghapus semua isi data di '{file_aktif}'.")
    print("Hanya baris header (nama kolom) yang tersisa.")
    jawab = input("Yakin hapus semua data? (y/n): ").strip().lower()
    if jawab != "y":
        print("Dibatalkan.")
        return False
    data.clear()
    backup = simpan_dataset(file_aktif, kolom, data)
    print(f"Semua data dihapus. File asli aman di '{backup}'.")
    return True

def tampilkan_submenu(jumlah_data, belum_simpan):
    print()
    print("-" * 46)
    print("  KELOLA DATA")
    print("-" * 46)
    print(f" Jumlah data saat ini: {jumlah_data} baris")
    if belum_simpan:
        print(" (ada perubahan yang BELUM disimpan ke file)")
    print(" 1. Tambah data baru")
    print(" 2. Ubah data")
    print(" 3. Hapus data")
    print(" 4. Simpan perubahan ke file CSV")
    print(" 0. Kembali ke menu utama")
    print("-" * 46)

def info_setelah_perubahan(data):
    hasil = ringkas_validasi(data)        
    print(hasil[2])                       
    print("Perubahan belum tersimpan ke CSV. Pilih 4 untuk menyimpan.")

def kelola_data(kolom, data, numerik, file_aktif, belum_simpan):
    while True:
        tampilkan_submenu(len(data), belum_simpan)
        pilihan = input("Mau melakukan apa? ").strip()

        if pilihan == "0":
            return belum_simpan

        elif pilihan == "1":
            baris = tambah_baris(data, kolom, numerik)
            belum_simpan = True
            print("Data ditambahkan:")
            tampilkan_satu_baris(baris)
            info_setelah_perubahan(data)

        elif pilihan == "2":
            id_cari = input("ID yang diubah: ").strip()
            baris = cari_berdasarkan_id(data, id_cari)
            if baris is None:
                print("ID tidak ditemukan.")
                continue
            tampilkan_satu_baris(baris)
            if ubah_baris(baris, kolom, numerik):
                belum_simpan = True
                print("\nData setelah diubah:")
                tampilkan_satu_baris(baris)
                info_setelah_perubahan(data)

        elif pilihan == "3":
            id_cari = input("ID yang dihapus: ").strip()
            baris = cari_berdasarkan_id(data, id_cari)
            if baris is None:
                print("ID tidak ditemukan.")
                continue
            tampilkan_satu_baris(baris)
            jawab = input("Yakin hapus data ini? (y/n): ").strip().lower()
            if jawab == "y":
                data.remove(baris)
                belum_simpan = True
                print("Data dihapus.")
                info_setelah_perubahan(data)
            else:
                print("Dibatalkan.")

        elif pilihan == "4":
            if hapus_semua_isi(kolom, data, file_aktif):
                belum_simpan = False

        elif pilihan == "5":
            backup = simpan_dataset(file_aktif, kolom, data)
            belum_simpan = False
            print(f"Tersimpan ke '{file_aktif}' ({len(data)} baris).")
            print(f"File asli aman di '{backup}'.")

        else:
            print("Pilihan tidak valid.")

def hitung_jumlah(x, y):
    n = len(x)
    sx = 0
    sy = 0
    sxy = 0
    sx2 = 0
    sy2 = 0
    for i in range(n):
        sx += x[i]
        sy += y[i]
        sxy += x[i] * y[i]
        sx2 += x[i] * x[i]
        sy2 += y[i] * y[i]
    return n, sx, sy, sxy, sx2, sy2

def hitung_regresi(x, y):
    n, sx, sy, sxy, sx2, sy2 = hitung_jumlah(x, y)
    b = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
    a = (sy - b * sx) / n
    return a, b


def hitung_korelasi(x, y):
    n, sx, sy, sxy, sx2, sy2 = hitung_jumlah(x, y)
    pembilang = n * sxy - sx * sy
    penyebut = math.sqrt((n * sx2 - sx ** 2) * (n * sy2 - sy ** 2))
    r = pembilang / penyebut
    return r, r * r

def interpretasi_r(r):
    kuat = r
    if r < 0:
        kuat = -r

    if kuat < 0.2:
        tingkat = "sangat lemah"
    elif kuat < 0.4:
        tingkat = "lemah"
    elif kuat < 0.6:
        tingkat = "sedang"
    elif kuat < 0.8:
        tingkat = "kuat"
    else:
        tingkat = "sangat kuat"

    if r > 0:
        arah = "searah (diskon naik, rating cenderung naik)"
    elif r < 0:
        arah = "berlawanan (diskon naik, rating cenderung turun)"
    else:
        arah = "tidak ada arah"
    return f"hubungan {tingkat}, {arah}"

def tampilkan_regresi(x, y):
    n, sx, sy, sxy, sx2, sy2 = hitung_jumlah(x, y)
    a, b = hitung_regresi(x, y)
    r, r2 = hitung_korelasi(x, y)
    print("=" * 50)
    print("  ANALISIS REGRESI LINEAR SEDERHANA")
    print("  X = Discount_offered | Y = Customer_rating")
    print("=" * 50)
    print(f"n   = {n}")
    print(f"Σx  = {sx:g}") 
    print(f"Σy  = {sy:g}")
    print(f"Σxy = {sxy:g}")
    print(f"Σx² = {sx2:g}")
    print(f"Σy² = {sy2:g}")
    print("-" * 50)
    print(f"Gradien  (b)     = {b:.6f}") 
    print(f"Intersep (a)     = {a:.4f}")
    print(f"Persamaan        : ŷ = {a:.4f} + ({b:.6f}) x")
    print("-" * 50)
    print(f"Korelasi (r)     = {r:.4f}")
    print(f"Determinasi (R²) = {r2 * 100:.4f}%")
    print(f"Arti             : {interpretasi_r(r)}")

def prediksi(a, b, diskon):
    hasil = a + b * diskon 
    if hasil > 5.0:
        hasil = 5.0
    elif hasil < 1.0:
        hasil = 1.0
    return hasil

def buat_saran(x, y, a, b, r, r2):
    n = len(x)
    rata_y = sum(y) / n
    saran = []
    jumlah_kurang_puas = 0
    for yi in y:
        if yi <=2 :
            jumlah_kurang_puas = jumlah_kurang_puas + 1

    kurang_puas = jumlah_kurang_puas / n * 100

    per_10  = b * 10
    y_min = prediksi(a, b, min(x))
    y_max = prediksi(a, b, max(x))

    if -BATAS_R < r < BATAS_R:
        saran.append(f"Jangan cuman mengandalkan diskon untuk menaikkan kepuasan pelanggan, "
                     f"karena jika menambah diskon 10 poin, hanya akan mengubah rating sebanyak {per_10:+.4f}.")
        saran.append(f"Prediksi rating pada diskon {max(x):g} "
                     f"({y_max:.2f}) nyaris sama dengan pada diskon {min(x):g} "
                     f"({y_min:.2f}), jadi diskon besar belum terbukti membuat pelanggan lebih puas. "
                     f"Batasi diskon besar bila tujuannya hanya kepuasan.")
        saran.append(f"Gunakan diskon untuk tujuan lain, seperti menarik pembeli baru atau menghabiskan stok, "
                     f"dan ukur hasilnya dengan data penjualan, bukan rating.")
        saran.append(f"Cari faktor lain yang mempengaruhi kepuasan. Diskon hanya menjelaskan "
                     f"{r2 * 100:.4f}% variasi rating, sisanya dari faktor lain, misalnya "
                     f"ketepatan pengiriman, layanan pelanggan, dan kualitas produk. "
                     f"Jadi, lakukan survei atau kumpulkan komentar pelanggan untuk mengetahui faktor utamanya.")
    elif r >= BATAS_R:
        saran.append(f"Diskon dapat dipertahankan sebagai salah satu strategi kepuasan, "
                     f"karena setiap tambahan diskon 10 poin menaikkan rating sekitar {per_10:+.4f}.")
        saran.append("Naikkan diskon secara bertahap lalu cek apakah tambahan rating sepadan "
                     "dengan uang yang hilang dari potongan harga, supaya keuntungan tidak tergerus.")
        saran.append(f"Jangan hanya bergantung pada diskon. Diskon menjelaskan {r2 * 100:.2f}% "
                     f"variasi rating, sisanya dari faktor lain yang tetap perlu dibenahi.")
    else:
        saran.append(f"Tinjau kembali strategi diskon. Setiap tambahan diskon 10 poin justru "
                     f"menurunkan rating sekitar {per_10:+.4f}.")
        saran.append("Selidiki penyebabnya pada pesanan berdiskon besar, misalnya "
                     "kualitas produk, ketepatan pengiriman, atau harapan pelanggan yang tidak terpenuhi.")
        saran.append("Uji coba batas diskon yang lebih rendah pada sebagian pelanggan, "
                     "lalu bandingkan ratingnya.")

    if rata_y < 3.5:
        saran.append(f"Rata-rata rating {rata_y:.2f} dari 5 dan {kurang_puas:.1f}% pelanggan "
                     f"kurang puas (rating 1-2). Jadikan peningkatan kualitas layanan "
                     f"sebagai prioritas, tanpa menunggu perubahan diskon.")
    elif rata_y < 4.0:
        saran.append(f"Rata-rata rating {rata_y:.2f} dari 5 tergolong cukup. "
                     f"Targetkan peningkatan dengan memperbaiki layanan.")
    else:
        saran.append(f"Rata-rata rating {rata_y:.2f} dari 5 sudah baik. "
                     f"Pertahankan kualitas layanan saat ini.")

    saran.append("\n Ulangi analisis ini secara berkala, terutama setelah kebijakan diskon berubah, "
                 "agar keputusan selalu memakai data terbaru.")
    return saran

def buat_laporan(x, y):
    n = len(x)
    a, b = hitung_regresi(x, y)
    r, r2 = hitung_korelasi(x, y)
    jumlah_puas = 0
    jumlah_kurang_puas = 0

    for nilai in y:
        if nilai >= 4:
            jumlah_puas = jumlah_puas + 1

        if nilai <= 2:
            jumlah_kurang_puas = jumlah_kurang_puas + 1

    puas = jumlah_puas / n * 100
    kurang_puas = jumlah_kurang_puas / n * 100

    baris = []
    baris.append("=" * 66)
    baris.append("  LAPORAN ANALISIS DISKON vs KEPUASAN PELANGGAN")
    baris.append("  Metode: Regresi Linear Sederhana")
    baris.append("=" * 66)
    baris.append("[ 1. Ringkasan data ]")
    baris.append(f"Jumlah data valid  : {n} pelanggan")
    baris.append(f"Rentang diskon     : {min(x):g} sampai {max(x):g}")
    baris.append(f"Rata-rata diskon   : {sum(x) / n:.2f}")
    baris.append(f"Rata-rata rating   : {sum(y) / n:.2f} (skala 1-5)")
    baris.append(f"Puas (rating 4-5)  : {puas:.1f}%")
    baris.append(f"Kurang puas (1-2)  : {kurang_puas:.1f}%")
    baris.append("")
    baris.append("[ 2. Hasil regresi linear sederhana ]")
    baris.append("X = Discount_offered | Y = Customer_rating")
    baris.append(f"Persamaan        : ŷ = {a:.4f} + ({b:.6f}) x")
    baris.append(f"Korelasi (r)     : {r:.4f} -> {interpretasi_r(r)}")
    baris.append(f"Determinasi (R²) : {r2 * 100:.4f}%")
    baris.append(f"Arti gradien     : tiap diskon naik 10 poin, rating berubah {b * 10:+.4f}")
    baris.append(f"Prediksi rating  : diskon {min(x):g} -> {prediksi(a, b, min(x)):.2f} | "
                     f"rata-rata {sum(x) / n:.1f} -> {prediksi(a, b, sum(x) / n):.2f} | "
                     f"diskon {max(x):g} -> {prediksi(a, b, max(x)):.2f}")
    baris.append("")
    baris.append("[ 3. Kesimpulan ]")
    if -BATAS_R < r < BATAS_R:
            baris.append("Diskon tidak berpengaruh berarti terhadap kepuasan pelanggan.")
            baris.append(f"- Korelasi r = {r:.4f} tergolong sangat lemah.")
            baris.append(f"- Diskon hanya menjelaskan {r2 * 100:.4f}% variasi rating.")
    elif r > 0:
            baris.append("Semakin besar diskon, kepuasan pelanggan cenderung naik.")
            baris.append(f"- Diskon menjelaskan {r2 * 100:.2f}% variasi rating (r = {r:.4f}).")
    else:
            baris.append("Semakin besar diskon, kepuasan pelanggan cenderung turun.")
            baris.append(f"- Diskon menjelaskan {r2 * 100:.2f}% variasi rating (r = {r:.4f}).")
    baris.append("")
    baris.append("[ 4. Saran dan rekomendasi untuk perusahaan ]")
    for no, kalimat in enumerate(buat_saran(x, y, a, b, r, r2), start=1): 
            baris.append(f"{no}. {kalimat}")
    baris.append("")
    baris.append("Catatan: hasil menunjukkan hubungan, bukan sebab-akibat.")
    return baris

def tampilkan_menu():
    print()
    print("=" * 46)
    print("  ANALISIS DISKON vs KEPUASAN PELANGGAN")
    print("=" * 46)
    print(" 1. Buka dataset")
    print(" 2. Validasi")
    print(" 3. Kelola data (tambah, ubah, hapus, simpan)")
    print(" 4. Analisis regresi dan korelasi")
    print(" 5. Laporan, kesimpulan, dan saran")
    print(" 6. Keluar")
    print("=" * 46)

def jalankan_menu():
    kolom = data = None     
    numerik = []             
    x = y = None             
    file_aktif = NAMA_FILE
    belum_simpan = False    
    sudah_buka_menu = False  

    while True:
        tampilkan_menu()
        if sudah_buka_menu:
            pilihan = input("Ingin buka menu apa lagi? ").strip()
        else:
            pilihan = input("Mau buka menu yang mana? ").strip()

        if pilihan == "1":
            nama = input(f"Nama file CSV (Enter = {NAMA_FILE}): ").strip() or NAMA_FILE
            try:
                kolom, data = baca_dataset(nama)
                file_aktif = nama
                numerik = cari_kolom_numerik(kolom, data)
                belum_simpan = False
                print(f"Dataset berhasil dibuka: {len(data)} baris, {len(kolom)} kolom")
                print("Kolom analisis: Discount_offered (X), Customer_rating (Y)")
                x, y, status = ringkas_validasi(data)    
                print(status)
                sudah_buka_menu = True
            except FileNotFoundError:
                print(f"File '{nama}' tidak ditemukan.")
            except KeyError as e:
                print(f"Kolom {e} tidak ada di file.")

        elif pilihan == "6":
            if belum_simpan:
                jawab = input("Ada perubahan yang belum disimpan. "
                              "Simpan sekarang? (y/n): ").strip().lower()
                if jawab == "y":
                    simpan_dataset(file_aktif, kolom, data)
                    print(f"Tersimpan ke '{file_aktif}'.")
            print("Anda keluar. Kembali ke halaman login.")
            return

        elif pilihan not in ("2", "3", "4", "5"):
            print("Pilihan tidak valid. Pilih angka 1 sampai 6.")

        elif data is None:
            print("Buka dataset dulu (menu 1).")
       
        elif pilihan == "2":
            tampilkan_validasi(data)
            sudah_buka_menu = True

        elif pilihan == "3":
            belum_simpan = kelola_data(kolom, data, numerik, file_aktif, belum_simpan)
            x, y, _ = ringkas_validasi(data)     
            sudah_buka_menu = True

        elif len(x) < 2:
            print("Data valid kurang dari 2 baris, analisis tidak bisa dilakukan.")

        elif pilihan == "4":
            try:
                tampilkan_regresi(x, y)
                sudah_buka_menu = True
            except ZeroDivisionError:
                print("Semua nilai diskon (atau rating) sama, regresi tidak bisa dihitung.")

        elif pilihan == "5":
            try:
                laporan = buat_laporan(x, y)
            except ZeroDivisionError: 
                print("Laporan tidak bisa dibuat: nilai diskon atau rating seragam.")
                continue
            print()
            for garis_laporan in laporan:
                print(garis_laporan)
            if input ("\nSimpan laporan ke file? (y/n): ").strip().lower() == "y":
                with open(NAMA_LAPORAN, "w", encoding="utf-8") as f:
                    f.write("\n".join(laporan) + "\n")
                print(f"Laporan disimpan ke '{NAMA_LAPORAN}'")
            sudah_buka_menu = True


def main():
    while True:
        if not login():                
            print("Program ditutup. Terima kasih.")
            break
        jalankan_menu()                 


main()