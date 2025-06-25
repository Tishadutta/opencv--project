import cv2
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('D:/PYTHON/pythonbasicsprogram/open--cvproject/rainbow.jpg')

# Check if the image loaded properly
if img is None:
    print("Error: Image not loaded. Check the path.")
else:
    print("Image loaded successfully.")

    # Show original image
    plt.imshow(img)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    plt.show()

    # Apply threshold
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

    # Show thresholded image
    plt.imshow(thresh1, cmap='gray')
    plt.title("Thresholded Image")
    plt.axis('off')
    plt.show()

    # Print maximum pixel value
    print("Max pixel value:", img.max())


