import cv2
#import numpy as np
import random
#import math
import time
import pyautogui #để press thoát game :))
from termcolor import colored
#import keyboard

#============================================================
#os cd folder terminal !!! Không chỉnh sửa!!!
import os
#target_path cần được trỏ đúng folder chứa file python
target_path = r"C:\Users\NGOC DUNG\OneDrive - Hanoi University of Mining and Geology\A_HUMG_code\KHDL\btl"
current_path = os.getcwd()
if current_path != target_path:
    try:
        os.chdir(target_path)
        print(f"Đã chuyển đến {target_path}")
    except FileNotFoundError:
        print(f"Không tìm thấy đường dẫn: {target_path}")
    except PermissionError:
        print(f"Không có quyền truy cập đến {target_path}")
else:
    print("Đã ở trong đúng thư mục.")
print('\n')
#============================================================


#update: tăng dần tốc độ 
'''
#để con trỏ chuột tại đây 

'''

# Hiển thị thông báo
pyautogui.alert('''
Flappy Face 🙂 được tạo ra dựa trên tựa game Flappy Bird 🐦, sử dụng Cascade Classifier haarcascade_frontalface_default (Nhận diện khuôn mặt). Người chơi sử dụng khuôn mặt của mình để di chuyển qua các chướng ngại vật sao cho ô vuông đỏ (khuôn mặt) không chạm vào chướng ngại vật, khi đó sẽ được +1 điểm và tốc độ chạy cũng được tăng. Chơi đến 999 điểm sẽ có điều bất ngờ 😘
\nKhi chơi có vài lưu ý sau đây:
1. Tắt Vietkey hihihi 
2. Để trải nghệm tốt nhất hãy chơi ở nền trắng (dễ nhận diện mặt, ít bị nhầm) 
3. Nhấn phím q để thoát (hoặc chơi thua hehe) 
4. Tốc độ tăng dần, càng nhiều điểm chơi càng khó
\nLàm hết rồi thì nhấn OK để chơi nha
\n\n===================================
*Thông tin nhóm:
1. Nguyễn Ngọc Cường
2. Trần Minh Cường
3. Nguyễn Danh Duy
\n*Source: https://github.com/cuongbokreal/face-detector-haarcascade
''', 'Giới thiệu về Flappy Face 🙂 - Nhóm Xe Tăng (KHDL K68 HUMG)')

# Kích thước cửa sổ trò chơi
window_width, window_height = 800, 600
#min_width: 600
#min_height: 400

# Mở kết nối với webcam và set kích thước frame
print(colored('\nĐang kết nối Webcam...', 'red', attrs=['bold']))
cap = cv2.VideoCapture(0)
cap.set(3, window_width)  # 3 là mã cho chiều rộng frame
cap.set(4, window_height)  # 4 là mã cho chiều cao frame
print(colored('Đã kết nối Webcam!', 'green', attrs=['bold']))

# Tạo Cascade Classifier để nhận diện khuôn mặt
faceCascade = cv2.CascadeClassifier("module/haarcascade_frontalface_default.xml")

#pau game
pause = False
#tốc độ di chuyển của chướng ngại vật (px)
speed = 5

#size chướng ngại vật (chiều ngang px)
obstacle_size = 150

# Font và kích thước văn bản
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1
font_color = (255, 255, 255)
font_thickness = 2

# Điểm số
score = 0
#biến tính toán score
cal_score = 1

#Fix chướng ngại vật gen ra sát đỉnh hoặc đáy (px)
fix_random_obstacles = 100

#resize cho khung đỏ khuôn mặt nhỏ hơn (px)
resize_rectangle_face = 15

data_obstacles = [
    {
        'x':window_width,
        'y': random.randint(0, window_height - obstacle_size - fix_random_obstacles),
        'score': cal_score
    }
] #mảng thông tin chứa x, y khoảng cách an toàn của chướng ngại vật (góc bên trái dưới cùng của ô trên)
#sau đó for loop để vẽ ra, mỗi lần for của face di chuyển x -= 1
#chướng ngại vật đi từ bên phải sang: window_width => 0 
#for loop: sinh thêm chướng ngại vật khi cnv trước window_width - 200
def resetGame(e):
    print(e)
    global pause
    global speed
    global score
    global cal_score
    global data_obstacles
    pause = False
    speed = 5
    score = 0
    cal_score = 1
    data_obstacles = [
        {
            'x':window_width,
            'y': random.randint(0, window_height - obstacle_size - fix_random_obstacles),
            'score': cal_score
        }
    ]
