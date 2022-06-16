from tkinter import *
import requests

if requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/NanTk.py') == open('NanTk.py','r').read():
  pass
else:
  f = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/NanTk.py')
  ftext = f.text
  file = open('NanTk.py','w')
  file.write(ftext)
  file.close()
  
def CreateTk(title, geometry):
  root = Tk()
  root.title(title)
  root.geometry(geometry)
  return root
