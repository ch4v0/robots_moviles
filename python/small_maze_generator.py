#Carga de librerias necesarias 
from PIL import Image, ImageDraw

#Carga de la plantilla de color negro sobre la que se va a trabajar
image = Image.open("400x400.jpg")
pixels = image.load()
draw = ImageDraw.Draw(image)

despPixel = 0 

imageWidth = 400 - despPixel 
imageHeight = 400 - despPixel

#Dibujo del plano del suelo, con el fondo blanco
draw.rectangle([(10, 10), (390, 390)], fill=(255,255,255,255), outline=(255,255,255,255))

#verticales
draw.rectangle([(90, 400), (110, 90)],fill=(0,0,0,0),outline=(0,0,0,0))
draw.rectangle([(290, 400), (310, 290)],fill=(0,0,0,0),outline=(0,0,0,0))
draw.rectangle([(290, 0), (310, 110)],fill=(0,0,0,0),outline=(0,0,0,0))

#horizontales
draw.rectangle([(90, 310), (210, 290)],fill=(0,0,0,0),outline=(0,0,0,0))
draw.rectangle([(190, 110), (310, 90)],fill=(0,0,0,0),outline=(0,0,0,0))
draw.rectangle([(190, 210), (400, 190)],fill=(0,0,0,0),outline=(0,0,0,0))


#Guardado de la imagen en el directorio que se desee
image.save("small_maze_400x400.jpg", quality=100)

#Mas info acerca de draw
#http://effbot.org/imagingbook/imagedraw.htm
