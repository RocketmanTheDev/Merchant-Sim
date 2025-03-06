import time
import game.utils as utils
from game.game import new_game

def display_menu(): # Displays game title and main menu
    utils.clear_screen()
    print("===============================")
    print("      Merchant Simulator       ")
    print("===============================")
    print("1. Start New Game")
    print("2. Load Game (not implemented yet)")
    print("3. Exit")

def start_new_game():
    print("Starting new game...")
    time.sleep(1)
    new_game()

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            start_new_game()
        elif choice == "2":
            print("Loading game...")
            time.sleep(1)
        elif choice == "3":
            print("Exiting game...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()