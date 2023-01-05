# This is the Image Selection Class
import cv2
import tkinter.filedialog
import tkinter.ttk


# Completes all path selections and image data retrievals
class ImageSelection:

    # UI File Dialog for Image Processing
    @staticmethod
    def image_selector():
        # Creates Tkinter FileDialog for file selection(s) and returns path(s)
        root = tkinter.Tk()
        root.wm_withdraw()
        file_selections = tkinter.filedialog.askopenfilenames()
        return file_selections

    # Loads Image Data with Given Path
    @staticmethod
    def load_image_data(img_path):
        return cv2.imread(img_path)
