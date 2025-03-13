import re
import time

def process_command(command, this_world, this_player):
    command = command.lower().strip()

    # Display available commands
    if command in ["what can i do", "what can i do?", "help", "commands"]:
        list_commands()
        input("\nPress Enter to continue...")
        return

    # Open inventory
    if command in ["open inventory", "inventory"]:
        this_player.display_inventory()
        input("\nPress Enter to continue...")
        return

    # Drop or remove item from inventory
    match = re.search(r"(drop|remove) (\w+)", command)
    if match:
        remove_item(this_player, match.group(2).lower())
        input("\nPress Enter to continue...")
        return

    # Travel to a city
    if any(phrase in command for phrase in ["go to", "travel to"]):
        match = re.search(r"travel to (\w+)", command)
        if match:
            city_name = match.group(1).lower()
            city = next((c for c in this_world.cities if c.name.lower() == city_name), None)
            if city:
                this_player.current_location = city
                print(f"Traveling to {city.name}...")
                time.sleep(1)
            else:
                print("City not found.")
        return

    # List available travel locations
    if any(phrase in command for phrase in ["where can i travel", "travel locations"]):
        print("You can travel to:")
        for city in this_world.cities:
            print(f"- {city.name}")
        input("\nPress Enter to continue...")
        return

    # Enter market
    if any(phrase in command for phrase in ["go to market", "visit market", "enter market"]):
        enter_market(this_player, this_world)
        return

    # Buying items
    match = re.search(r"buy (\d+|all|max) (\w+)", command)
    if match:
        amount, item_name = match.groups()
        buy_item(this_player, item_name.lower(), amount)
        return

    # Selling items
    match = re.search(r"sell (\d+|all|max) (\w+)", command)
    if match:
        amount, item_name = match.groups()
        sell_item(this_player, item_name.lower(), amount)
        return

    # Exit market
    if "exit market" in command:
        return

    print("I didn't understand that command. Try again.")



def list_commands():
    """ Displays available commands """
    print("\nAvailable Commands:")
    print("- travel to [city] -> Travel to a different city")
    print("- where can i travel -> List available cities")
    print("- go to market / visit market -> Enter the market")
    print("- buy [item] / buy all / buy max -> Purchase an item")
    print("- sell [item] / sell all / sell max -> Sell an item")
    print("- open inventory -> View your inventory")
    print("- drop [item] / remove [item] -> Remove an item from your inventory")
    print("- exit market -> Leave the market")
    print("- what can i do? / help / commands -> Show this list\n")


def enter_market(this_player, this_world):
    while True:
        print("\n========== Market ==========")
        print(f"Current City: {this_player.current_location.name}")
        print(f"Gold: {this_player.gold}")
        print("Items available for trade:")
        city_prices = this_player.current_location.calculate_prices()
        city_stock = this_player.current_location.stock

        for index, (item, price) in enumerate(city_prices.items(), start=1):
            stock = city_stock[item]
            print(f"{index}. {item} - Price: {price} Gold | Stock: {stock}")

        command = input("Enter market command: ")
        if "exit" in command.lower():
            break
        process_command(command, this_world, this_player)


def buy_item(this_player, item_name, amount):
    city_prices = this_player.current_location.calculate_prices()
    city_stock = this_player.current_location.stock

    if item_name not in city_prices:
        print("Item not available in the market.")
        return

    if amount in ["all", "max"]:
        max_affordable = this_player.gold // city_prices[item_name]
        max_available = city_stock[item_name]
        amount = max_available if amount == "all" else min(max_affordable, max_available)
    else:
        amount = int(amount)

    total_price = city_prices[item_name] * amount
    if amount > city_stock[item_name]:
        print("Not enough stock available.")
    elif total_price > this_player.gold:
        print("Not enough gold.")
    else:
        this_player.gold -= total_price
        this_player.add_to_inventory(item_name, amount)
        city_stock[item_name] -= amount
        print(f"You bought {amount} {item_name} for {total_price} gold.")


def sell_item(this_player, item_name, amount):
    city_prices = this_player.current_location.calculate_prices()
    player_inventory = this_player.inventory

    if item_name not in player_inventory or player_inventory[item_name] <= 0:
        print("You don’t have this item.")
        return

    if amount in ["all", "max"]:
        max_sellable = player_inventory[item_name]
        max_demand = this_player.current_location.stock[item_name]
        amount = max_sellable if amount == "all" else min(max_sellable, max_demand)
    else:
        amount = int(amount)

    total_price = city_prices[item_name] * amount
    this_player.gold += total_price
    this_player.remove_from_inventory(item_name, amount)
    this_player.current_location.stock[item_name] += amount
    print(f"You sold {amount} {item_name} for {total_price} gold.")


def remove_item(this_player, item_name):
    if item_name in this_player.inventory and this_player.inventory[item_name] > 0:
        amount = input(f"How many {item_name} do you want to drop? ")
        if not amount.isdigit():
            print("Invalid quantity.")
            return
        amount = int(amount)

        if amount > this_player.inventory[item_name]:
            print(f"You don't have that many {item_name} to drop.")
        else:
            this_player.remove_from_inventory(item_name, amount)
            print(f"You dropped {amount} {item_name}.")
    else:
        print("You don't have that item in your inventory.")