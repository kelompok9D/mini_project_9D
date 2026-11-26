# HUBUNGAN PENGGUNAAN DISKON DENGAN TINGKAT KEPUASAN PELANGGAN MENGGUNAKAN PYTHON
program in berbasis Python yang dibuat untuk mengetahui hubungan antara diskon yang diberikan oleh sebuah E-commerce dengan tingkat kepuasan pelanggan sehingga dapat dijadikan salah satu landasan perusahaan untuk mengambil keputusan. 

## Daftar Isi
- [Latar Belakang](#latar-belakang)
- [Manfaat](#manfaat)
- [Tujuan](#tujuan)
- [Fitur Utama](#fitur-utama)
- [Metodologi](#metodologi)
- [Struktur Repositori](#struktur-repositori)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Tim Pengembang](#tim-pengembang)

## Latar Belakang
Pemberian diskon merupakan salah satu strategi bagi sebuah perusahaan E-commerce untuk meningkatkan nilai jual. Namun, belum tentu pemberian diskon itu membuat pelanggan lebih puas. Sebelum itu kita perlu memahami satu hal bahwasannya kepuasan pelanggan dapat dipengaruhi oleh beberapa faktor lain.

program ini menjawab pertanyaan : Apakah pemberian diskon itu dapat meningkatkan kepuasan pelanggan?

## Manfaat 
Program ini memiliki manfaat sebagai salah satu landasan untuk mengambil keputusan bagi sebuah perusahaan e-commerce saat ingin memberikan diskon.

## Tujuan 
program ini memiliki tujuan untuk mengetahui apakah terdapat hubungan antara besarnya diskon yang diberikan dengan tingkat kepuasan pelanggan berdasarkan dataset e-commerce.

## Fitur Utama
|Fitur|Keterangan|
| :--- | :---: |
|Login|Program menggunakan *username* dan *password* ketika ingin mengakses program, tetapi memiliki batasan 3 kali percobaan.|
|Buka Dataset| Fitur ini digunakan untuk membuka *file* dataset yang digunakan oleh program dan memeriksa ketersediaan kolom wajib.|
|*Backup*|Fitur digunakan untuk menduplikat *file* CSV sebelum diubah|
|Validasi data|Fitur ini untuk mendeteksi data kosong, bukan angka, diskon negatif, dan *rating* di luar rentang 1-5.|
|Kelola Data|Fitur ini untuk menambah, mengubah, menghapus dan menyimpan data langsung dari program|
|Analisis Statistik| Fitur ini untuk menghitung regresi linear sederhana, koefisien korelasi (r), dan koefisien determinasi|
|Laporan Otomatis| Fitur ini untuk menyimpan kesimpulan dan saran hasil pengolahan data ke dalam *file* teks|

## Metodologi 
variabel yang digunakan dalam program ini ada dua yaitu:
|Variabel|Peran|
| :--- | :---: |
|x|Variabel Bebas|
|y|Variabel Terikat|

1. Regresi Linear Sederhana
   ```text
   y = a + bx
   b = (nΣxy − ΣxΣy) / (nΣx² − (Σx)²)
   a = (Σy − b·Σx) / n
   ```
   
3. Korelasi dan Determinasi
   ```text
   r (Korelasi)  = (nΣxy − ΣxΣy) / √[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]
   R² (Determinasi ) = r²
   ```

5. Klasifikasi Korelasi
   jika korelasinya kecil dari 0,2 maka tingkat hubungannya sangat rendah. Kemudian, jika korelasinya kecil dari 0,4 dan besar dari 0,2 maka tingkat hubungannya lemah. lalu, jika korelasinya kurang dari 0,6 dan besar dari 0,4 maka tingkat hubungannya sedang. Selanjutnya jika korelasinya kurang dari 0,8 dan lebih dari 0,6 maka tingkat hubungannya adalah kuat. Kemudian yang terakhir jika korelasinya 0,8 atau lebih maka tingkat hubungannya sangat kuat.

## Struktur Repositori
1. main.py = Kode utama program
2. e-commerce_csv.csv = *File* dataset yang digunakan
3. e-commerce_csv_backup.csv = *File* cadangann yang dibuat otomatis
4. laporan_analisis_diskon.txt = *File* laporan setelah dianalisis dan disimpan
5. README.md = dokumentasi proyek

## Cara Menjalankan Program
1. pastikan *file* Python sudah terpasang.
2. pastikan *ffile* CSV e-commerce sudah berada dalam satu folder yang sama dengan *file* Python.

## Panduan Penggunaan
1. Login
   - *Username* = Nama salah satu anggota kelompok dengan huruf kapital
   - *Password* = NIM salah satu anggota kelompok
   - Ketentuan = Maksimal percobaan sebanyak tiga kali.
     
2. Menu Utama
   |Menu|Fungsi|
   | :---: | :---: |
   |Buka Dataset| Menu ini berfungsi untuk membuka dan menjalankan *file* CSV. Menu ini merupakan menu yang harus dibuka sebelum membuka menu lainnya|
   |Validasi|Menu ini berfungsi untuk memeriksa data yang ada di dalam *file* CSV sesuai ketentuan yang diberikan|
   |Kelola Data|Menu ini memiliki fungsi untuk membuka submenu untuk mengelola isi dataset|
   |Analisis Regresi dan Korelasi| Menu ini memiliki fungsi untuk menampilkan hasil pengolahan data menggunakan metode regresi linear sederhana|
   |Laporan, Kesimpulan, dan Saran| Menu ini memiliki fungsi untuk menampilkan laporan, saran dan kesimpulan dari hasil pengolahan data|
   |Keluar| Menu ini memiliki fungsi untuk kembali ke halaman login dan jika ada perubahan yang belum disimpan, maka program akan menawarkan untuk menyimpannya|

   Submenu Kelola Data :
   1. Tambah Data Baru (ID dibuat otomatis, input divalidasi)
   2. Ubah Data Berdasarkan ID 
   3. Hapus Data Berdasarkan ID, dengan Konfirmasi
   4. Hapus Semua Data (hanya header tersisa) Dengan Konfirmasi
   5. Simpan Perubahan Ke *File* CSV
   0. Kembali Ke Menu Utama

3. Alur Penggunaan yang Disarankan
   1. Login
   2. Buka dataset pada menu 1
   3. Validasi data pada menu 2
   4. Jika ingin mengelola data pilih menu 3
   5. Menampilkan hasil perhitungan data pada menu 4
   6. Menampilkan laporan pada menu 5
  
4. Keterbatasan Program
   1. Analisis terkait kepuasan pelanggan haanya menggunakan satu variabel yaitu diskon, sehingga pengaruh lain tidak ikut dihitung.
   2. Hasil menunjukkan hubungan sebab akibat.
   3. Rating Berskala 1 sampai 5.
   4. Analisis memerlukan minimal 2 data valid.
   5. Diskon dan rating pada file CSV tidak boleh sama.
   6. Program hanay membaca 1 dataset.

## Tim Pengembang
|No|Nama|NIM|
| :---: | :---: | :---: |
|1|Sayyid Nabil Ramadhan|2610932039|
|2|Dinara Savitri|2610932027|
|3|Najla Mutia Adiba|2610931008|
   





    



