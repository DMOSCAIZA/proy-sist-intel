# Importando 'pillow', 'tkinter' y 'matplotlib'.
from PIL import Image, ImageChops, ImageOps, ImageEnhance
from tkinter.filedialog import askopenfilename
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

img = None


# Creando función para invertir colores de la imagen
def invertircolores(img):
    newimg = ImageChops.invert(img)
    guardar(newimg)
    newimg.show()


# Creando función
def escalagrises():
    newimg = ImageOps.grayscale(img)
    guardar(newimg)
    newimg.show()


# Creando función para
def resaltarluces():
    newimg = ImageEnhance.Brightness(img).enhance(2)
    guardar(newimg)
    newimg.show()


# Creando función para
def contraste():
    newimg = ImageEnhance.Contrast(img).enhance(4)
    guardar(newimg)
    newimg.show()


# Creando función para
def espejo():
    newimg = ImageOps.mirror(img)
    guardar(newimg)
    newimg.show()


# Creando función para
def cambiartamaño():
    newimg = img.resize((200, 400))
    guardar(newimg)
    newimg.show()


# Creando función para
def disminuirnitidez():
    newimg = ImageEnhance.Sharpness(img).enhance(-100)
    guardar(newimg)
    newimg.show()


# Creando función para
def identidad(img):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[0]):
            arr[x, y] = img.getpixel((x, y))

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def inverso(img):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            arr[x, y] = 255 - img.getpixel((x, y))

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def umbrall(img, umbral):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) > umbral:
                arr[x, y] = 255
            else:
                arr[x, y] = 0
    return arr

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def umbrallinverso(img, umbral):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) > umbral:
                arr[x, y] = 0
            else:
                arr[x, y] = 255
    return arr

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def umbralbinario(img, umbral1, umbral2):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) > umbral1 & img.getpixel((x, y)) < umbral2:
                arr[x, y] = 0
            else:
                arr[x, y] = 255
    return arr

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def umbralbinarioinvertido(img, umbral1, umbral2):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) > umbral1 & img.getpixel((x, y)) < umbral2:
                arr[x, y] = 255
            else:
                arr[x, y] = 0
    return arr

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
def histograma(img):
    arr = img.load()
    Mx = [0] * 256
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            Mx[int(img.getpixel((x, y)))] = Mx[int(img.getpixel((x, y)))] + 1
    l = plt.plot(Mx, 'b--', linewidth=1)
    plt.xlabel("Grises")
    plt.ylabel("Cantidad")
    plt.title(r'$\mathrm{Histograma\ de\ Tono\ de\ Gris:}\ $')
    plt.grid(True)
    plt.show()
    return arr

    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)


# Creando función para
"""
def binarizacion(img, umbral):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            p = img.getpixel((x, y))
            if p > umbral:
                arr[x, y] = 255
            else:
                arr[x, y] = 0
    
    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)
"""

"""
# Creando función para
def adelgazamiento(img):
    arr = img.load()
    for x in range(1, img.size[0] - 1, 1):
        for y in range(1, img.size[1] - 1, 1):
            la = img.getpixel((x - 1, y - 1))
            lb = img.getpixel((x - 1, y))
            lc = img.getpixel((x - 1, y + 1))
            ld = img.getpixel((x, y - 1))
            le = img.getpixel((x, y))
            lf = img.getpixel((x, y + 1))
            lg = img.getpixel((x + 1, y - 1))
            lh = img.getpixel((x + 1, y))
            li = img.getpixel((x + 1, y + 1))
            if le == 0:
                if (la + ld + lg) == 255 * 3 and (lc + lf + li) == 0:
                    arr[x, y] = 255
                elif (la + lb + lc) == 0 and (lg + lh + li) == 255 * 3:
                    arr[x, y] = 255
                elif (la + ld + lg) == 0 and (lc + lf + li) == 255 * 3:
                    arr[x, y] = 255
                elif (la + lb + lc) == 255 * 3 and (lg + lh + li) == 0:
                    arr[x, y] = 255
                elif (ld + lg + lh) == 255 * 3 and (lb + le + lf) == 255 * 3:
                    arr[x, y] = 255
                elif (lf + li + lh) == 255 * 3 and (lb + le + ld) == 0:
                    arr[x, y] = 255
                elif (lb + lc + lf) == 255 * 3 and (ld + le + lh) == 0:
                    arr[x, y] = 255
                elif (lb + la + ld) == 255 * 3 and (lf + le + lh) == 0:
                    arr[x, y] = 255
                    
    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)
"""

