import cv2
import sys

img = cv2.imread(sys.argv[1],0) # Load an color image in grayscale
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
