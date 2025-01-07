print("Welcome to the Haunted Mansion.")
move=input("You stand infront of a spooky old mansion.Do you Enter or Run away? ")
move=move.lower()
if(move=="enter"):
    choice=input("You enter the dimly lit hallway. Do you go Left or Right?")
    choice=choice.lower()
    if(choice=="left"):
        option=input("The riddle reads: I speak without a mouth and hear without ears. Who I am? Echo")
        option=option.lower()
        if(option=="echo"):
            door=input("You see three doors: Gold, Silver, and Black. Which one do you choose.")
            door=door.lower()
            if(door=="gold"):
                print("You escaped the mansion! Congratulations!")
            elif(door=="silver"):
                print("The door locks behind you, trapping you forever. Game Over.")
            elif(door=="black"):
                print("A swarm  of bats attacks you. Game Over.")
            else:
                print("You hesitated, and the mansion collapsed on you. Game Over.")  
        else:
            print("The walls close in. You are trapped forever. Game Over.")        
    elif(choice=="right"):
        print("You fell through a trapdoorbinto a pit of spikes. Game Over.")
    else:
        print("Confused, you wandered into the darkness and vanished. Game Over.")            
elif(move=="run away"):
    print("You feld in fear. Mission failed.")
else:
    print("You hesitated too long. A ghost dragged you in. Game Over.")
print("Thank you for braving the Haunted Mansion!")





