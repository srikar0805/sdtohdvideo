import os
import cv2

# Input and output folders
input_folder = 'resized_frames'
output_video = 'sdtohdvideo.mp4'

# Get the list of image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

if not image_files:
    print("No image files found in the input folder.")
    exit()

# Sort the image files based on their filenames
image_files.sort()

# Read the first image to get the dimensions
first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
height, width, channels = first_image.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
fps = 30  # Frames per second
video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Write each image to the video
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()

print(f"Video created: {output_video}")
