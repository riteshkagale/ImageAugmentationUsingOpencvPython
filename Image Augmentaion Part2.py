import cv2
import numpy as np
import glob

Folder_name="augmented_image_part2"

def multiply_image(image,R,G,B):
    image=image*[R,G,B]
    cv2.imwrite(Folder_name+"/Multiply-"+str(R)+str(G)+str(B)+ "-" + img, image)

def gausian_blur(image,blur):
    image = cv2.GaussianBlur(image,(5,5),blur)
    cv2.imwrite(Folder_name+"/GausianBLur-"+str(blur)+ "-" + img, image)

def averageing_blur(image,shift):
    image=cv2.blur(image,(shift,shift))
    cv2.imwrite(Folder_name + "/AverageingBLur-" + str(shift) + "-" + img, image)

def median_blur(image,shift):
    image=cv2.medianBlur(image,shift)
    cv2.imwrite(Folder_name + "/MedianBLur-" + str(shift) + "-" + img, image)

def bileteralBlur(image,d,color,space):
    image = cv2.bilateralFilter(image, d,color,space)
    cv2.imwrite(Folder_name + "/BileteralBlur-"+str(d)+str(color)+str(space)+ "-" + img, image)

def erosion_image(image,shift):
    kernel = np.ones((shift,shift),np.uint8)
    image = cv2.erode(image,kernel,iterations = 1)
    cv2.imwrite(Folder_name + "/Erosion-"+str(shift) + "-" + img, image)

def dilation_image(image,shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.dilate(image,kernel,iterations = 1)
    cv2.imwrite(Folder_name + "/Dilation-" + str(shift)+ "-" + img, image)

def opening_image(image,shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(Folder_name + "/Opening-" + str(shift)+ "-" + img, image)

def closing_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(Folder_name + "/Closing-" + str(shift) + "-" + img, image)

def morphological_gradient_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(Folder_name + "/Morphological_Gradient-" + str(shift) + "-" + img, image)

def top_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite(Folder_name + "/Top_Hat-" + str(shift) + "-" + img, image)

def black_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(Folder_name + "/Black_Hat-" + str(shift) + "-" + img, image)

# image_file="image_24089.jpg"
# image=cv2.imread(image_file)

image_file = glob.glob("*.jpg")

for img in image_file:
    image = cv2.imread(img)

    # multiply_image(image,0.5,1,1)
    # multiply_image(image,1,0.5,1)
    # multiply_image(image,1,1,0.5)
    # multiply_image(image,0.5,0.5,0.5)

    # multiply_image(image,0.25,1,1)
    # multiply_image(image,1,0.25,1)
    # multiply_image(image,1,1,0.25)
    # multiply_image(image,0.25,0.25,0.25)

    # multiply_image(image,1.25,1,1)
    # multiply_image(image,1,1.25,1)
    # multiply_image(image,1,1,1.25)
    # multiply_image(image,1.25,1.25,1.25)
    #
    # multiply_image(image,1.5,1,1)
    # multiply_image(image,1,1.5,1)
    # multiply_image(image,1,1,1.5)
    # multiply_image(image,1.5,1.5,1.5)


    # gausian_blur(image,0.25)
    # gausian_blur(image,0.50)
    gausian_blur(image,1)
    # gausian_blur(image,2)
    # gausian_blur(image,4)

    # averageing_blur(image,5)
    averageing_blur(image,4)
    # averageing_blur(image,6)

    median_blur(image,3)
    # median_blur(image,5)
    # median_blur(image,7)

    # bileteralBlur(image,9,75,75)
    # bileteralBlur(image,12,100,100)
    # bileteralBlur(image,25,100,100)
    # bileteralBlur(image,40,75,75)

    # erosion_image(image,1)
    # erosion_image(image,3)
    # erosion_image(image,6)

    # dilation_image(image,1)
    # dilation_image(image,3)
    # dilation_image(image,5)

    # opening_image(image,1)
    # opening_image(image,3)
    # opening_image(image,5)

    # closing_image(image,1)
    # closing_image(image,3)
    # closing_image(image,5)

    # morphological_gradient_image(image,5)
    # morphological_gradient_image(image,10)
    # morphological_gradient_image(image,15)

    # top_hat_image(image,200)
    # top_hat_image(image,300)
    # top_hat_image(image,500)

    # black_hat_image(image,200)
    # black_hat_image(image,300)
    # black_hat_image(image,500)
