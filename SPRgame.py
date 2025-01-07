import random
scissor = 0
paper = 1
rock = 2
computer_action = (random.randint(0,2))
human_action = int(input("Enter a choice. 0 for scissor, 1 for paper and 2 for rock"))
if (human_action == computer_action):
    print("Both player selected same choice. Its a tie.")
elif (human_action==0 and computer_action==1):
    print("Scissor cuts paper. Human win!")
elif (human_action==0 and computer_action==2):
    print("Rock breaks scissor. Computer win!")
elif (human_action==1 and computer_action==0):
    print("Scissor cuts paper. Computer win!")
elif (human_action==1 and computer_action==2):
    print("Paper wrapp rock. Human win!")
elif (human_action==2 and computer_action==0):
    print("Rocks breaks scissor. Human win!")
elif (human_action==2 and computer_action==1):
    print("Paper wrapp rock. Computer win!")
else:
    print("invalid choice")