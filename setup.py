import requests
import time
import os
import io
from PIL import Image

response = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/Logo-Test.png')

#img = Image.open(response.raw)
#logo = open('logo.png','w+')
#logo.write(img)
#logo.close()

## Gets the files from github
print("Retrieving the files...")
file = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/AutoUpdate.py')
file2 = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/main.py')

## Writes the files to the correct files
print("Files found, downloading them now..")
Au = open("AutoUpdate.py",'w+')
time.sleep(1)
print("Downloading: 10%")
Au.write(file.text)
time.sleep(1)
print("Downloading: 20%")
Au.close()
time.sleep(1)
print("Downloading: 50%")

Au = open("main.py",'w+')
Au.write(file2.text)
Au.close()
time.sleep(1)
print("Downloading: 100%")

print("Download complete")

## Runs the main.py function
run = input("Would you like to run main.py?(y/n): ")
if run == 'n':
  pass
else:
  os.system("python main.py")
