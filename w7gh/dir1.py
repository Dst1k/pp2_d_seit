import os
os.makedirs("project/data/raw", exist_ok=True)
with open("project/data/file.txt","w") as f:
    f.write("Something by Beatles is an awesome song")
print("Nested directories created.")