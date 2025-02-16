import cv2
import urllib.request
import numpy as np

# Use the working URL
url = 'http://192.168.24.63/capture'

cv2.namedWindow("ESP32-CAM Stream", cv2.WINDOW_AUTOSIZE)

while True:
    try:
        # Fetch frame from ESP32-CAM
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(imgnp, -1)

        # Show frame in OpenCV window
        cv2.imshow("ESP32-CAM Stream", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"⚠️ Error: {e}")
        break

cv2.destroyAllWindows()
