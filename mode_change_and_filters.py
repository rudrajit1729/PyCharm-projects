from PIL import Image
from PIL import ImageFilter

rudy=Image.open("2.jpg")

'''black_white=rudy.convert("L")#CMYK for printing format
black_white.show()'''
#blur=rudy.filter(ImageFilter.BLUR)
detail=rudy.filter(ImageFilter.DETAIL)
edges=rudy.filter(ImageFilter.FIND_EDGES)
#blur.show()
detail.show()
edges.show()

