# This is the Main Class for Image Processing
from ImageProcessing import ImageProcessing
from ImageSelection import ImageSelection
from ImageSaving import ImageSaving

# Main Function for Processing
if __name__ == '__main__':
    # Select Image(s)
    file_paths = ImageSelection.image_selector()
    # Process Selected Image(s)
    processed_images = ImageProcessing.image_processor(file_paths)
    # Save Data
    ImageSaving.save_image_data(processed_images)
