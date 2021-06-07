# Importing all necessary libraries
from os import walk
import os

# Replace the path to the folder in the string
# (Copy path directly from the windows explorer/ mac finder)
folder_path = r"C:\Users\Lakshya Dev\Downloads\Work\test"


# Check if extracted_images_path
counter = 0
try:
    print('-------------------------------------------------------------------------------')
    print('--------- Renaming Files Script Execution Begin-----------')
    print(f'Source directory: {folder_path}')
    print('-------------------------------------------------------------------------------\n')
    dirPath, _, filenames = next(walk(folder_path))
    for oldFileName in filenames:
        newFileName = oldFileName.replace('.xml.txt', '.txt')
        src = os.path.join(dirPath, oldFileName)
        dst = os.path.join(dirPath, newFileName)
        os.rename(src, dst)
        print(f'Renamed {oldFileName} to ----> {newFileName}')
        counter += 1
# if not created then raise error
except Exception as e:
    print(
        f'-->Error<--: Something went wrong while trying to rename files from path: {folder_path}')
    print(f'-->Exception details: {e}')

print('-------------------------------------------------------------------------------')
print('--------- Renaming Files Script Execution End-----------')
print(f'Total no. of files renamed: {counter}')
print('-------------------------------------------------------------------------------\n')
