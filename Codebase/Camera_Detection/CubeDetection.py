import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Unable to open the webcam.")
    exit()

# Create the main window
window = tk.Tk()
window.title("Rubik's Cube Color Extraction")

# Define the color ranges and their associated labels
color_ranges = {
    'red': ([0, 120, 70], [10, 255, 255]),
    'orange': ([15, 120, 70], [25, 255, 255]),
    'green': ([35, 120, 70], [85, 255, 255]),
    'blue': ([90, 120, 70], [130, 255, 255]),
    'yellow': ([20, 120, 70], [30, 255, 255]),
    'white': ([0, 0, 200], [180, 30, 255])
}

# Create a frame for the color images
image_frame = tk.Frame(window)
image_frame.pack()

# Create image labels for each color
image_labels = {}
row, col = 0, 0
for color in color_ranges.keys():
    image_labels[color] = tk.Label(image_frame)
    image_labels[color].grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col == 3:
        col = 0
        row += 1

# Function to update the color images
def update_color_images():
    # Capture frame from the webcam
    ret, frame = cap.read()

    if ret:
        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Extract colors and update the image labels
        for color, (lower, upper) in color_ranges.items():
            # Create a mask using the color range
            mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))

            # Apply the mask to the original frame
            color_frame = cv2.bitwise_and(frame, frame, mask=mask)

            # Convert the frame to PIL format
            color_image = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(color_image)

            # Resize the image
            pil_image = pil_image.resize((250, 250), Image.ANTIALIAS)

            # Convert the PIL image to Tkinter format
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the image label
            image_labels[color].config(image=tk_image)
            image_labels[color].image = tk_image

        # Schedule the next update
        window.after(10, update_color_images)
    else:
        # Stop updating if there's no frame
        cap.release()

# Start the color image updates
update_color_images()

# Run the GUI event loop
window.mainloop()
