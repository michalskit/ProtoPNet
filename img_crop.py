import os
from PIL import Image

# Path to the dataset folder
dataset_path = '/home/robin/d/CUB_200_2011'
images_path = os.path.join(dataset_path, 'images')
images_txt_path = os.path.join(dataset_path, 'images.txt')
bounding_boxes_txt_path = os.path.join(dataset_path, 'bounding_boxes.txt')

# Creating the cropped images folder if it doesn't exist
cropped_path = os.path.join(dataset_path, 'cropped')
os.makedirs(cropped_path, exist_ok=True)

# Reading image names and bounding box information
with open(images_txt_path, 'r') as f:
    images_info = [line.strip().split(' ') for line in f.readlines()]

with open(bounding_boxes_txt_path, 'r') as f:
    bounding_boxes_info = [line.strip().split(' ') for line in f.readlines()]

# Mapping image IDs to their respective data
image_id_to_name = {int(image_info[0]): image_info[1] for image_info in images_info}
image_id_to_bbox = {int(bbox_info[0]): [float(x) for x in bbox_info[1:]] for bbox_info in bounding_boxes_info}

# Loading images, cropping them, and saving the cropped images
for image_id, image_name in image_id_to_name.items():
    x, y, width, height = image_id_to_bbox[image_id]
    
    # Load the image
    img_path = os.path.join(images_path, image_name)
    img = Image.open(img_path)
    
    # Crop the image
    cropped_img = img.crop((x, y, x + width, y + height))
    
    # Save the cropped image
    cropped_image_name = os.path.join(cropped_path, image_name)
    os.makedirs(os.path.dirname(cropped_image_name), exist_ok=True)
    cropped_img.save(cropped_image_name)

print("Cropping complete.")
