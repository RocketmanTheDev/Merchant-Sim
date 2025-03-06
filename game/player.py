from game import utils

class Player: # Handles player data
    def __init__(self):
        self.name = ""
        self.gold = 0
        self.inventory = {"Grain": 0}
        self.current_location = None

    def generate_player(self):
        self.name = input("Enter your name: ")
        print("Welcome, {}!".format(self.name))
        print("Choose your starting difficulty:")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        choice = input("Enter choice: ")
        if choice == "1":
            self.gold = 100
            self.inventory["Grain"] = 20
            self.inventory["Meat"] = 10
        elif choice == "2":
            self.gold = 50
            self.inventory["Grain"] = 10
            self.inventory["Meat"] = 10
        elif choice == "3":
            self.gold = 25
            self.inventory["Grain"] = 5
            self.inventory["Meat"] = 5
        else:
            print("Invalid choice. Starting on Normal difficulty.")
            self.gold = 50
            self.inventory["Grain"] = 10
            self.inventory["Meat"] = 10
        utils.clear_screen()

    def assign_location(self, location):
        self.current_location = location

    def display_stats(self):
        print("========== Player Stats ==========")
        print("Current Location: {}".format(self.current_location.name), end=" ")
        print("Gold: {}".format(self.gold))
        print("==================================")

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