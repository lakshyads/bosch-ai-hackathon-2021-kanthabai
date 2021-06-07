# Importing all necessary libraries
from os import walk
import cv2
import os

path_to_videos = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\test_data_unseen\abeesh_new"
extracted_images_path = r'C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\test_data_unseen\abeesh_new_extracted_frames'

# Check if extracted_images_path
try:
    # creating a folder named data
    if not os.path.exists(extracted_images_path):
        os.makedirs(extracted_images_path)
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')


_, _, filenames = next(walk(path_to_videos))
imageNumber = 2962
videoNumber = 1

for filename in filenames:
    print(
        f"------- Processing video {videoNumber} --------------------------------------------------")

    filePath = path_to_videos + '/' + filename
    print("Current file path: " + filePath)
    print("--> extracted frames: ")

    # Read the video from specified path
    cam = cv2.VideoCapture(filePath)
    currentframe = 0

    while(True):
        # reading from frame
        ret, frame = cam.read()

        if ret:
            if currentframe % 20 == 0:
                # if video is still left continue creating images
                name = extracted_images_path + \
                    '/frame' + str(imageNumber) + '.jpg'
                print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)
                imageNumber += 1

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    print(
        f"------- Video {videoNumber} processed -  ---------------------------------------------------")
    videoNumber += 1

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
