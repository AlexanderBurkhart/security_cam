import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise IOError('no cam detected')

while True:
    ret, frame = cam.read()

