import numpy as np
from PIL import Image

choose = input("""
1- Resmi Yükleyin
2- Resmi siyah ve beyaza çevirin
3- Resmi yatay olarak döndürün
Seçiminizi giriniz: """)
if (choose == "1"):
    choose_image = input("Resim dosyasının tam yolunu giriniz: ")
    img = Image.open(choose_image)
    print(choose_image.split("/")[-1]," resmi yüklendi")
    while True:
        choose = input("""
1- Resmi Yükleyin
2- Resmi siyah ve beyaza çevirin
3- Resmi yatay olarak döndürün
Seçiminizi giriniz: """)        
        if (choose == "1"):
            choose_image = input("Resim dosyasının tam yolunu giriniz: ")
            img = Image.open(choose_image)
            print(choose_image.split("/")[-1]," resmi yüklendi")
        elif (choose == "2"):
            img = Image.open(choose_image)
            pix = np.array(img)
            gray = lambda rgb : np.dot(rgb[... , :3] , [0.2989 , 0.5870, 0.1140]) 
            gray = gray(pix)  
            img = Image.fromarray(gray)
            img.show()
        elif (choose == "3"):
            img = Image.open(choose_image)
            pix = np.array(img)
            pix = np.flipud(pix)
            img = Image.fromarray(pix)
            img.show()
else:
    print("Resim seçmeden bu işlemi yapamazsınız")