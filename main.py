from os import system
import battle
#battle sim

while True: 
    print("Welcome to my text-based battle simulator")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

    # Get input for selecting a choice
    choice = input(">> ")

    if choice == "1":
        battle.start()
    elif choice =="2":
        print("Load Game")
    elif choice == "3":
        print("Goodbye")
        exit(0)
    else: 
        system("cls")
        print("Enter a valid option. ") 