print("Welocome to my Computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
answer =input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("Who is the Father of the Computer?? ")
if answer.upper() == "Charles Babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer =input("What is the full form of E-Mail? ")
if answer.upper() == "Electronic Mail":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer =input(" In the virtual world, WWW stands for____ ")
if answer.lower == "world wide web":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer =input(" Who invented Compact Disc? ")
if answer == "James T. Russell":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("What is also known as a portable computer? ")
if answer == "laptop":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer =input("Name the device that is used to take a printout of a document from a computer. ")
if answer.lower() == "pinter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct! :) ")
print("You got " + str((score / 4) * 100) + " %")