import cv2
usr = "admin"
pwd = "[password]"
ip = "192.168.1.1" # default for access-point mode
cap = cv2.VideoCapture(f"rtsp://{usr}:{pwd}@{ip}/live/ch00_1")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
