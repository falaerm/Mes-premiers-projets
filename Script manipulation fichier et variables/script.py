import os

folder_path = "/python/fifi"

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)