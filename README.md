# Sudoku Solver


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.


## Spesifikasi

#### Spesifikasi untuk program yang dibuat :
| No | Spesifikasi Program | Jenis |
| ---- | ---- | ---- |
| 1 | Program dibuat dalam bahasa Python | Wajib |
| 2 | Program menerima input berupa file eksternal yang berisi matriks area permainan (disediakan pada repository) dengan lambang '#' yang menandai area belum diketahui nomornya | Wajib |
| 3 | Program melengkapi area-area yang nomornya belum diketahui, strategi dan heuristik yang digunakan dibebaskan dan menjadi salah satu komponen penilaian. **Pencarian solusi harus dibuat sendiri algoritmanya**. | Wajib |
| 4 | Tuliskan hasil dari sepesifikasi (3) pada command prompt/terminal dan simpan dalam file eksternal. Buatlah agar mudah dibaca | Wajib |
| 5 | Tuliskan semua koordinat dari area bernomor 5, tuliskan pada command prompt/terminal dan simpan pada file eksternal yang sama dengan spesifikasi nomor (4). Koordinat dituliskan setelah area permainan | Wajib |
| 6 | Program dapat membaca inputan dari gambar. **Program hanya perlu dapat membaca gambar spesifik yang ada pada repository**. Library yang digunakan dibebaskan dan tidak ada batasan. | Bonus |
| 7 | Program diletakkan pada directory src, kemudian file pengujian diletakkan pada directory test, dan hasil pengujian berupa screenshot diletakkan pada directory result | Wajib |
| 8 | Program dikejakan secara individu, Anda boleh mencari referensi dari manapun namun tidak diperkenankan bekerja sama | Wajib |

#### Edit file readme setelah fork repository ini sehingga mencakup :
| No | Spesifikasi |
| ---- | ---- |
| 1 | Cara penggunaan program, seperti cara untuk kompilasi serta command yang dapat diterima program |
| 2 | Strategi pencarian solusi yang digunakan dan alasan penggunaannya secara lengkap, termasuk kompleksitas algoritmanya | 
| 3 | Apabila mengerjakan bonus, tuliskan library yang digunakan serta alasan penggunaannya dan kelebihan serta kekurangnnya menurut Anda |
| 4 | Tuliskan referensi (berupa link atau judul buku beserta halamannya) yang membantu Anda dalam mengerjakan tugas ini |


## Komponen Penilaian 
| No | Komponen |
| ---- | ---- |
| 1 | Kebenaran program dan fungsionalitasnya |
| 2 | Algoritma yang digunakan beserta alasan penggunaannya | 
| 3 | AKerapihan kode dan struktur repository |
| 4 | Kejelasan dan kerapihan readme |


## Pengumpulan
Lakukan merge request hasil fork Anda ke repository ini, informasi selanjutnya mengenai demo akan diberitahukan oleh asisten.

pip install pillow
pip install tesseract