import requests
import time
import os

## Gets the files from github
print("Retrieving the files...")
file = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/AutoUpdate.py')
file2 = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/main.py')
file3 = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/NanTk.py')
time.sleep(1)

## Writes the files to the correct files
print("Files found, downloading them now..")
Au = open("AutoUpdate.py",'w+')
Au.write(file.text)
Au.close()

Au = open("main.py",'w+')
Au.write(file2.text)
Au.close()

hasTk = input("Do you want NanTk?(y/n): ")
if hasTk == 'n':
  print('NanTk has not been installed')
else:
  Au = open("NanTk.py",'w')
  Au.write(file3.text)
  Au.close()

print("Download complete")
time.sleep(1)

## Runs the main.py function
run = input("Would you like to run main.py?(y/n): ")
if run == 'n':
  pass
else:
  os.system("python main.py")
