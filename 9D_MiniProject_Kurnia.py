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
