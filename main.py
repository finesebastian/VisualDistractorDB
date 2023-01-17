# This is the Main Class for Image Processing
from ImageProcessing import ImageProcessing
from ImageSelection import ImageSelection
from DBComm import DBComm
import multiprocessing

# Main Function for Processing
if __name__ == '__main__':
    # Create Threads
    par_workers = multiprocessing.Pool()
    # Select Image(s)
    file_paths = ImageSelection.image_selector()
    # Process Selected Image(s) and Save Data
    par_workers.map(ImageProcessing.image_processor, file_paths)
    # Close Worker Threads
    par_workers.close()
