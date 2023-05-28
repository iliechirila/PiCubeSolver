import cv2
import numpy as np

color_ranges = {
    'white': ([0, 0, 100], [180, 30, 255]),
    'green': ([35, 50, 50], [85, 255, 255]),
    'yellow': ([20, 100, 100], [40, 255, 255]),
    'orange': ([10, 100, 100], [20, 255, 255]),
    'red': ([0, 100, 100], [10, 255, 255]),
    'blue': ([90, 100, 100], [130, 255, 255])
}

def identify_color(hsv):
    for color, (lower, upper) in color_ranges.items():
        if np.alltrue(np.greater_equal(hsv, lower)) and np.alltrue(np.less_equal(hsv, upper)):
            return color
    return "Unknown"

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_color = hsv_frame[y, x]
        identified_color = identify_color(hsv_color)
        print(f"Clicked at position ({x}, {y}) - HSV: {hsv_color} - Identified Color: {identified_color}")

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Failed to open webcam")
    exit()

# Create a window and bind the mouse callback function
cv2.namedWindow("Color Detection")
cv2.setMouseCallback("Color Detection", mouse_callback)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the frame
    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
