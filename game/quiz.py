global Points
Points = 0

def AnnouncePoints():
    global Points
    if Points == 1:
        print("you have 1 point")
    else:
        print("you have",str(Points),"Points")

##Question One##
print("Which African land mamal has the longes neck?")
print("A - Elephant")
print("B - Girrafe")
print("C - LLama")
Question1 = input("Pick A,B or C: ")
if Question1.lower() == 'b':
    print("Correct")
    Points += 1
else:
    print("Incorrect")

AnnouncePoints()

##Question Two##
print("Who created Microsoft?")
print("A - Jeff Bezos")
print("B - Bill Gates")
print("C - Garfield")
Question2 = input("Pick A,B or C: ")
if Question2.lower() == 'b':
    print("Correct")
    Points += 1
else:
    print("Incorrect")

AnnouncePoints()

##Question Three##
print("Who is the famous lasagne eating cat?")
print("A - Jimmy Neutron")
print("B - Puss In Boots")
print("C - Garfield")
Question3 = input("Pick A,B or C: ")
if Question3.lower() == 'c':
    print("Correct")
    Points += 1
else:
    print("Incorrect")

AnnouncePoints()
