import cv2
cap = cv2.VideoCapture("rtsp://admin:Alirezakarimi81*@192.168.1.107/live/ch00_1")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
