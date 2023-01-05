# This is the Image Properties Class
from ImageSelection import ImageSelection
import math

# Completes all Image Dimensioning and Dimension Computations
class ImageProperties:
    # Determine Slice Dimensioning (in Pixels)
    @staticmethod
    def image_dimensioning(img_h_pixels, img_v_pixels):
        # Given Slices (Squared) is 4x4
        h_pixel_slice = math.floor(img_h_pixels / 4)
        v_pixel_slice = math.floor(img_v_pixels / 4)
        return [h_pixel_slice, v_pixel_slice]

    # Extract Image Pixel Sizes
    @staticmethod
    def image_pixels(file_path):
        # Defines sector pixels to parse images (x,y)
        v_pixel, h_pixel, channels = ImageSelection.load_image_data(file_path).shape
        return [h_pixel, v_pixel]