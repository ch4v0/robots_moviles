#Carga de librerias necesarias 
from PIL import Image, ImageDraw

#Carga de la plantilla de color negro sobre la que se va a trabajar
image = Image.open("1500x1500.jpg")
pixels = image.load()
draw = ImageDraw.Draw(image)


despPixel = 0 
grosor = 10
escala = 100

imageWidth = 1500 - despPixel 
imageHeight = 1500 - despPixel

#Dibujo del plano del suelo, con el fondo blanco
draw.rectangle([(grosor, grosor), (imageWidth - grosor, imageHeight - grosor)], fill=(255,255,255,255), outline=(255,255,255,255))

lineas_verticales=[
(1,0,1,3),
(3,0,3,1),
(3,3,3,4),
(4,1,4,4),
(5,0,5,3),
(7,1,7,11),
(8,2,8,3),
(10,1,10,3),
(14,2,14,4),
(13,3,13,4),
(12,3,12,4),
(9,3,9,4),
(6,5,6,6),
(1,5,1,7),
(10,6,10,8),
(11,7,11,8),
(12,7,12,13),
(13,6,13,11),
(14,7,14,12),
(9,8,9,9),
(6,8,6,13),
(5,8,5,11),
(2,9,2,12),
(1,8,1,14),
(14,13,14,14),
(11,11,11,13),
(10,11,10,13),
(9,11,9,12),
(8,7,8,11),
(3,11,3,12),
(4,12,4,13),
(3,13,3,14),
(5,13,5,14),
(7,13,7,14),
(9,13,9,14),
(8,12,8,13)
]

lineas_horizontales=[
(1,1,2,1),
(5,1,6,1),
(7,1,14,1),
(2,2,4,2),
(6,2,7,2),
(8,2,9,2),
(11,2,15,2),
(2,3,3,3),
(5,3,6,3),
(9,3,11,3),
(0,4,7,4),
(8,4,9,4),
(10,4,13,4),
(2,5,6,5),
(8,5,12,5),
(13,5,15,5),
(2,6,6,6),
(7,6,9,6),
(10,6,15,6),
(2,7,7,7),
(8,7,10,7),
(11,7,12,7),
(1,8,5,8),
(2,9,4,9),
(9,9,12,9),
(3,10,5,10),
(9,10,12,10),
(4,11,5,11),
(9,11,10,11),
(11,11,12,11),
(2,12,9,12),
(12,12,14,12),
(1,13,2,13),
(13,13,14,13),
(0,14,14,14)
]

n_v = len(lineas_verticales)
print("Numero de lineas verticales ", n_v)

n_h = len(lineas_horizontales)
print("Numero de lineas horizontales ", n_h)

#verticales

for linea in lineas_verticales:
	draw.rectangle([(linea[0]*escala-grosor, imageHeight - (linea[1]*escala-grosor)), (linea[2]*escala+grosor, imageHeight - (linea[3]*escala+grosor))],fill=(0,0,0,0),outline=(0,0,0,0))	

#horizontales

for linea in lineas_horizontales:
	draw.rectangle([(linea[0]*escala-grosor, imageHeight - (linea[1]*escala-grosor)), (linea[2]*escala+grosor, imageHeight - (linea[3]*escala+grosor))],fill=(0,0,0,0),outline=(0,0,0,0))	

#Guardado de la imagen en el directorio que se desee
image.save("large_maze.jpg", quality=100)

#Mas info acerca de draw
#http://effbot.org/imagingbook/imagedraw.htm
