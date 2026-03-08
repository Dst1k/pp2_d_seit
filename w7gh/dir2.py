import os

path = "project/data"

items = os.listdir(path)

for item in items:
    print(item)