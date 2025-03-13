import time
import random
from game import utils

class World: # Handles the world state
    def __init__(self):
        self.name = 'world'
        self.cities = []
        self.base_prices = {'grain': 5, 'silk': 17, 'leather': 15, 'hides': 9, 'meat': 7}

    def generate_world(self):
        print("Generating world...")
        time.sleep(.1)
        utils.clear_screen()
        print("Creating default cities...")
        time.sleep(.1)
        self.generate_city("Homestead", ["farmland", "tavern"])
        self.generate_city("Eldoria", ["loom"])
        self.generate_city("Athelheim", ["hunter", "tanner"])
        utils.clear_screen()

    def generate_city(self, name, prefixes):
        city = City(name, prefixes)
        self.cities.append(city)

    def update_world(self):
        for city in self.cities:
            city.update_economy()

    def travel(self, current_location):
        utils.clear_screen()
        print("Travel to which city?")
        print("0. Stay in {}".format(current_location.name))
        for i, city in enumerate(self.cities):
            if city == current_location:
                continue
            print("{}. {}".format(i+1, city.name))
        choice = int(input("Enter choice: "))
        if choice == 0:
            return current_location
        else:
            print("Traveling to {}...".format(self.name))
            time.sleep(1)
            return self.cities[choice-1]

class City: # Handles city data
    def __init__(self, name, prefixes):
        self.name = name
        self.prices = World().base_prices
        self.population = random.randint(100, 10000)
        self.development = random.randint(1, 10)
        self.prefixes = prefixes
        self.stock = self.initialize_stock()

    def initialize_stock(self):
        return {item: max(50, int(self.population / 10) + random.randint(-20, 20)) for item in World().base_prices}

    def calculate_prices(self):
        prices = {}
        for item, price in self.prices.items():
            stock_factor = max(0.5, min(2.0, 100 / (self.stock[item] + 1)))
            development_factor = 1 - ((self.development - 5) * 0.05)
            prices[item] = round(price * stock_factor * development_factor)
        return prices

    def update_economy(self):
        self.prefix_tick()
        self.prices = self.calculate_prices()

    def prefix_tick(self):
        if "farmland" in self.prefixes:
            self.stock["grain"] += round(random.randint(10, 20)*self.development/5)
        if "tavern" in self.prefixes:
            self.stock["meat"] -= 2
            self.development += random.randint(1,5)/100
        if "loom" in self.prefixes:
            self.stock["silk"] += round(random.randint(4, 8)*self.development/5)
        if "hunter" in self.prefixes:
            self.stock["meat"] += round(random.randint(5, 10)*self.development/5)
            self.stock["hides"] += round(random.randint(3, 6)*self.development/5)
        if "tanner" in self.prefixes:
            self.stock["hides"] -= 2
            self.stock["leather"] += round(random.randint(3, 5)*self.development/5)

        self.development = round(min(10, self.development), 2) # Cap development at 10 and round to 2 decimal places

    def display_city(self):
        print("City: {}".format(self.name))
        print("Population: {}".format(self.population))
        print("Development: {}".format(self.development))
        print("Prices:")
        for item, price in self.prices.items():
            print("{}: {}".format(item, price), end=" ")
        print("\n")
        print("Stock:")
        for item, quantity in self.stock.items():
            print("{}: {}".format(item, quantity), end=" ")
        print("\n")


