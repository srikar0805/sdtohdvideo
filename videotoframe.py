import os
import cv2

# Function to resize frame to specified resolution
def resize_frame(frame, target_resolution):
    return cv2.resize(frame, target_resolution)

# Input and output folders
input_folder = 'input_videos'
output_folder = 'resized_frames'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Target resolution
target_resolution = (640, 360)

# Iterate over all video files in the input folder
for video_file in os.listdir(input_folder):
    # Check if file is a video file
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        # Open video capture object
        cap = cv2.VideoCapture(os.path.join(input_folder, video_file))

        # Check if the video file is opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open video file '{video_file}'.")
            continue

        frame_count = 0

        # Read and process each frame
        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if frame is read successfully
            if not ret:
                break

            # Resize frame to target resolution
            resized_frame = resize_frame(frame, target_resolution)

            # Save resized frame to output folder
            output_file = f'{os.path.splitext(video_file)[0]}_frame_{frame_count}.jpg'
            cv2.imwrite(os.path.join(output_folder, output_file), resized_frame)

            frame_count += 1

            # Display progress
            print(f"Processed frame {frame_count} of '{video_file}'")

        # Release video capture object
        cap.release()

print("Frames resized and saved successfully.")
