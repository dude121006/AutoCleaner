import time
import pathlib
import os
import shutil

src = "C:\\Users\\manoj\\OneDrive\\Desktop\\MyNewTestFolder"
mediaDest = os.path.join(src, "Images")
docDest = os.path.join(src, "Docs")
othersDest = os.path.join(src, "Others")

fileTypesDocs = ['docx', 'pdf', 'webp', 'pptx', 'txt', 'doc', 'xlsx',\
              'png', 'svg']
fileTypesMedia = ['png', 'jfif', 'jpg', 'jpeg', 'mp4', 'mkv']




def NewDir(path):
    if not os.path.exists(path):
           os.mkdir(path)

def MoveToFolder(filepath, dest):

    NewDir(dest)
    filename = filepath.split("\\")[-1]

    if not filename in os.listdir(dest):
        try:
            shutil.move(filepath, dest)
        except:
            pass


def main(src):
    for root, dirs, files in os.walk(src):
        
        for file in files:

            _, extension = pathlib.Path(file).suffix.split('.')
            filepath = os.path.join(src, file)

            if extension in fileTypesDocs:
                MoveToFolder(filepath, docDest)
            elif extension in fileTypesMedia:
                MoveToFolder(filepath, mediaDest)
            else:
                MoveToFolder(filepath, othersDest)

if __name__ == '__main__':

    while True:

        NumberOfFiles=len(os.listdir(src))
        time.sleep(40)
    
        OldNumber = NumberOfFiles
        NumberOfFiles = len(os.listdir(src))

        if NumberOfFiles != OldNumber:
            main(src)
    