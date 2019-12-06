import cv2
import numpy as np
import glob

Folder_name="augmented_image"

#RESIZE
def resize_image(image,w,h):
    image=cv2.resize(image,(w,h))
    cv2.imwrite(Folder_name + "/Resize-" + img, image)

#crop
def crop_image(image,y1,y2,x1,x2):
    image=image[y1:y2,x1:x2]
    cv2.imwrite(Folder_name+"/Crop-" + str(x1) + str(x2) + str(y1) + str(y2) + "-" + img, image)

def padding_image(image,topBorder,bottomBorder,leftBorder,rightBorder,color_of_border=[0,0,0]):
    image = cv2.copyMakeBorder(image,topBorder,bottomBorder,leftBorder,
        rightBorder,cv2.BORDER_CONSTANT,value=color_of_border)
    cv2.imwrite(Folder_name + "/padd-" + str(topBorder) + str(bottomBorder) + str(leftBorder) + str(rightBorder) + "-" + img, image)

def flip_image(image,dir):
    image = cv2.flip(image, dir)
    cv2.imwrite(Folder_name + "/flip:" + str(dir)+ "-" + img, image)

def saturation_image(image,saturation):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder_name + "/saturation-" + str(saturation) + "-" + img, image)

def gausian_blur(image,blur):
    image = cv2.GaussianBlur(image,(5,5),blur)
    cv2.imwrite(Folder_name+"/GausianBLur-"+str(blur)+ "-" + img, image)

def averageing_blur(image,shift):
    image=cv2.blur(image,(shift,shift))
    cv2.imwrite(Folder_name + "/AverageingBLur-" + str(shift) + "-" + img, image)

def median_blur(image,shift):
    image=cv2.medianBlur(image,shift)
    cv2.imwrite(Folder_name + "/MedianBLur-" + str(shift) + "-" + img, image)

def sharpen_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(Folder_name+"/Sharpen-"+ img, image)

def translation_image(image,x,y):
    rows, cols ,c= image.shape
    M = np.float32([[1, 0, x], [0, 1, y]])
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Translation:" + str(x) + str(y) + "-" + img, image)

def rotate_image(image,deg):
    rows, cols,c = image.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2), deg, 1)
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Rotate-" + str(deg) + "-" + img, image)

def transformation_image(image):
    rows, cols, ch = image.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Transformations-" + str(1) + "-" + img, image)

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[100, 10], [200, 50], [0, 150]])
    M = cv2.getAffineTransform(pts1, pts2)
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Transformations-" + str(2) + "-" + img, image)

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[100, 10], [200, 50], [30, 175]])
    M = cv2.getAffineTransform(pts1, pts2)
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Transformations-" + str(3) + "-" + img, image)

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[100, 10], [200, 50], [70, 150]])
    M = cv2.getAffineTransform(pts1, pts2)
    image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite(Folder_name + "/Transformations-" + str(4) + "-" + img, image)


###Change Image file
image_file = glob.glob("*.jpg")

for img in image_file:
    image = cv2.imread(img)

    resize_image(image, 450, 400)

    crop_image(image,100,400,0,350)#(y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image,100,400,100,450)#(y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image,0,300,0,350)#(y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image,0,300,100,450)#(y1,y2,x1,x2)(bottom,top,left,right)
    crop_image(image,100,300,100,350)#(y1,y2,x1,x2)(bottom,top,left,right)

    padding_image(image,100,0,0,0)#(y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image,0,100,0,0)#(y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image,0,0,100,0)#(y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image,0,0,0,100)#(y1,y2,x1,x2)(bottom,top,left,right)
    padding_image(image,100,100,100,100)#(y1,y2,x1,x2)(bottom,top,left,right)

    flip_image(image,0)#horizontal
    flip_image(image,1)#vertical
    flip_image(image,-1)#both

    saturation_image(image,50)
    saturation_image(image,100)

    gausian_blur(image,1)
    averageing_blur(image,4)
    median_blur(image,3)

    sharpen_image(image)

    translation_image(image,150,150)
    translation_image(image,-150,150)
    translation_image(image,150,-150)
    translation_image(image,-150,-150)

    rotate_image(image,90)
    rotate_image(image,180)
    rotate_image(image,270)

    transformation_image(image)

