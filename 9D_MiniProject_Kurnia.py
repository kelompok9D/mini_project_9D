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
          