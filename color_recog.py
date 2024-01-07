import cv2
import numpy as np

def color_bgr():
    cap = cv2.VideoCapture(0)

    counter = 0
    total_avg = [0, 0, 0]

    while True:
        ret, frame = cap.read()
        height, width, _ = frame.shape

        # Define the region around the center
        center_x = width // 2
        center_y = height // 2
        sample_size = 150  # Size of sample in the middle
        sample = frame[center_y - sample_size // 2:center_y + sample_size // 2, center_x - sample_size // 2:center_x + sample_size // 2]

        # Display the frame with the region of interest
        # cv2.imshow('Original', frame)
        # cv2.imshow('Sample', sample)

        # Calculate the average color of the region in BGR and HSV
        avg_color = np.mean(sample, axis=(0, 1))
        # avg_color_hsv = cv2.cvtColor(np.uint8([[avg_color]]), cv2.COLOR_BGR2HSV)[0][0]

        if counter > 30:
            total_avg = total_avg + avg_color

        counter += 1
        # Print the average color values
        # print(counter, ". BGR:", np.round(avg_color), "HSV:", avg_color_hsv)

        
        # Exits after "counter" number of instances
        if cv2.waitKey(1) & counter >= 60:
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return total_avg/30
