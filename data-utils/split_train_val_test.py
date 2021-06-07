def split_data(images_dir_path, labels_dir_path, output_dir_path, should_create_test_set=True, should_move_files=False):

    print('Splitting data into training, testing, and validation sets.')
    print(f'Output directory (out_dir) = {output_dir_path}')
    if (should_move_files is True):
        print(f'Training data will be moved to <out_dir>/train')
        print(f'Validation data will be moved to <out_dir>/val')
        print(f'Testing data will be moved to <out_dir>/test')
    else:
        print(f'Training data will be copied to <out_dir>/train')
        print(f'Validation data will be copied to <out_dir>/val')
        print(f'Testing data will be copied to <out_dir>/test')

    from shutil import copy
    from sklearn.model_selection import train_test_split
    from os.path import join as joinPath
    from os import walk
    import os

    # Gather all image file names
    imgDirPath, _, imgFilenames = next(walk(images_dir_path))
    imgFilenames = [name for name in set(imgFilenames) if (name.endswith(".jpg"))]

    # Gather all label file names
    lblDirPath, _, lblFilenames = next(walk(labels_dir_path))
    lblFilenames = list(set([name for name in set(lblFilenames) if (
        name.endswith(".txt") and not name.startswith('classes.txt'))]))

    imgFilenames.sort()
    lblFilenames.sort()

    images_train = []
    images_test = []
    labels_train = [] 
    labels_test = []

    if(should_create_test_set is True):
        # Split into training and test data
        [images_train, images_test, labels_train, labels_test] = train_test_split(
            imgFilenames, lblFilenames, test_size=0.2, random_state=42, shuffle=True)

    # Split training data into training and validation data
    [images_train, images_validate, labels_train, labels_validate] = train_test_split(
        images_train, labels_train, test_size=0.2, random_state=31, shuffle=True)

    train_data_path = joinPath(output_dir_path, 'train')
    validate_data_path = joinPath(output_dir_path, 'validate')
    test_data_path = joinPath(output_dir_path, 'test')

    splitPaths = [train_data_path, validate_data_path, test_data_path]

    data_maps = [
        {
            "name": "train",
            "images": images_train,
            "labels": labels_train,
        },        
        {
            "name": "val",
            "images": images_validate,
            "labels": labels_validate
        },
    ]

    if(should_create_test_set is True):
        data_maps.append({
            "name": "test",
            "images": images_test,
            "labels": labels_test,
        })

    try:
        for map in data_maps:
            imgPath = joinPath(output_dir_path, map['name'], "images")
            lblPath = joinPath(output_dir_path, map['name'], "labels")

            if not os.path.exists(imgPath):
                os.makedirs(imgPath)
            if not os.path.exists(lblPath):
                os.makedirs(lblPath)

            imgCount = 0
            lblCount = 0

            for img in map['images']:
                if (should_move_files is True):
                    os.renames(joinPath(imgDirPath, img), joinPath(imgPath, img))
                else:
                    copy(joinPath(imgDirPath, img), joinPath(imgPath, img))
                imgCount += 1
            if (should_move_files is True):
                print(f"Total {imgCount} {map['name']} images moved to {imgPath}")
            else:
                print(f"Total {imgCount} {map['name']} images copied to {imgPath}")

            for lbl in map['labels']:
                if (should_move_files is True):
                    os.renames(joinPath(lblDirPath, lbl), joinPath(lblPath, lbl))
                else:
                    copy(joinPath(lblDirPath, lbl), joinPath(lblPath, lbl))
                lblCount += 1
            if (should_move_files is True):
                print(f"Total {lblCount} {map['name']} labels moved to {lblPath}")
            else:
                print(f"Total {lblCount} {map['name']} labels copied to {lblPath}")
    # if not created then raise error
    except Exception as e:
        print(
            f'-->Error<--: Something went wrong while trying to split data')
        print(f'-->Exception details: {e}')
