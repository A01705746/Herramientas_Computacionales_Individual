# Importación de librerías
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

# Función de convolución con padding
def convolution(image, kernel):

    # Analiza la imágen para que en caso de que tenga color se convierte a escala de grises, de 3 dimesiones a 2
    if len(image.shape) == 3:
        print("Found 3 Channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))

    # Tamaño del filtro
    print("Kernel Shape : {}".format(kernel.shape))

    # Impresión de filtro kernel
    print('Kernel')
    for row in kernel:
            for col in row:
                print(col ,end=' ')
            print(end='\n')

    image_row, image_col = image.shape # obtiene tupla con las medidas de alto y ancho de la imagen
    kernel_row, kernel_col = kernel.shape # obtiene tupla con las medidas de alto y ancho el filtro

    output = np.zeros(image.shape) # Matriz vacía del tamaño de la imágen para guardar el resultado

    # Altura y ancho del padding en base al filtro => (filas o columnas - 1) / 2
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    # Matriz vacía del tamaño de la imágen con padding
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

    # Matriz de la imágen con padding
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    print("Padded image:")
    print(padded_image)

    # Mostrar el plot de la imágen con padding
    plt.imshow(padded_image, cmap='gray')
    plt.title("Padded Image of {}X{}".format(image_row, image_col))
    plt.show()

    #  Multiplica la matriz de image con la de kernel y devuelve la suma de esta
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])
    
    print("Output Image size : {}".format(output.shape))

    # Mostrar el plot del resultado con filtro
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel Sobel".format(kernel_row, kernel_col))
    plt.show()

    return output

if __name__ == '__main__':

    # Matriz de filtro Sobel
    filter = np.array([ [-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])

    # Para obtener la imágen se corre el programa con la siguiente línea de comando:
    # "python convolusiones.py -i Hatsune3.png"
    # la imágen tiene que estar en la misma carpeta
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path of image")
    args = vars(ap.parse_args())

    # Convierte la imagen a una matriz de 3 dimensiones rgb
    image = cv2.imread(args["image"])
    
    # Cambia la imágen a RGB para que conserve el color
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Muestra la imagen original por un plot
    plt.imshow(RGB_img, cmap='gray')
    plt.title("Original Image")
    plt.show()

    # Se llama la función convolution
    convolution(image, filter)