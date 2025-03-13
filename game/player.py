from game import utils

class Player: # Handles player data
    def __init__(self):
        self.name = ""
        self.gold = 0
        self.inventory = {"grain": 0}
        self.current_location = None

    def generate_player(self):
        self.name = input("Enter your name: ")
        print("Welcome, {}!".format(self.name))
        self.gold = 100
        self.inventory["grain"] = 20
        self.inventory["meat"] = 10
        utils.clear_screen()

    def assign_location(self, location):
        self.current_location = location

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print("{}: {}".format(item, quantity))

    def add_to_inventory(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount

    def remove_from_inventory(self, item, amount):
        if item in self.inventory:
            if self.inventory[item] >= amount:
                self.inventory[item] -= amount
            else:
                print("Not enough {} in inventory.".format(item))
        else:
            print("Item not found in inventory.")