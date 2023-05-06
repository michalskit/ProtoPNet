import os
import shutil

# Path to the dataset folder
dataset_path = '/home/robin/d/CUB_200_2011'
images_path = os.path.join(dataset_path, 'cropped')
images_txt_path = os.path.join(dataset_path, 'images.txt')
train_test_split_txt_path = os.path.join(dataset_path, 'train_test_split.txt')

# Creating train and test folders if they don't exist
train_path = os.path.join(dataset_path, 'train_cropped')
test_path = os.path.join(dataset_path, 'test_cropped')
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Reading image names and train_test_split information
with open(images_txt_path, 'r') as f:
    images_info = [line.strip().split(' ') for line in f.readlines()]

with open(train_test_split_txt_path, 'r') as f:
    train_test_split = [line.strip().split(' ') for line in f.readlines()]

# Mapping image IDs to their respective data
image_id_to_name = {int(image_info[0]): image_info[1] for image_info in images_info}
image_id_to_train = {int(split_info[0]): int(split_info[1]) for split_info in train_test_split}

# Splitting images into train and test folders with respective class subfolders
for image_id, image_name in image_id_to_name.items():
    is_train = image_id_to_train[image_id]
    class_name = image_name.split('/')[0]
    
    if is_train:
        class_folder = os.path.join(train_path, class_name)
    else:
        class_folder = os.path.join(test_path, class_name)

    os.makedirs(class_folder, exist_ok=True)
    
    # Copying the image to the respective train or test class folder
    src = os.path.join(images_path, image_name)
    dst = os.path.join(class_folder, image_name.split('/')[-1])
    shutil.copy(src, dst)

print("Splitting complete.")
