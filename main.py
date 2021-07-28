# this program is to convert jpg files to png format.
# 1st project in Andrei's Python course in Udemy.

import sys
import os
from PIL import Image

# source_folder, target_folder = sys.argv[1], sys.argv[2]  # This to get input from command line.

# If you want to get input via the IDE replace above code with below.
source_folder, target_folder = input("Enter source directory followed by '\\' : ").split(" ")

if not os.path.isdir(target_folder):
    os.makedirs(target_folder)

for filename in os.listdir(source_folder):
    img = Image.open(f'{source_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{target_folder}{clean_name}.png', 'png')
    print("Done!")
