import cv2

# Replace with your ESP32-CAM stream URL
esp32_cam_url = "http://192.168.24.63/capture"

# Open the video stream
cap = cv2.VideoCapture(esp32_cam_url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Display the video stream
    cv2.imshow("ESP32-CAM Stream", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
