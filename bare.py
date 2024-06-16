#!/usr/bin/python3

import time

time.sleep(2)
import random

print(" ")
print(" ")

print("Welcome to our bare-minimum MONOPOLY !! ")

print(" ")


class Property:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Player:
    def __init__(self, name, initial_balance=1500):
        self.name = name
        self.balance = initial_balance
        self.properties = []

    def deduct_balance(self, amount):
        self.balance -= amount

    def add_balance(self, amount):
        self.balance += amount

    def buy_property(self, property):
        if self.balance >= property.price:
            self.deduct_balance(property.price)
            self.properties.append(property)
            print(f"{self.name} has bought {property.name} for {property.price} Kenyan Shillings.")
        else:
            print(f"{self.name} cannot afford {property.name}.")

    def sell_property(self, property):
        if property in self.properties:
            self.add_balance(property.price)
            self.properties.remove(property)
            print(f"{self.name} has sold {property.name} for {property.price} Kenyan Shillings.")
        else:
            print(f"{self.name} does not own {property.name}.")

    def display_properties(self):
        if self.properties:
            print(f"{self.name}'s Properties:")
            for prop in self.properties:
                print(f"- {prop.name}")
        else:
            print(f"{self.name} does not own any properties.")
            
time.sleep(2)

def main():
    # Initializing players
    player_name = input("Enter your name: ")
    player = Player(player_name)
    computer = Player("Computer")

    # Initialize properties
    properties = [
        Property("Park Lane", 400),
        Property("Mayfair", 600),
        Property("Kings Cross Station", 300),
        Property("Bond Street", 350)
        #more properties
    ]

    game_continue = True

    while game_continue:
        print("\n1. Continue game")
        print("2. Exit game")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Player's turn
            print(f"\n{player.name}'s turn:")
            dice_roll = random.randint(1, 6)
            print(f"You rolled a {dice_roll}.")

            # Simulate landing on a property
            property_to_buy = random.choice(properties)
            print(f"You landed on {property_to_buy.name}.")
            
            time.sleep(2)

            # Ask player to buy property
            buy_choice = input(f"Do you wish to buy {property_to_buy.name}? (y/n): ")
            if buy_choice.lower() == 'y':
                player.buy_property(property_to_buy)

            # Computer's turn (basic simulation, can be enhanced)
            print("\nComputer's turn:")
            computer_property_to_buy = random.choice(properties)
            computer.buy_property(computer_property_to_buy)

            # Display player's properties
            player.display_properties()

            # Check winning condition (example: reaching a certain balance)
            if player.balance >= 5000:
                print(f"\nCongratulations! {player.name} has won!")
                game_continue = False

        elif choice == '2':
            print("Exiting the game...")
            game_continue = False

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

