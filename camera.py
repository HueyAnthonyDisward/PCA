import os
import cv2

# Thư mục lưu ảnh
save_dir = 'PCA/PCA/PCA/unpadded'
os.makedirs(save_dir, exist_ok=True)

# Danh sách người và cảm xúc
ids = range(1, 16)
states = ['centerlight', 'glasses', 'happy', 'leftlight',
          'noglasses', 'normal', 'rightlight', 'sad',
          'sleepy', 'surprised', 'wink']
prefix = 'subject'
suffix = '.jpg'

# Khởi động webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không thể mở webcam.")
    exit()

print("Nhấn 's' để chụp ảnh, 'q' để bỏ qua ảnh đó, 'Esc' để thoát hoàn toàn.")
print("Bắt đầu kiểm tra và chụp các ảnh còn thiếu...")

for person_id in ids:
    for state in states:
        filename = f"{prefix}{str(person_id).zfill(2)}.{state}{suffix}"
        filepath = os.path.join(save_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"\n Thiếu ảnh: {filename}")
            print("Đưa khuôn mặt bạn vào camera, sau đó nhấn 's' để chụp...")

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Không thể nhận hình ảnh từ camera.")
                    break

                # Hiển thị thông tin tên ảnh đang chụp
                display_frame = frame.copy()
                label = f"Chup: {filename} - Nhan 's' de chup, 'q' de bo qua, 'Esc' de thoat"
                cv2.putText(display_frame, label, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                display_frame = cv2.resize(display_frame, (500, 400))
                cv2.imshow("Camera", display_frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('s'):
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    resized = cv2.resize(gray, (98, 116))
                    cv2.imwrite(filepath, resized)
                    print(f" Da luu anh: {filepath}")
                    break
                elif key == ord('q'):
                    print(" Bo qua anh nay.")
                    break
                elif key == 27:  
                    print(" Da thoat chuong trinh.")
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

cap.release()
cv2.destroyAllWindows()
print("Hoan tat!")
