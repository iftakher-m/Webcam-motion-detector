import cv2, time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

a=0

while True:   
    a+=1
    check, frame = video.read()
    # print(check,"\n",frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # time.sleep(1)
    cv2.imshow("Capturing",gray)
    key= cv2.waitKey(1)
    print(gray)
    
    if key== ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows