# This is the Image Processing Class
from ImageProperties import ImageProperties
from ImageSelection import ImageSelection
import numpy


# Completes all Image Processing and Manipulations
class ImageProcessing:
    # Image Processor Routine
    @staticmethod
    def image_processor(filepaths):
        # Initialize Variable
        sliced_img_tuple = []
        # Image Processing Pipeline <- Could be Parallel Operation
        for paths in filepaths:
            # Get Image Dimensions
            h_pixels, v_pixels = ImageProperties.image_pixels(paths)
            # Determine Pixel Slicing
            img_h_pixel_slice, img_v_pixel_slice = ImageProperties.image_dimensioning(h_pixels, v_pixels)
            # Section Image Data with Pixel Slicing
            sliced_img_tuple.append(ImageProcessing.image_slicer(paths, img_h_pixel_slice, img_v_pixel_slice))
        return sliced_img_tuple

    # Slice Image based on given dimensioning
    @staticmethod
    def image_slicer(img_path, h_slice, v_slice):
        # Initialize Variable
        img_tuple = []
        # Load Image Data to Sub Index
        img_data = ImageSelection.load_image_data(img_path)
        for col in range(1, 5):
            for row in range(1, 5):
                # Array = Data[vert_start -> vert_end, h_start -> h_end]
                img_tuple.append(
                    numpy.array(img_data[(row - 1) * v_slice:row * v_slice:1, (col - 1) * h_slice:col * h_slice:1]))
        return img_tuple
