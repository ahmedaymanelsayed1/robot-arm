import cv2
from cvzone.HandTrackingModule import HandDetector
from serial import Serial

# Initialize webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7)

# Initialize serial communication
try:
    serial_port = Serial("COM3", 9600, timeout=1)
except Exception as e:
    print(f"Serial connection error: {e}")
    serial_port = None

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture frame")
        continue

    # Detect hands
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]  # Process only the first detected hand
        fingers = detector.fingersUp(hand)

        # Encode finger states into a single byte
        finger_data = sum([int(fingers[i]) << (4 - i) for i in range(5)])
        print(f"Finger data: {bin(finger_data)}")

        # Send data to Arduino
        if serial_port:
            try:
                serial_port.write(bytes([finger_data]))
            except Exception as e:
                print(f"Serial write error: {e}")

    # Display webcam image
    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
if serial_port:
    serial_port.close()