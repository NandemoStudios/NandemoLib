import AutoUpdate

dev = 0

if __name__ == '__main__':
  print("You are running this file as a file, not a module... ")
  isdev = input("Would you like to enter developer mode? (y/n): ")
  if isdev.lower() == 'y':
    dev = 1
    print("Developer mode activated")
  else:
    print("Developer mode inactivated")
else:
  pass

def IsDev():
  if dev == 1:
    print("Welcome.. Dev")
  else:
    pass

IsDev()
