from IOFile import outputFile, inputFromImage, inputFromText
from solver import solve

pilihan = input("Apakah Anda ingin menerima input melalui gambar ? (y/n) ")
isImage = False
if pilihan == 'y' :
    isImage = True

num = int(input("Pilih nomor test case dari 1 sampai 4 : "))
if isImage :
    sudoku = inputFromImage(num)
else :
    sudoku = inputFromText(num)

solve(sudoku)

outputFile(sudoku, isImage, num)
