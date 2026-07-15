#FILE ORAGNIZER BOT:

import os
import shutil

path = input("Enter the folder path: ")

if not os.path.exists(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)

for file in files:

    if not os.path.isfile(os.path.join(path, file)):
        continue

    filename, extension = os.path.splitext(file)

    extension = extension[1:]

    if extension == "":
        extension = "No Extension"

    folder = os.path.join(path, extension)

    if not os.path.exists(folder):
        os.makedirs(folder)

    shutil.move(
        os.path.join(path, file),
        os.path.join(folder, file)
    )

print("Files organized successfully!")