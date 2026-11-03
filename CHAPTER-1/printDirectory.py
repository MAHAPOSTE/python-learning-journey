import os

path = "."

files = os.listdir(path)

print("Files and directories:")

for item in files:
    print(item)