import shutil
import sys

if __name__ == "__main__":
    for num in range(16):
        shutil.copyfile(sys.argv[1]+"_"+str(num)+".jpg", sys.argv[1].split("/")[len(sys.argv[1].split("/"))-1]+"_"+str(num)+".jpg")


