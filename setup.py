import requests

file = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/AutoUpdate.py')
file2 = requests.get('https://raw.githubusercontent.com/NandemoStudios/NandemoLib/main/main.py')

Au = open("AutoUpdate.py",'w+')
Au.write(file.text)
Au.close()

Au = open("main.py",'w+')
Au.write(file2.text)
Au.close()
