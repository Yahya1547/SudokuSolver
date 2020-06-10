# Sudoku Solver


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.

## Cara Penggunaan Program
### Prasyarat
Pada tugas ini, versi python yang digunakan adalah python 3. Kemudian, ada beberapa library yang perlu di-install untuk menjalankan program ini :
1. Pillow
```
pip install pillow
```
atau
```
pip3 install pillow
```
2. Pytesseract
```
pip install tesseract
```
atau
```
pip3 install tesseract
```

Untuk meng-install pytesseract hingga dapat digunakan, dapat menuju link berikut https://github.com/UB-Mannheim/tesseract/wiki dan kemudian download installer sesuai yang sesuai apakah 32 bit atau 64 bit. Setelah program terinstall, buka file "IOFile.py" pada folder src. Dan kemudian, ubah potongan kode berikut :
```
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
```
Ubah "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" menjadi tempat kalian melakukan instalasi tesseract sebelumnya.

### Jalankan Program
1. Dari root directory, buka cmd dan kemudian menuju ke directory "src". Dapat dilakukan dengan command berikut :
```
cd src
```
2. Pastikan semua prasyarat telah terinstall dengan baik. Kemudian, jalankan program main.py pada src dengan command berikut :
```
python main.py
```
atau
```
python3 main.py
```
3. Kemudian, masukkan inputan sesuai dengan perintah yang ada pada program.

4. Hasil sudoku solver dapat dilihat pada folder result.

Notes : Untuk saat ini, file test case yang disediakan masing-masing 4 untuk file image ataupun file text, sesuai dengan test case default yang diberikan. Jika ingin, membuat custom test case, silahkan ubah salah satu test case yang ada dengan penamaan format tetap sama, dan berada pada nomor antara 1 sampai 4. Dan untuk custom test case image, sangat disarankan untuk mengikuti format gambar pada test case default.

## Strategi Pencarian Solusi
Setelah saya mencoba beberapa pendekatan untuk menyelesaikan permainan sudoku ini, saya melihat bahwa pendekatan dengan algoritma backtracking merupakan pendekatan yang sangat cocok dan dapat digunakan di berbagai kondisi. Hal itu karena algoritma backtracking akan mencoba setiap kemungkinan solusi dengan pohon ruang status. Apabila telah sampai pada suatu state dan state tersebut ternyata sudah tidak mungkin untuk mencapai goal, maka dapat dilakukan backtrack untuk melanjutkan pencarian solusi pada pohon ruang status. Untuk kompleksitas ruang pada algoritma backtracking sangat kecil, namun untuk kompleksitas waktu nya cukup besar. Alasan saya menggunakan backtracking meskipun kompleksitas waktunya yang cukup besar adalah karena pada kasus ini, grid sudoku tidak akan bertambah besar, sehingga waktu komputasi yang dibutuhkan pun tidak akan bertambah besar secara eksponensial, sehingga kompleksitas waktu algoritma yang cukup besar tersebut dapat ditoleransi. 

## Pengerjaan Bonus
Untuk mengerjakan bonus ini, saya menggunakan 2 library yaitu pillow dan pytesseract. Alasan saya menggunakan Pillow pada pengerjaan bonus ini adalah karena pillow cukup mudah untuk di-install dan support untuk di windows dibanding openCV yang lebih sulit untuk di-install di Windows. Selain itu, pillow juga sudah cukup baik dalam melakukan tugasnya untuk processing image seperti pembacaan image, cropping image, dan juga filter image untuk memudahkan convert image to string nantinya. Sehingga penggunaan pillow sudah cukup untuk menyelesaikan bonus ini. Kelebihan pillow itu sendiri adalah karena kemudahannya dalam menginstall dan juga sudah memiliki banyak fitur yang dibutuhkan untuk melakukan image processing. Sedangkan kekurangannya adalah, pillow tidak sepopuler openCV untuk image processing, dan juga sejauh yang saya ketahui, untuk melakukan image processing untuk machine learning, orang-orang cenderung untuk menggunakan openCV karena performa yang lebih cepat dibanding pillow.  

Alasan saya menggunakan pytesseract karena memiliki kemampuan untuk melakukan OCR. Kemampuan tersebut dibutuhkan untuk mengubah gambar menjadi text. Pada kasus ini adalah untuk mengubah gambar menjadi angka. Kelebihan dari pytesseract yang saya rasakan untuk pengerjaan bonus ini adalah mudahnya untuk melakukan pengubahan dari gambar menjadi teks yang hanya tinggal menjalankan satu baris fungsi yang disediakan oleh pytesseract. Kekurangannya adalah proses instalasi yang cukup rumit dan juga perlunya pengaturan yang dilakukan pada program untuk dapat menggunakan fungsi yang tersedia pada pytesseract. 

## Referensi
1. https://auth0.com/blog/image-processing-in-python-with-pillow/
2. https://pypi.org/project/pytesseract/