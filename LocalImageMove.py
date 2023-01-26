import shutil
import sys

# This script copies files to current directory
# Need to add:
#   Removal of old files

if __name__ == "__main__":
    for num in range(16):
        shutil.copyfile(sys.argv[1]+"_"+str(num)+".jpg", sys.argv[1].split("/")[len(sys.argv[1].split("/"))-1]+"_"+str(num)+".jpg")


