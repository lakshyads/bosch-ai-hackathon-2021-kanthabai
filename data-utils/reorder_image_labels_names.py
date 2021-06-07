# Importing all necessary libraries
from os import walk
import os

# Replace the path to the folder in the string
# (Copy path directly from the windows explorer/ mac finder)
folder_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\final_data\unseen_data_new_by_abeesh\obj_train_data"


# Check if extracted_images_path
counter = 0
try:
    dirPath, _, filenames = next(walk(folder_path))
    images = [filename for filename in filenames if filename.endswith(".jpg")]
    labels = [filename for filename in filenames if filename.endswith(".txt")]
    images.sort()
    labels.sort()
    frame_number = 3629
    for i in range(0, len(images)):
        imgName = f"frame{frame_number}.jpg"
        lblName = f"frame{frame_number}.txt"

        img_src = os.path.join(dirPath, images[i])
        img_dst = os.path.join(dirPath, imgName)

        lbl_src = os.path.join(dirPath, labels[i])
        lbl_dst = os.path.join(dirPath, lblName)

        os.rename(img_src, img_dst)
        os.rename(lbl_src, lbl_dst)

        print(f"Renamed {images[i]} to ----> {imgName}")
        print(f"Renamed {labels[i]} to ----> {lblName}")
        counter += 1
        frame_number += 1
# if not created then raise error
except Exception as e:
    print(
        f"-->Error<--: Something went wrong while trying to rename files from path: {folder_path}"
    )
    print(f"-->Exception details: {e}")
