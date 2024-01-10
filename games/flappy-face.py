import cv2
import numpy as np
import random
import math
import time
import pyautogui #để press thoát game :))

# Hiển thị thông báo
pyautogui.alert('1. Tắt Vietkey hihihi \n2. Để trải nghệm tốt nhất hãy chơi ở nền trắng \nLàm hết rồi thì nhấn OK để chơi nha', 'Lưu ý trước khi chơi')

# Tạo Cascade Classifier để nhận diện khuôn mặt
faceCascade = cv2.CascadeClassifier("module/haarcascade_frontalface_default.xml")

# Kích thước cửa sổ trò chơi
window_width, window_height = 800, 600

# Mở kết nối với webcam và set kích thước frame
cap = cv2.VideoCapture(0)
cap.set(3, window_width)  # 3 là mã cho chiều rộng frame
cap.set(4, window_height)  # 4 là mã cho chiều cao frame

#tốc độ di chuyển của chướng ngại vật
speed = 5

#size chướng ngại vật (chiều ngang)
obstacle_size = 150

# Font và kích thước văn bản
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1
font_color = (255, 255, 255)
font_thickness = 2

# Điểm số
score = 0
cal_score = 1

#Fix chướng ngại vật grenade ra sát đỉnh hoặc đáy 
fix_random_obstacles = 100

data_obstacles = [
    {
        'x':window_width,
        'y': random.randint(0, window_height - obstacle_size - fix_random_obstacles),
        'score': cal_score
    }
] #mảng thông tin chứa x, y khoảng cách an toàn của chướng ngại vật (góc bên trái dưới cùng của ô trên)
#sau đó for loop để vẽ ra, mỗi lần for di chuyển x += 1
#chướng ngại vật đi từ bên phải sang: window_width => 0 
#for loop: sinh thêm chướng ngại vật khi cnv trước window_width - 200
'''

'''

while True:
    # Đọc frame từ webcam
    ret, frame = cap.read()

    # Chuyển đổi ảnh sang ảnh đen trắng để tăng tốc độ xử lý
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Nhận diện khuôn mặt trong ảnh đen trắng
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Vẽ hình chữ nhật xung quanh khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        for data_obstacle in data_obstacles:#vẽ các chướng ngại vật
            
            cv2.rectangle(frame, (data_obstacle['x'], 0), (data_obstacle['x'] + obstacle_size, data_obstacle['y']), (0, 255, 0), -1)
            cv2.rectangle(frame, (data_obstacle['x'], data_obstacle['y'] + obstacle_size), (data_obstacle['x'] + obstacle_size, window_height), (0, 255, 0), -1)
            
            if (x in range(data_obstacle['x'], data_obstacle['x']+(speed * 2))) and (y in range(data_obstacle['y'], data_obstacle['y']+obstacle_size) and score < data_obstacle['score']):
                #set score
                score = data_obstacle['score']
                #grenade chuong ngai vat
                cal_score = score +1
                print(score)
                #print(cal_score)
                data_obstacles.append(
                    {
                        'x':window_width,
                        'y': random.randint(0, window_height - obstacle_size - fix_random_obstacles),
                        'score': cal_score
                    }
                )
            
            elif data_obstacle['x'] <= 5: #gần hết
                data_obstacles.remove(data_obstacle)
            else:
                data_obstacle['x'] -= speed #nếu chưa đi hết thì di chuyển nó sang trái theo speed

            #trường hợp đụng trúng cnv
            '''if ((x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and (y in range(0, data_obstacle['y']))) or \
                  (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and (y in range(data_obstacle[y]+obstacle_size, window_height)))):
            '''
            if (
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(0, data_obstacle['y'])) or
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(data_obstacle['y'] + obstacle_size, window_height))
            ):
                print(f'Bạn đã thua, điểm số của bạn là: {score}')
                # Nhấn phím "q"
                pyautogui.press('q')
                break
                

    # Hiển thị điểm số lên frame
    cv2.putText(frame, f"Score: {score}", (10, 30), font, font_size, font_color, font_thickness)
    # Copyright =))
    cv2.putText(frame, f"Cuongbok", (10, 200), font, font_size, font_color, font_thickness)

    # Hiển thị frame kết quả
    cv2.imshow('Flappy Face - Cuongbok', frame)

    # Thoát khỏi vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.03) #delay time cho đỡ lag

# Giải phóng tài nguyên sau khi kết thúc
cap.release()
cv2.destroyAllWindows()
