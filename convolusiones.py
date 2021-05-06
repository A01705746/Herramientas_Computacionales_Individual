import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

# Función que multiplica la matriz de image con la de kernel y devuelve la suma de esta
def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

# Función de convolución sin padding que devuelve la matriz resultante del mismo tamaño de la matriz image
def convolution(image, kernel):

    if len(image.shape) == 3:
        print("Found 3 Channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))

    print("Kernel Shape : {}".format(kernel.shape))

    # Impresión de matriz image
    print('Kernel')
    # Impresión de filtro kernel
    for row in kernel:
            for col in row:
                print(col ,end=' ')
            print(end='\n')

    image_row, image_col = image.shape # obtiene tupla con las medidas de alto y ancho de la imagen
    kernel_row, kernel_col = kernel.shape # obtiene tupla con las medidas de alto y ancho el filtro

    output = np.zeros(image.shape) # Matriz vacía del tamaño de la imágen para guardar el resultado

    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
    # Mostrar el plot
    plt.imshow(image, cmap='gray')
    plt.title("Image of {}X{}".format(image_row, image_col))
    plt.show()

    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()

    return output

if __name__ == '__main__':

    # Matriz de filtro Sobel
    filter = np.array([ [-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])

    # obtiene la imagen de la linea de comando "python convolusiones.py -i Hatsune3.png"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path of image")
    args = vars(ap.parse_args())

    # cambia la imagen a formato numerico, matriz de 3 dimensiones rgb
    image = cv2.imread(args["image"])

    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.show()

    # Se usa el print para ver la matriz resultante
    convolution(image, filter)