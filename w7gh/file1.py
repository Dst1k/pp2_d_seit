f = open("sample.txt", "x")
with open("sample.txt","a") as f:
    f.write("Sample chetam")

with open("sample.txt") as f:
    print(f.read())