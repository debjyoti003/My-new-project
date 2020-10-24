import cv2

def image_resize(image):
    img = cv2.imread(image)
    resized_image = cv2.resize(img, (650, 1000))
    cv2.imwrite("New resized.jpg", resized_image)
    return resized_image

image_resize("Passport size pic.jpg")

