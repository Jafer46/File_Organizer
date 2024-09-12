### this is specificaly made for windows i don't know how it will
### behave in other operating systems

import os
import shutil

#mapping each file extension to corresponding directory or folder
fileExtensions = {
    'pdf': 'Documents',
    'doc': 'Documents',
    'docx': 'Documents',
    'mkv': 'Videos',
    'mp4': 'Videos',
    'avi': 'Videos',
    'mp3': 'Music',
    'jfif': 'Images',
    'jpg': 'Images',
    'webp': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'svg': 'Images',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executable'
}

#get the path of downloads in users
path = os.path.expanduser('~/Downloads')


def organize_files ():
    #list all file names on the folder downloads
    for filename in os.listdir(path):

        #creates the file path for latter use
        filePath = os.path.join(path, filename)

        #gets the extentions from filename
        extension = filename.split('.')[-1].lower()

        #defining target folders based on the types of extensions
        targetFolder = fileExtensions.get(extension)

        #ignore if you dont find the folder for extention
        if targetFolder == None:
            continue

        #define the target path to create the folder for extensions
        targetPath = os.path.join(path, targetFolder)

        #create the folder if it doesn't exist
        os.makedirs(targetPath, exist_ok=True)

        #move the file into the folder
        shutil.move(filePath, targetPath)




if __name__ == '__main__':
    organize_files()