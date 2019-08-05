from PIL import Image
'''=Image.open("2.jpg")#object of Image class
#print(img.size)
#print(img.format)
area=(0,0,540,100)
cropped_img=img.crop(area)
cropped_img.show()
img.show()#shows the image in default program(eg:windows photos)'''

mar=Image.open("407.jpg")
print(mar.size)
area=(250,0,450,200)
cropped_img=mar.crop(area)
cropped_img.show()
mar2=Image.open("938.jpg")
area2=(600,100,800,300)
mar2.paste(cropped_img,area)
mar2.show()
