import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
    print('Matriz')
    for row in image:
        for col in row:
            print(col ,end=' ')
        print(end='\n')

    print('\n')
    print('Kernel')
    
    for row in kernel:
            for col in row:
                print(col ,end=' ')
            print(end='\n')

    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    output = np.zeros(image.shape)

    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)

    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()

    return output

if __name__ == '__main__':

    image = np.array([  [1,2,3,4,5,6],
                        [7,8,9,10,11,12],
                        [0,0,1,16,17,18],
                        [0,1,0,7,23,24],
                        [1,7,6,5,4,3]])

    filter = np.array([ [1,1,1],
                        [0,0,0],
                        [2,10,3]])
    
    print(convolution(image, filter))