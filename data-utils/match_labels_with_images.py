
# Replace the path to the folder in the string
# (Copy path directly from the windows explorer/ mac finder)
images_folder_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\data_archive\extracted_images\try_1"
# Replace the path to the folder in the string
# (Copy path directly from the windows explorer/ mac finder)
labels_folder_path = r"C:\Users\Lakshya Dev\Downloads\Work\Workspace\Bosch Hackathon\labelled_data\combined\labels"

# Set to False to use this file as script
# Set to True to use this file as import
useThisScriptASImport = False


def match_labels_with_images(images_dir_path, labels_dir_path, mismatched_images_archive_path='default', printFullLogs=True):
    """Match image names with label names.

    Args:
        images_dir_path (string): Path to images.
        labels_dir_path (string): Path to labels.
        mismatched_images_archive_path (string): Move mismatched images to this directory. Defaults to "<images_dir_path>/mismatched_images_archive/"
        printFullLogs (bool, optional): Print detailed logs or not. Defaults to True.

    Raises:
        OSError: If unable to create a directoy <mismatched_images_archive_path> when not found.
        Exception: If anything else goes wrong.

    Returns:
        {
            "images_dir_path": string,
            "labels_dir_path": string,
            "mismatch_count": number,
            "mismatched_images": list of names of mismatched images,
            "mismatched_images_archive_path": string,
        }
    """

    # Importing all necessary libraries
    from os import walk
    import os

    # Check if extracted_images_path
    try:
        if printFullLogs == True:
            print(
                '\n-------------------------------------------------------------------------------')
            print('--------- Match Labels With Images Script Execution Begin-----------')
            print(f'Images directory path: {images_dir_path}')
            print(f'Labels directory path: {labels_dir_path}')
            print(
                '-------------------------------------------------------------------------------\n')
        else:
            print(f'Running match_labels_with_images script ...')

        imgDirPath, _, imgFilenames = next(walk(images_dir_path))
        _, _, lblFilenames = next(walk(labels_dir_path))

        imgFilenames = [name for name in set(imgFilenames) if (
            name.endswith(".jpg"))]
        lblFilenames = [name for name in set(
            lblFilenames) if (name.endswith(".txt"))]

        mismatches = [img for img in imgFilenames if (
            f'{img.split(".jpg")[0]}.txt' not in set(lblFilenames))]
        if printFullLogs is True:
            print(
                f'All images whose corresponding labels not found: \n\n{mismatches}')

        if (len(mismatches) > 0):
            if(mismatched_images_archive_path == 'default'):
                mismatched_images_archive_path = os.path.join(
                    imgDirPath, 'mismatched_images_archive')

            if printFullLogs is True:
                print(
                    f'Mismatched images archive path : {mismatched_images_archive_path}')
            try:
                # creating a folder named data
                if not os.path.exists(mismatched_images_archive_path):
                    # if not created then raise error
                    os.makedirs(mismatched_images_archive_path)

                for mismatched_img in mismatches:
                    os.rename(os.path.join(imgDirPath, mismatched_img), os.path.join(
                        mismatched_images_archive_path, mismatched_img))
                    if printFullLogs is True:
                        print(f'Archived mismatched file {mismatched_img}')
            except OSError as e:
                if printFullLogs is True:
                    print(
                        f'Error: Creating directory failed: {mismatched_images_archive_path}')
                raise OSError(e)

        returnObj = {
            "images_dir_path": images_dir_path,
            "labels_dir_path": labels_dir_path,
            "mismatch_count": len(mismatches),
            "mismatched_images": mismatches,
            "mismatched_images_archive_path": mismatched_images_archive_path,
        }

        if printFullLogs is True:
            print(
                '\n-------------------------------------------------------------------------------')
            print('--------- Match Labels With Images Script Execution End-----------')
            print(f'Total no. of mismatched files : {len(mismatches)}')
            print(
                '-------------------------------------------------------------------------------\n')
        else:
            print('results', returnObj)
            print(f'Completed running match_labels_with_images script ...')

        return returnObj
    except Exception as e:
        if printFullLogs is True:
            print(
                '###########################################################################')
            print(
                f'-->Error<--: Something went wrong')
            print(f'-->Exception details: {e}')
            print(
                '###########################################################################')
        raise Exception(e)


##################################
##################################
if(useThisScriptASImport is not True):
    match_labels_with_images(images_dir_path=images_folder_path,
                             labels_dir_path=labels_folder_path, printFullLogs=True)
###################################
###################################
