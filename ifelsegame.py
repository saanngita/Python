print("Welcome to Treasure Island!")
move=input("You are at the center of the island. Where do you want to go? Left or Right")
move =move.lower()
if (move=="left"):
    choice=input("What do you want to do? Wait or swim")
    choice=choice.lower()
    if (choice=="wait"):
        door=input("There are three doors: Yellow, Blue, and Red. Which one will you open?")
        door=door.lower()
        if(door=="yellow"):
            print("You found the treasure! Congratulations!")
        elif(door=="red"):
            print("You are burned by fire. Game Over.")
        elif(door=="blue"):
            print("You are eaten by beasts. Game Over.")
        else:
            print("You wandered into the washroom. Game Over.")
    elif(choice=="swim"):
        print("You are attacked by a trout. Game Over.") 
    else:
        print("You made a dumb choice. Game Over.") 

elif (move=="right"):
    print("You felt in to a hole. Game Over.") 
else:
    print("You made a dumb choice. Game Over.")  
             
