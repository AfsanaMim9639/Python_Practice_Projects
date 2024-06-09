name = input("Type Your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across ")
    if answer == "swim":
        print("You swam across and were eaten by alligator.")
    elif answer == "walk":
        print("You walked or many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
   answer = input("You come to a bridge. It looks like wobbly, Do you want to cross it or head back (cross/back)? ")
   if answer == "back":
       print("You can go back and lose. ")
   elif answer == "cross":
       answer = input("You cross the bridge and meet a stranger. Do you talk to him (yes/no)? ")
       if answer =="yes":
           print("You talked to the stranger and they gave you something and you WIN the game !")
       elif answer == "no":
            print("You ignore the starnger and they are ooffended and you Lose!")
       else:
           print("Not a valid option. You lose.")

   else:
       print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose")
print("Thank you for trying ", name)