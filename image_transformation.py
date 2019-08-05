from PIL import Image

img=Image.open("938.jpg")
square_img=img.resize((900,900))#resized to a square
flip_img=img.transpose(Image.FLIP_LEFT_RIGHT)#flips lft to r8
flip_img2=img.transpose(Image.FLIP_TOP_BOTTOM)#flips upside down
spin_img=img.transpose(Image.ROTATE_90)#rotates image
square_img.show()
flip_img.show()
flip_img2.show()
spin_img.show()