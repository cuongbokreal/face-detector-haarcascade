import cv2
import time

# Mở kết nối với webcam
cap = cv2.VideoCapture(0)

# Tạo Cascade Classifier để nhận diện khuôn mặt
faceCascade = cv2.CascadeClassifier("module/haarcascade_frontalface_default.xml")

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

    # In số lượng khuôn mặt được phát hiện
    print("Found {0} faces!".format(len(faces)))

    # Vẽ hình chữ nhật xung quanh khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Hiển thị frame kết quả
    cv2.imshow('Frame', frame)

    # Thoát khỏi vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.05) #delay time cho đỡ lag

# Giải phóng tài nguyên sau khi kết thúc
cap.release()
cv2.destroyAllWindows()
