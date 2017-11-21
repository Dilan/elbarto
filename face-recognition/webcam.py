import cv2
import sys

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def face_cascade(name='lbp'):
    xml_path = {
        'lbp': 'opencv-files/lbpcascade_frontalface.xml',
        'haar': 'opencv-files/haarcascade_frontalface_alt.xml'
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


#
# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('./opencv-files/haarcascade_frontalface_alt.xml')
# faceCascade = cv2.CascadeClassifier(cascPath)
#
video_capture = cv2.VideoCapture(0)
#
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    faces = detect_face(frame)
    for item in faces:
        draw_rectangle(frame, item[1])


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
