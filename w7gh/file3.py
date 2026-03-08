with open("file3.txt","w") as f:
    f.write("Some overlap text on censored text")
with open("file3.txt") as f:
    print(f.read())