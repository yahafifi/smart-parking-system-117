import cv2
video_path = r"C:\Users\Yahia\Desktop\smart-parking-system-117\utils\BLK-HDPTZ12 Security Camera Parkng Lot Surveillance Video [U7HRKjlXK-Y].mkv"
cap = cv2.VideoCapture(video_path)
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if count % 10 == 0:  # take every 10th frame
        cv2.imwrite(f"frames/frame_{count}.jpg", frame)

    count += 1
cap.release()