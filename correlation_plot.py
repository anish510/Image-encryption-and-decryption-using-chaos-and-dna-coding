from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def colored_image_analysis(original_image_path, encrypted_image_path, starting_pixel_position = None, ending_pixel_position = None):
    encrypted_color_image_data_1 = cv.imread(encrypted_image_path)
    original_color_image_data_2 = cv.imread(original_image_path)

    encrypted_color_image_data=cv.cvtColor(encrypted_color_image_data_1,cv.COLOR_BGR2RGB)
    original_color_image_data=cv.cvtColor(original_color_image_data_2,cv.COLOR_BGR2RGB)


    original_image_x_plus_one_y = original_color_image_data[:,1:] #(x+1,y)
    original_image_x_y_adjusted_for_x = original_color_image_data[:,:-1]
    original_image_x_y_plus_one = original_color_image_data[1:,:] #(x,y+1)
    original_image_x_y_adjusted_for_y = original_color_image_data[:-1,:]

    encrypted_image_x_plus_one_y = encrypted_color_image_data[:,1:] #(x+1,y)
    encrypted_image_x_y_adjusted_for_x = encrypted_color_image_data[:,:-1]
    encrypted_image_x_y_plus_one = encrypted_color_image_data[1:,:] #(x,y+1)
    encrypted_image_x_y_adjusted_for_y = encrypted_color_image_data[:-1,:]


    r_original_image_x_y_adjusted_for_x = original_image_x_y_adjusted_for_x[:,:,0]
    g_original_image_x_y_adjusted_for_x = original_image_x_y_adjusted_for_x[:,:,1]
    b_original_image_x_y_adjusted_for_x = original_image_x_y_adjusted_for_x[:,:,2]

    r_original_image_x_plus_one_y = original_image_x_plus_one_y[:,:,0]
    g_original_image_x_plus_one_y = original_image_x_plus_one_y[:,:,1]
    b_original_image_x_plus_one_y = original_image_x_plus_one_y[:,:,2]


    fig, ax = plt.subplots()
    ax.scatter(convert_to_1d(r_original_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(r_original_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Red",color="Red",marker="x")
    ax.scatter(convert_to_1d(g_original_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(g_original_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Green",color="g", marker=".")
    ax.scatter(convert_to_1d(b_original_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(b_original_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Blue", marker="+")
    ax.set_title('Distribution of RGB values of two horizontally adjacent pixels of plain image')
    ax.set_ylabel('Pixel gray vaue on location (x+1,y)')
    ax.set_xlabel('Pixel gray vaue on location (x,y)')
    ax.legend()


    r_encrypted_image_x_y_adjusted_for_x = encrypted_image_x_y_adjusted_for_x[:,:,0]
    g_encrypted_image_x_y_adjusted_for_x = encrypted_image_x_y_adjusted_for_x[:,:,1]
    b_encrypted_image_x_y_adjusted_for_x = encrypted_image_x_y_adjusted_for_x[:,:,2]

    r_encrypted_image_x_plus_one_y = encrypted_image_x_plus_one_y[:,:,0]
    g_encrypted_image_x_plus_one_y = encrypted_image_x_plus_one_y[:,:,1]
    b_encrypted_image_x_plus_one_y = encrypted_image_x_plus_one_y[:,:,2]

    fig, ax2 = plt.subplots()
    ax2.scatter(convert_to_1d(r_encrypted_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(r_encrypted_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Red",color="Red",marker="x")
    ax2.scatter(convert_to_1d(g_encrypted_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(g_encrypted_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Green",color="g", marker=".")
    ax2.scatter(convert_to_1d(b_encrypted_image_x_y_adjusted_for_x)[starting_pixel_position:ending_pixel_position],convert_to_1d(b_encrypted_image_x_plus_one_y)[starting_pixel_position:ending_pixel_position], label="Blue", marker="+")
    ax2.set_title('Distribution of RGB values of two horizontally adjacent pixels of cipher image')
    ax2.set_ylabel('Pixel gray vaue on location (x+1,y)')
    ax2.set_xlabel('Pixel gray vaue on location (x,y)')
    ax2.legend()


    r_original_image_x_y_adjusted_for_y = original_image_x_y_adjusted_for_y[:,:,0]
    g_original_image_x_y_adjusted_for_y = original_image_x_y_adjusted_for_y[:,:,1]
    b_original_image_x_y_adjusted_for_y = original_image_x_y_adjusted_for_y[:,:,2]

    r_original_image_x_y_plus_one = original_image_x_y_plus_one[:,:,0]
    g_original_image_x_y_plus_one = original_image_x_y_plus_one[:,:,1]
    b_original_image_x_y_plus_one = original_image_x_y_plus_one[:,:,2]

    fig1, ax3 = plt.subplots()
    ax3.scatter(convert_to_1d(r_original_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(r_original_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Red",color="Red",marker="x")
    ax3.scatter(convert_to_1d(g_original_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(g_original_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Green",color="g", marker=".")
    ax3.scatter(convert_to_1d(b_original_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(b_original_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Blue", marker="+")
    ax3.set_title('Distribution of RGB values of two vertically adjacent pixels of plain image')
    ax3.set_ylabel('Pixel gray vaue on location (x,y+1)')
    ax3.set_xlabel('Pixel gray vaue on location (x,y)')
    ax3.legend()



    r_encrypted_image_x_y_adjusted_for_y = encrypted_image_x_y_adjusted_for_y[:,:,0]
    g_encrypted_image_x_y_adjusted_for_y = encrypted_image_x_y_adjusted_for_y[:,:,1]
    b_encrypted_image_x_y_adjusted_for_y = encrypted_image_x_y_adjusted_for_y[:,:,2]

    r_encrypted_image_x_y_plus_one = encrypted_image_x_y_plus_one[:,:,0]
    g_encrypted_image_x_y_plus_one = encrypted_image_x_y_plus_one[:,:,1]
    b_encrypted_image_x_y_plus_one = encrypted_image_x_y_plus_one[:,:,2]

    fig, ax4 = plt.subplots()
    ax4.scatter(convert_to_1d(r_encrypted_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(r_encrypted_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Red",color="Red",marker="x")
    ax4.scatter(convert_to_1d(g_encrypted_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(g_encrypted_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Green",color="g", marker=".")
    ax4.scatter(convert_to_1d(b_encrypted_image_x_y_adjusted_for_y)[starting_pixel_position:ending_pixel_position],convert_to_1d(b_encrypted_image_x_y_plus_one)[starting_pixel_position:ending_pixel_position], label="Blue", marker="+")
    ax4.set_title('Distribution of RGB values of two vertically adjacent pixels of cipher image')
    ax4.set_ylabel('Pixel gray vaue on location (x,y+1)')
    ax4.set_xlabel('Pixel gray vaue on location (x,y)')
    ax4.legend()
    plt.show()
    
def convert_to_1d(array):
    return np.reshape(array, array.size)

# colored_image_analysis(r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\Baboon.tiff',r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\Baboon-baboon.tiff',1000,1500)
colored_image_analysis(r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\6.3.09.tiff',r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\encrypted_images\gray.png",1000,1500)