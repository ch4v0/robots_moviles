#Carga de librerias necesarias 
from PIL import Image, ImageDraw

#Carga de la plantilla de color negro sobre la que se va a trabajar
image = Image.open("/home/jsanz/python/mapa/black.jpg")
pixels = image.load()
draw = ImageDraw.Draw(image)

despPixel = 10 #desplazamiento de los pixeles para generar un borde

imageWidth = 900 - despPixel #ancho máximo de la imagen teniendo en cuenta los pixeles necesarios para el reconocimiento de la pared

caja1 = [imageWidth - 466, 447], [imageWidth - 506, 448], [imageWidth - 510, 475], [imageWidth - 467, 478] #Valores de la caja 1

caja2 = [imageWidth - 266, 359], [imageWidth - 308, 361], [imageWidth - 307, 388], [imageWidth - 265, 387] #Valores de la caja 2

#Dibujo del plano del suelo, con el fondo blanco
draw.polygon([(imageWidth - 0,0 + despPixel),(imageWidth - 330, 0 + despPixel),(imageWidth - 329,167),(imageWidth - 726,174),(imageWidth - 693,857),(imageWidth - 0,870)],fill=(255,255,255,127),outline=(255,255,255,255))

#Dibujo de los objstaculos en color negro
draw.polygon([(caja1[0][0] + despPixel, caja1[0][1] + despPixel), (caja1[1][0] + despPixel, caja1[1][1] + despPixel), (caja1[2][0] + despPixel, caja1[2][1] + despPixel), (caja1[3][0] + despPixel, caja1[3][1] + despPixel)], fill=(0,0,0,0), outline=(0,0,0,0))

draw.polygon([(caja2[0][0] + despPixel, caja2[0][1] + despPixel), (caja2[1][0] + despPixel, caja2[1][1] + despPixel), (caja2[2][0] + despPixel, caja2[2][1] + despPixel), (caja2[3][0] + despPixel, caja2[3][1] + despPixel)], fill=(0,0,0,0), outline=(0,0,0,0))

#Guardado de la imagen en el directorio que se desee
image.save("/home/jsanz/python/mapa/map.jpg")

#Más info acerca de draw
#http://effbot.org/imagingbook/imagedraw.htm
