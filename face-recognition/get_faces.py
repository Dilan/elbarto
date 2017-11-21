# coding: utf-8

import cv2
import os
import sys

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def face_cascade(name='lbp'):
    dir = os.path.dirname(__file__)
    xml_path = {
        'lbp': os.path.join(dir, 'opencv-files/lbpcascade_frontalface.xml'),
        'haar': os.path.join(dir, 'opencv-files/haarcascade_frontalface_alt.xml')
    }[name]
    return cv2.CascadeClassifier(xml_path)

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def detect_face(img):
    gray = to_gray(img)
    fc = face_cascade('lbp')
    fch = face_cascade('haar')

    # where face is "rect" - (x, y, w, h)
    faces = fc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)
    faces_h = fch.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # choose moooooore faces
    if len(faces_h) > len(faces):
        faces = faces_h

    result = []
    for face in faces:
        (x, y, w, h) = face
        result.append((gray[y:y+w, x:x+h], face))

    # [(grayImg, rect), ...]
    return result

img_path = os.path.abspath(sys.argv[1]) # test-data/test_Diana.jpg
output_path = os.path.abspath(sys.argv[2]) # output/

img = cv2.imread(img_path)
faces = detect_face(img)

print(len(faces))

for k,item in enumerate(faces):
    (x, y, w, h) = item[1]

    facePath = os.path.join(output_path, 'face_' + str(k) + '__' + os.path.basename(img_path))
    print(facePath)
    cv2.imwrite(facePath, img[y:y+w, x:x+h])
    # cv2.imshow('image' + str(k), img[y:y+w, x:x+h])

print ('Done')

# cv2.waitKey(0)
# cv2.destroyAllWindows()
