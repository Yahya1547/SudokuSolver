from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def inputFromText(number) :
    # Setting path and open file
    path = "../test/tc" + str(number) + ".txt"
    fileConfig = open(path, "r")
    lines = fileConfig.readlines()
    
    # Inisialisasi array 2 dimensi untuk sudoku
    sudoku = [[0 for i in range(9)] for j in range(9)]
    
    # Traverse setiap row
    for i,line in enumerate(lines):
        nums = line.split(' ')

        # Traverse setiap kolom
        for j,num in enumerate(nums) : 
            if num[-1] == '\n' :
                num = num[0]
            
            if num == '#' :
                sudoku[i][j] = 0
            else :
                sudoku[i][j] = int(num)

        
    return sudoku


def inputFromImage(number) :
    # Inisialisasi
    sudoku = [[0 for i in range(9)] for j in range(9)]
    
    # Open image
    path = "../test/image" + str(number) + ".png"
    image = Image.open(path)

    # Mendapatkan lebar dan tinggi tiap grid
    row, col = image.size
    h, w = row/9, col/9

    for i in range(9) :
        for j in range(9) :
            # Crop grid dan memperhalus gambar untuk convert string yang lebih tepat
            im = image.crop((4 + w*j, 4 + h*i, w*(j+1) - 4, h*(i+1) - 3))
            im = im.convert('RGBA')
            im = im.filter(ImageFilter.MedianFilter())
            enhancer = ImageEnhance.Contrast(im)
            im = enhancer.enhance(2)

            # Convert string dan menangani kasus kesalahan convert untuk angka 5
            text = pytesseract.image_to_string(im, lang = 'eng', config='--psm 6')
            if text == '' :
                text = '0'
            if text[0] == 'S' :
                text = '5'
            if text[0] == '2' : # Menangani kasus khusus kesalahan convert pada angka 2 yang menjadi '2?'
                text = '2'
            if text[0] == '&' or text[0] == 'g' : # Menangani kasus khusus kesalahan convert pada angka 8
                text = '8'

            number = int(text)
            sudoku[i][j] = number
    
    return sudoku

def outputFile(sudoku, isImage, num) :
    # Setting path untuk image ataupun file sesuai dengan nomor test case
    path = "../result/"
    if isImage :
        path = path + "image" + str(num) + "-jawaban.txt"
    else :
        path = path + "tc" + str(num) + "-jawaban.txt"
        
    f = open(path, "w")
    
    print("")
    print("SUDOKU SOLVER")
    print("")
    f.write("SUDOKU SOLVER\n")
    for i in range(9) :
        for j in range(9) :
            print(" " + str(sudoku[i][j]), end="")
            f.write(" " + str(sudoku[i][j]))
            
            # Batas grid
            if j%3 == 2:

                # Grid terakhir
                if j == 8 :
                    print("")
                    f.write("\n")
                    if i % 3 == 2 and i != 8:
                        print("-------|-------|------")
                        f.write("-------|-------|------\n")
                else : # Bukan grid terakhir
                    print(" |", end="")
                    f.write(" |")

    print("")
    print("Posisi nomor 5 pada sudoku : ")
    f.write("\n")
    f.write("Posisi nomor 5 pada sudoku : \n")
    for i in range(9) :
        for j in range(9) :
            if sudoku[i][j] == 5 :
                print("(" + str(i+1) + "," + str(j+1) + ")")
                f.write("(" + str(i+1) + "," + str(j+1) + ")\n")

    f.close()