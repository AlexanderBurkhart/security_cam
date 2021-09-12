import cv2
idx = 0;
arr = [];
i = 10;
while i > 0:
    cap = cv2.VideoCapture(idx)
    if cap.read()[0]:
        arr.append(idx)
        cap.release()
    idx += 1
    i -= 1
print(arr)
