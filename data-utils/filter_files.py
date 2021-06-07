from shutil import copy
from os.path import join as joinPath
from os import walk
import os
import pandas as pd


filter_input_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\data_treatment_scripts\skipped_images.txt"

images_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\final_data\task_bosch-hackathon-dataset-2021_06_06_20_03_51-yolo 1.1\obj_train_data"
labels_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\final_data\task_bosch-hackathon-dataset-2021_06_06_20_03_51-yolo 1.1\obj_train_data"

filter_file_names = pd.read_table(filter_input_path, header=None)[0]
print(filter_file_names[0])

skipped_images_path = joinPath(images_path, "skipped_images")
skipped_labels_path = joinPath(images_path, "skipped_labels")
if not os.path.exists(skipped_images_path):
    os.makedirs(skipped_images_path)
if not os.path.exists(skipped_labels_path):
    os.makedirs(skipped_labels_path)

for frameNumber in filter_file_names:
    image_name = f"frame{frameNumber}.jpg"
    label_name = f"frame{frameNumber}.txt"
    try:
        os.rename(
            os.path.join(images_path, image_name),
            os.path.join(skipped_images_path, image_name),
        )
        os.rename(
            os.path.join(labels_path, label_name),
            os.path.join(skipped_labels_path, label_name),
        )
    except Exception as e:
        print(f"Error moving files {image_name} & {label_name}")

# Edit Train.txt file.
