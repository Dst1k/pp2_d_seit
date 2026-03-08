import shutil
shutil.copy("project/data/file.txt", "project/data/file_copy.txt")
shutil.move("project/data/file.txt", "project/data/file.txt")
print("File copied and moved successfully.")