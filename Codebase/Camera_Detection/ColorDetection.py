import cv2
import numpy as np

selected_pixel = None
# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global selected_pixel

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pixel = (x, y)

def translate_rgb_to_color(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    # Compare the RGB values to the color intervals
    if red >= 0 and red <= 20 and green >= 0 and green <= 50 and blue >= 100 and blue <= 255:
        return "Red"
    elif red >= 40 and red <= 100 and green >= 100 and green <= 180 and blue >= 150 and blue <= 255:
        return "Orange"
    elif red >= 0 and red <= 70 and green >= 100 and green <= 255 and blue >= 0 and blue <= 70:
        return "Green"
    elif red >= 150 and red <= 255 and green >= 100 and green <= 255 and blue >= 0 and blue <= 70:
        return "Blue"
    elif red >= 150 and red <= 255 and green >= 150 and green <= 255 and blue >= 150 and blue <= 255:
        return "White"
    elif red >= 120 and red <= 255 and green >= 100 and green <= 255 and blue >= 100 and blue <= 255:
        return "Yellow"

    else:
        return "Unknown"
# def is_within_interval(value, interval):
#     return interval[0][0] <= value <= interval[0][1] and interval[1][0] <= value <= interval[1][1]

# Create a window
cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', mouse_callback)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Unable to open the webcam.")
    exit()

# Start capturing frames
while True:
    # Capture frame from the webcam
    ret, frame = cap.read()

    if ret:
        # Show the frame
        cv2.imshow('Webcam', frame)

        # Check if a pixel is selected
        if selected_pixel is not None:
            x, y = selected_pixel

            # Calculate the area coordinates
            x_start = max(0, x - 3)
            y_start = max(0, y - 3)
            x_end = min(frame.shape[1], x + 3)
            y_end = min(frame.shape[0], y + 3)

            # Extract the area
            area = frame[y_start:y_end, x_start:x_end]

            # Calculate the mean RGB values
            mean_rgb = np.mean(area, axis=(0, 1))

            # Print the mean RGB values for the first 10 iterations
            print(f"X:{x}, Y:{y}; Mean RGB values: {mean_rgb}; Color: {translate_rgb_to_color(mean_rgb)}")
            selected_pixel = None

    # Exit if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
