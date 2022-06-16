import requests
import time
import os

main =requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/main.py')

update = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/AutoUpdate.py')
  
maintext = main.text
updatetext = update.text
  
if maintext == open("main.py",'r+').read() and updatetext == open("AutoUpdate.py",'r'):
  print("You all up to date")
  time.sleep(0)
else:
  doesupdate = input("An update has been found, do you want to install it?(y/n): ")
  if doesupdate.lower() == 'n':
    pass
  else:
    print("Update installing")
    time.sleep(1)
    f = open("main.py",'w')
    f.write(maintext)
    f.close()
    f = open("AutoUpdate.py")
    f.write(updatetext)
    f.close()
    print("Update has been complete, stopping the program")
    time.sleep(1)
    os.system("python main.py")
    print("Restarting the program")
    exit()
    os.system('cls')
