from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def inputFromText(number) :
    path = "../test/tc" + str(number) + ".txt"
    fileConfig = open(path, "r")
    lines = fileConfig.readlines()
    
    sudoku = [[0 for i in range(9)] for j in range(9)]
    container = [[] for i in range(9)]
    for i,line in enumerate(lines):
        nums = line.split(' ')
        for j,num in enumerate(nums) : 
            if num[-1] == '\n' :
                num = num[0]
            
            if num == '#' :
                sudoku[i][j] = 0
            else :
                container[i].append(int(num))
                sudoku[i][j] = int(num)

        
    return sudoku


def inputFromImage(number) :
    sudoku = [[0 for i in range(9)] for j in range(9)]
    
    path = "../test/image" + str(number) + ".png"
    image = Image.open(path)

    row, col = image.size
    h, w = row/9, col/9

    for i in range(4,5) :
        for j in range(9) :
            im = image.crop((4 + w*j, 4 + h*i, w*(j+1) - 2, h*(i+1) - 3))
            im = im.convert('RGBA')
            im = im.filter(ImageFilter.MedianFilter())
            enhancer = ImageEnhance.Contrast(im)
            im = enhancer.enhance(2)

            text = pytesseract.image_to_string(im, lang = 'eng', config='--psm 6')

            if text == '' :
                text = '0'
            if text == 'S' :
                text = '5'

            number = int(text)
            sudoku[i][j] = number
    
    return sudoku

def outputFile(sudoku, isImage, num) :
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
            
            if j%3 == 2:
                if j == 8 :
                    print("")
                    f.write("\n")
                    if i % 3 == 2 and i != 8:
                        print("-------|-------|------")
                        f.write("-------|-------|------\n")
                else :
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