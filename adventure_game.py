def start_game():
    # Keep starting a new adventure until the player chooses to stop.
    while True:
        # Welcome the player and introduce the quest.
        print("Welcome to the Python Adventure Game!")
        player_name = input("What is your name? ")
        print(f"\nHello, {player_name}! Your quest is to find the legendary treasure.")

        # Let the player choose where to begin.
        while True:
            print("\nWhere would you like to go?")
            print("1. Explore a dark forest")
            print("2. Enter a mysterious cave")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                forest_path()
                break
            elif choice == "2":
                cave_path()
                break
            else:
                print("That is not a valid choice. Please choose 1 or 2.")

        # Ask whether the player wants to start another adventure.
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing. Goodbye!")
                return
            else:
                print("Please answer yes or no.")


def forest_path():
    # Describe the forest and show the player's choices.
    print("\nYou enter a dark forest. The trees block most of the sunlight.")
    print("1. Follow the river")
    print("2. Climb a tree")

    # Keep asking until the player makes a valid choice.
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("You follow the river and find the legendary treasure. You win the game!")
            return
        elif choice == "2":
            print("You climb the tree, but lose your way. You do not find the treasure.")
            return
        else:
            print("That is not a valid choice. Please choose 1 or 2.")


def cave_path():
    # Describe the cave and show the player's choices.
    print("\nYou enter a mysterious cave while searching for the legendary treasure.")
    print("1. Light a torch")
    print("2. Proceed in the dark")

    # Keep asking until the player makes a valid choice.
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("The torch lights the cave. You find the legendary treasure and win the game!")
            return
        elif choice == "2":
            print("You stumble in the darkness and cannot find the treasure.")
            return
        else:
            print("That is not a valid choice. Please choose 1 or 2.")


start_game()