'''

'''
print(colored('Bắt đầu game!!!', 'green', attrs=['bold']))
while True:
    # Đọc frame từ webcam
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) #lật ngược lại cam

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
        #setting cho khung đỏ nhỏ hơn, dễ chơi hơn
        x += resize_rectangle_face
        y += resize_rectangle_face
        w -= (resize_rectangle_face +10) 
        h -= (resize_rectangle_face +10)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        for data_obstacle in data_obstacles: #vẽ các chướng ngại vật
            #ô trên
            cv2.rectangle(frame, (data_obstacle['x'], 0), (data_obstacle['x'] + obstacle_size, data_obstacle['y']), (0, 255, 0), -1)
            #ô dưới
            cv2.rectangle(frame, (data_obstacle['x'], data_obstacle['y'] + obstacle_size), (data_obstacle['x'] + obstacle_size, window_height), (0, 255, 0), -1)
            
            #trường hợp đi qua cnv
            if (x in range(data_obstacle['x'], data_obstacle['x']+(speed * 2))) and (y in range(data_obstacle['y'], data_obstacle['y']+obstacle_size) and score < data_obstacle['score']):
                #set score
                score = data_obstacle['score']
                #tạo chuong ngai vat
                cal_score = score +1
                speed += 1 #tăng speed, tăng độ khó cho game :)
                print(f'Score: {score}')
                #print(cal_score)
                data_obstacles.append(
                    {
                        'x':window_width,
                        'y': random.randint(0, window_height - obstacle_size - fix_random_obstacles),
                        'score': cal_score
                    }
                )
            
            elif data_obstacle['x'] <= speed: #gần hết (cách mép trái speed px thì xóa luôn chướng ngại vật đó)
                data_obstacles.remove(data_obstacle)
            else:
                data_obstacle['x'] -= speed #nếu chưa đi hết thì di chuyển nó sang trái theo speed

            #trường hợp đụng trúng cnv (handle )
            '''if ((x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and (y in range(0, data_obstacle['y']))) or \
                  (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and (y in range(data_obstacle[y]+obstacle_size, window_height)))):
            '''
            if ( #góc trên bên trái
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(0, data_obstacle['y'])) or
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(data_obstacle['y'] + obstacle_size, window_height))
            ) or ( #góc trên bên phải, chỉ cần chỉnh sửa biến x, y => góc mới
                (x+w in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(0, data_obstacle['y'])) or
                (x+w in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y in range(data_obstacle['y'] + obstacle_size, window_height))
            ) or( #góc dưới bên trái
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y+h in range(0, data_obstacle['y'])) or
                (x in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y+h in range(data_obstacle['y'] + obstacle_size, window_height))
            ) or ( #góc dưới bên phải
                (x+w in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y+h in range(0, data_obstacle['y'])) or
                (x+w in range(data_obstacle['x'], data_obstacle['x'] + obstacle_size) and
                y+h in range(data_obstacle['y'] + obstacle_size, window_height))
            ):
                print(colored(f'Đụng trúng chướng ngại vật, điểm số của bạn là: {score}', 'red', attrs=['bold']))
                
                #setting lại game
                speed = 0
                data_obstacles = []
                print('Nhấn phím bất kì để chơi lại')
                pause = True

                # Nhấn phím "q"
                # pyautogui.press('q')
                # pyautogui.press('enter')
                # pyautogui.alert(f'Số điểm của bạn là {score}', 'Kết quả')
                #break

    if pause == True: #Nếu game đang dừng (set pause = True khi chạm cnv)
    # Kiểm tra xem có sự kiện nhấn phím nào không
        #int(window_width-font_size)//2, int(window_height-font_size)//2
        cv2.putText(frame, f"Diem so cua ban: {score}", (180,125), font, 0.75, [255,0,0], font_thickness)
        cv2.putText(frame, f"Nhan phim bat ky de choi lai, ESC hoac Q de thoat", (50,150), font, 0.65, [255,0,0], font_thickness)
        key = cv2.waitKey(10)#waitkey trong 10 mili s
        if key == 27 or key == 113:  # 27 Esc, 113 q
            break
        elif key!=-1:
            resetGame('Chơi lại')
    #nền cho score
    cv2.rectangle(frame, (0, 0), (175, 50), (135,135,135), -1)
    # Hiển thị điểm số lên frame
    cv2.putText(frame, f"Score: {score}", (10, 30), font, font_size, font_color, font_thickness)
    # Copyright =))
    cv2.putText(frame, f"BTL KHDL", (10, 200), font, font_size, font_color, font_thickness)

    # Hiển thị frame kết quả
    cv2.imshow('Flappy Face - Cuongbok', frame)

    # Thoát khỏi vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.02) #delay time cho đỡ lag

# Giải phóng tài nguyên sau khi kết thúc
cap.release()
cv2.destroyAllWindows()