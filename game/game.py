import time
from game import utils
from game import world
from game import player
this_world = world.World()
this_player = player.Player()

def game():
    while True:
        utils.clear_screen()
        this_player.display_stats()
        display_choices()
        choice = input("Enter choice: ")
        if choice == "1":
            this_player.display_inventory()
        elif choice == "2":
            this_player.current_location = this_world.travel(this_player.current_location)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

def new_game():
    utils.clear_screen()
    this_world.generate_world()
    this_player.generate_player()
    this_player.assign_location(this_world.cities[0])
    utils.clear_screen()
    print("Game successfully started!")
    time.sleep(1)
    utils.clear_screen()
    game()

def load_game():
    pass
def save_game():
    pass

def display_choices():
    print("1. View Inventory")
    print("2. Travel")
    print("3. Exit Game")