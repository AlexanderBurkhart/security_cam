import socket
import cv2

ip = '127.0.0.1'
port = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((ip, port))

print('Launched camera server.')

video_name = 'detected.mp4'

while True:
    addrpair = UDPServerSocket.recvfrom(bufferSize)
    data = addrpair[0]
    address = addrpair[1]

    # get video data and create video
    height, width, _ = data[0].shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for frame in data:
        video.write(frame)
    video.release()

    # send email attaching video