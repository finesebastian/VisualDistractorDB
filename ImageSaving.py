# This is the Image Saving Class
from pathlib import Path
from DBComm import DBComm
import cv2
import random


# Completes all Saving of Images
class ImageSaving:
    # Generate File Directory
    @staticmethod
    def make_directory():
        # Create Temp Directory
        temp_path = "Z:/parsed_images/"
        # Generate Directory for Saving
        Path(temp_path).mkdir(parents=True, exist_ok=True)
        # Return Directory Path
        return temp_path, str(random.getrandbits(128))

    # Generate File Name and Path
    @staticmethod
    def make_path(filepath, img_hash, index, filetype):
        # Generate Save Path
        return filepath + img_hash + "_" + str(index) + filetype

    # Save Data
    @staticmethod
    def save_image_data(image_data):
        # Iterate through LIST of parsed image SETS
        for img_sets in image_data:
            # Photo Index
            img_index = 0
            # Generate Save Location
            save_path, save_hash = ImageSaving.make_directory()
            # Iterate through SET of parsed images
            for parsed_img in img_sets:
                # Generate Image Name and Save Path
                img_save_path = ImageSaving.make_path(save_path, save_hash, img_index, ".jpg")
                # Save Parsed Image with Index at Maximum Quality
                cv2.imwrite(img_save_path, parsed_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                # Remote Save to Database
                DBComm.save_img_paths(save_hash, img_save_path, img_index)
                # Increment Index
                img_index += 1
