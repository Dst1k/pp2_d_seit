import os
file_name = "sample_copy.txt"
if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully.")
else:
    print("File not found.")