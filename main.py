# This is the Main Class for Image Processing
import cv2
import math
import numpy
from pathlib import Path
import time
import tkinter.filedialog
import tkinter.ttk


# Extract Image Pixel Sizes
def image_pixels(file_path):
    # Defines sector pixels to parse images (x,y)
    v_pixel, h_pixel, channels = (cv2.imread(file_path)).shape
    return [h_pixel, v_pixel]


# UI File Dialog for Image Processing
def image_selector():
    # Creates Tkinter FileDialog for file selection(s) and returns path(s)
    root = tkinter.Tk()
    root.wm_withdraw()
    file_selections = tkinter.filedialog.askopenfilenames()
    return file_selections


# Determine Slice Dimensioning (in Pixels)
def image_dimensioning(img_h_pixels, img_v_pixels):
    # Given Slices (Squared) is 4x4
    h_pixel_slice = math.floor(img_h_pixels/4)
    v_pixel_slice = math.floor(img_v_pixels/4)
    return [h_pixel_slice, v_pixel_slice]


# Slice Image based on given dimensioning
def image_slicer(img_path, h_slice, v_slice):
    # Initialize Variable
    img_tuple = []
    # Load Image Data to Subindex
    img_data = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    for col in range(1, 5):
        for row in range(1, 5):
            # Array = Data[vert_start -> vert_end, h_start -> h_end]
            img_tuple.append(numpy.array(img_data[(row-1)*v_slice:row*v_slice:1, (col-1)*h_slice:col*h_slice:1]))
    return img_tuple


# Image Processor Routine
def image_processor(filepaths):
    # Initialize Variable
    sliced_img_tuple = []
    # Image Processing Pipeline <- Could be Parallel Operation
    for paths in filepaths:
        # Get Image Dimensions
        h_pixels, v_pixels = image_pixels(paths)
        # Determine Pixel Slicing
        img_h_pixel_slice, img_v_pixel_slice = image_dimensioning(h_pixels, v_pixels)
        # Section Image Data with Pixel Slicing
        sliced_img_tuple.append(image_slicer(paths, img_h_pixel_slice, img_v_pixel_slice))
    return sliced_img_tuple


# Generate File Directory
def make_directory():
    # UNIX Timestamp for Uniqueness
    timestamp = int(time.time())
    # Create Temp Directory
    temp_path = "Z:/parsed_images/" + str(timestamp)
    # Generate Directory for Saving
    Path(temp_path).mkdir(parents=True, exist_ok=True)
    # Return Directory Path
    return temp_path


# Save Data
def save_image_data(image_data):
    # Iterate through LIST of parsed image SETS
    for img_sets in image_data:
        # Photo Index
        img_index = 0
        # Generate Save Location
        save_path = make_directory()
        # Iterate through SET of parsed images
        for parsed_img in img_sets:
            # Save Parsed Image with Index at Maximum Quality
            cv2.imwrite(save_path + "/" + (str(img_index) + ".jpg"), parsed_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
            # Increment Index
            img_index += 1


# Main Function for Processing
if __name__ == '__main__':
    # Select Image(s)
    file_paths = image_selector()
    # Process Selected Image(s)
    processed_images = image_processor(file_paths)
    # Save Data
    save_image_data(processed_images)

