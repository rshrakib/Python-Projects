import cv2
import os

def pencil_sketch(image_path, output_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    invert_gray_image = cv2.bitwise_not(gray_image)

    blurred_image = cv2.GaussianBlur(invert_gray_image, (21, 21), 0)

    invert_blurred_image = cv2.bitwise_not(blurred_image)

    pencil_sketch_image = cv2.divide(gray_image, invert_blurred_image, scale = 256.0)
    cv2.imwrite(output_path, pencil_sketch_image)

    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


input_image_path = input("input image path: ")
output_image_path = os.path.splitext(input_image_path)[0]+'_sketch.jpg'
pencil_sketch(input_image_path, output_image_path)
