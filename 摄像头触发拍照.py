import cv2
import time


cap = cv2.VideoCapture("rtsp://admin:a1234567@192.168.3.64:554//Streaming/Channels/1")  # 按照自己的摄像头IP、账号、密码填写
ret, frame = cap.read()
cv2.namedWindow('摄像头预览',
                cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # WINDOW_NORMAL使您可以调整大小窗口，WINDOW_KEEPRATIO保持图像比例，没有这个cv2.resizeWindow不会生效
cv2.namedWindow('拍照预览',
                cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # WINDOW_NORMAL使您可以调整大小窗口，WINDOW_KEEPRATIO保持图像比例，没有这个cv2.resizeWindow不会生效
while ret:
    ret, frame = cap.read()
    cv2.resizeWindow("摄像头预览", 1280, 720)
    cv2.imshow("摄像头预览", frame)
    key = cv2.waitKey(1) & 0xFF  # 这里建议，若需要多个waitKey()的判断语句（比如上面程序需要3个判断），那么先将cv2.waitKey()赋值给一个变量，再用该变量去判断

    if key == ord('p'):
        name = '/home/nie/Pictures/拍照/' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                        time.localtime(time.time())) + '.jpg'  # 设置图片的文件名称和储存格式
        cv2.imwrite(name, frame, )
        cv2.resizeWindow("拍照预览", 720, 360)
        cv2.imshow('拍照预览', frame)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
