from random import randint

print("FIRE,LOG AND WATER GAME")
print("What's your name?")

#input name of player
my_name=input()
print("Welcome!!",my_name)

print("""Here are the rules:
        1. Fires burns log
        2. Logs makes bridge over water
        3. Water puts out fire""")
games=1
while(games==1):
    #input choice from user
    choice=input("Enter fire(f) or logs(l) or water(w): ")
    print(choice)

    option=randint(1,3)

    if(option==1):
        computer='f'
    elif(option==2):
        computer='l'
    else:
        computer='w'

    #losing and winning
    if(choice==computer):
        print("Draw")
    elif(choice=='f' and computer=='l'):
        print("You won!!")
    elif(choice=='f' and computer=='w'):
        print("You lost!!")
    elif(choice=='l' and computer=='f'):
        print("You lost!!")
    elif(choice=='l' and computer=='w'):
        print("You won!!")
    elif(choice=='w' and computer=='l'):
        print("You lost!!")
    else:
        print("You won!!")

    print("Want to play another game?")
    another=input("Enter y or n")
    if(another=='y'):
        games=1
    else:
        game=0
        break
print("Thank you for playing")


    


