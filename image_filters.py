from PIL import Image
img1=Image.open("407.jpg")
img2=Image.open("406.jpg")
img3=img2.crop((400,0,1100,467))
r1,g1,b1=img1.split()#takes img and breaks into its channels
r2,g2,b2=img3.split()
new_img=Image.merge("RGB",(r1,g2,b2))#change r,g,b values for different filters
new_img.show()

