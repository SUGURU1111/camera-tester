import cv2
import time
# 创建摄像头对象（0 表示默认摄像头）
cap = cv2.VideoCapture(0)


# 判断是否成功打开
if  not cap.isOpened():
    print("摄像头打开失败！")
    exit()
print("摄像头打开成功!")
start_time = time.time()
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("读取画面失败")
        break

    key = cv2.waitKey(1)
    frame_count +=1
    current_time = time.time()

    FPS= frame_count/(current_time - start_time)
    fps_text = f"FPS: {FPS:.2f}"
    cv2.putText(
        frame,
        fps_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    cv2.imshow("Camera", frame)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()