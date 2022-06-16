import requests

file = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/AutoUpdate.py')

Au = open("AutoUpdate.py",'w+')
Au.write(file.text)
Au.close()
