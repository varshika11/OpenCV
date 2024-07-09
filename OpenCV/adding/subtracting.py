import cv2
import numpy as np

# Read two images of the same size
image1 = cv2.imread("D:\\downloads\\3d icon laptop wallpaper.jpg")
image2 = cv2.imread("D:\\downloads\\553530.jpg")

# Ensure both images have the same dimensions
assert image1.shape == image2.shape, "Images must have the same dimensions"

# Add the images
added_image = cv2.add(image1, image2)

# Subtract the images
subtracted_image = cv2.subtract(image1, image2)

# Save the resulting images
cv2.imwrite('added_image.jpg', added_image)
cv2.imwrite('subtracted_image.jpg', subtracted_image)

# Display the resulting images
cv2.imshow('Added Image', added_image)
cv2.imshow('Subtracted Image', subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
