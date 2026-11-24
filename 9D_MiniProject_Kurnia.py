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

def simpan_data(nama_file, kolom, data):
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

