import requests
import time
import os

def CheckUpdate():
  main =requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/main.py')
    
  maintext = main.text
    
  if maintext == open("main.py",'r').read():
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
      print("Writing the update")
      time.sleep(1)
      f.write(maintext)
      print("Fisnishing the update up")
      time.sleep(1)
      f.close()
      print("Update has been complete, stopping the program")
      time.sleep(1)
      os.system("python main.py")
      print("Restarting the program")
      exit()
      os.system('cls')
