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
USERNAME = "MINIPROJECT9D"
PASSWORD = "2310931006"
MAKS_PERCOBAAN = 3

def login():
    for percobaan in range(1, MAKS_PERCOBAAN+1):
        usn = input("Username:")
        pw = input("Password:")
        sisa = MAKS_PERCOBAAN - percobaan

        if usn == USERNAME and pw == PASSWORD:
            print("LOGIN BERHASIL")
            return True 
        print(f"Username/Password salah silahkan coba lagi, Sisa Percobaan: {sisa}\n")
print()

#menu
import os
import csv
import shutil
import math

NAMA_FILE = "e-commerce_csc.csv"

def baca_dataset(nama_file):
    with open(nama_file, newline="", encoding="utf-8-sig")as file:
        pembaca = csv.dictreader(file)
        kolom = pembaca.fieldnames
        data = list(pembaca)
    for wajib in ("ID", "DISCOUNT_OFFERED", "CUSTOMER_SATISFACTION"):
        if wajib not in kolom:
            raise ValueError(f"Kolom {wajib} tidak ditemukan dalam dataset")
    return kolom, data

def simpan_dataset(nama_file, kolom, data):
    backup = nama_file.replace(".csv", "") + "_backup.csv"


    with open(nama_file, "w", newline="", encoding="utf-8-sig") as file:
        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(data)

    return backup

KOLOM_WAJIB = ("DISCOUNT_OFFERED", "CUSTOMER_SATISFACTION")
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
        id_baris = baris["ID"]
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