"""
# Creando función minucia
def minucia(img):
    bif = int(0)
    ter = int(0)
    for x in range(1, img.size[0] - 1, 3):
        for y in range(1, img.size[1] - 1, 3):
            la = img.getpixel((x - 1, y - 1))
            lb = img.getpixel((x - 1, y))
            lc = img.getpixel((x - 1, y + 1))
            ld = img.getpixel((x, y - 1))
            lf = img.getpixel((x, y + 1))
            lg = img.getpixel((x + 1, y - 1))
            lh = img.getpixel((x + 1, y))
            li = img.getpixel((x + 1, y + 1))

            cn = float(0.5 * (abs(ld - la) + abs(lg - ld) + abs(lh - lg) + abs(li - lh) +
                              abs(lf - li) + abs(lc - lf) + abs(lb - lc) + abs(la - lb)))

            if cn == 3 and cn == 1:
                bif = int(bif + 1)
            else:
                ter = int(ter + 1)
    print("La cantidad de terminaciones son: " + str(ter) + " y la cantidad de bifurcaciones son: " + str(bif))
    
    img = img.convert("L")
    identidad(img)
    img.show()
    guardartif(img)
"""


# Creando función para
def guardar(newimg):
    #nombre = str(input("Digite el nombre para la foto creada: "))
    archivo = str("img-mdf.jpg")
    newimg.save(f"img-modificadas/{archivo}")


# Creando función para
def guardartif(newimg):
    #nombre = str(input("Digite el nombre para la foto creada: "))
    archivo = str("img-bdm.tif")
    newimg.save(f"img-modificadas/{archivo}")


# ---
"""
i = int(1)
ini = str("S")


while ini == "S":
    print("------> Opciones <-------")
    print("1.- Seleccionar o cambiar foto predeterminada")
    print("2.- Invertir colores")
    print("3.- Escala de Grises")
    print("4.- Resaltar luces")
    print("5.- Contraste")
    print("6.- Espejo")
    print("7.- Cambiar Tamaño")
    print("8.- Disminuir Nitidez")
    print("9.- Operador Identidad")
    print("10.- Operador Inverso o Negativo")
    print("11.- Operador Umbral")
    print("12.- Operador Umbral Inverso")
    print("13.- Operador de Interválo de Umbral Binario")
    print("14.- Operador de Interválo de Umbral Binario Invertido")
    print("15.- Histograma de Tono Gris")
    print("16.- Binarización (Solo trabaja con huella digital)")
    print("17.- Adelgaza (Solo trabaja con Imagenes Binarizadas)")
    print("18.- Minucia (Solo trabaja con imagenes Adelgazadas)")
    print("19.- Salir")
    opcion = int(input("Digite el número de la opcion a desear: "))

    # ---
    while opcion <= 0 or opcion >= 20:
        opcion = int(input("Seleccionó una opcion errónea. Digite una opcion correcta"))

    # ---
    if opcion != 19 and i == 1:
        while i == 1 and opcion != 1:
            opcion = int(input("Es necesario que seleccione una foto primero. Digite el numero 1: "))

    # ---
    if opcion == 1:
        filename = askopenfilename()
        img = Image.open(str(filename))
        i = i + 1

    # ---
    elif opcion == 2:
        invertircolores()

    # ---
    elif opcion == 3:
        escalagrises()

    # ---
    elif opcion == 4:
        resaltarluces()

    # ---
    elif opcion == 5:
        contraste()

    # ---
    elif opcion == 6:
        espejo()

    # ---
    elif opcion == 7:
        cambiartamaño()

    # ---
    elif opcion == 8:
        disminuirnitidez()

    # ---
    elif opcion == 9:
        img = img.convert("L")
        identidad(img)
        img.show()
        guardartif(img)

    # ---
    elif opcion == 10:
        img = img.convert("L")
        I = inverso(img)
        img.show()
        guardartif(img)

    # ---
    elif opcion == 11:
        img = img.convert("L")
        umb = int(input("Ingrese el valor para el umbral: "))
        I = umbrall(img, umb)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 12:
        img = img.convert("L")
        umb = int(input("Ingrese el valor para el umbral inverso: "))
        I = umbrallinverso(img, umb)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 13:
        img = img.convert("L")
        umb1 = int(input("Ingrese el valor para el primer umbral: "))
        umb2 = int(input("Ingrese el valor para el segundo umbral: "))
        I = umbralbinario(img, umb1, umb2)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 14:
        img = img.convert("L")
        umb1 = int(input("Ingrese el valor para el primer umbral invertido: "))
        umb2 = int(input("Ingrese el valor para el segundo umbral invertido: "))
        I = umbralbinarioinvertido(img, umb1, umb2)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 15:
        img = img.convert("L")
        I = histograma(img)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 16:
        img = img.convert("L")
        val = int(input("Ingrese valor(0 para maximo esclarecer y 255 para maximo oscurecer) :"))
        while 0 > val > 255:
            val = int(input("El valor debe estar entre 0 y 255. Ingrese el valor que desee: "))
        binarizacion(img, val)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 17:
        img = img.convert("L")
        adelgazamiento(img)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 18:
        img = img.convert("L")
        minucia(img)
        guardartif(img)
        img.show()

    # ---
    elif opcion == 19:
        ini = "N"

    # ---
    if opcion != 19:
        ini = str(input("¿Desea realizar otra operacion? S/N: "))

        # ---
        while ini != "S" and ini != "N":
            ini = str(input("Es necesario que escriba S o N. Digite S/N: "))
"""