import time
import game.utils as utils
import game.world as world
import game.player as player
import game.command as command

this_world = world.World()
this_player = player.Player()

def game():
    while True:
        utils.clear_screen()
        display_hud()  # Keep player stats separate from commands
        command_input = input("Enter command: ")
        command.process_command(command_input, this_world, this_player)

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

def display_hud():
    print("========== Player Stats ==========")
    print(f"Current Location: {this_player.current_location.name}")
    print(f"Gold: {this_player.gold}")
    print("==================================\n")
