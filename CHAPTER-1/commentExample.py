# Import the os module
import os

# Get the current directory
path = "."

# List all files and folders
items = os.listdir(path)

# Print directory contents
print("Directory contents:")

for item in items:
    print(item)