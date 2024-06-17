#!/usr/bin/python3

import random
import time


print("*** Welcome to our bare-minimum MONOPOLY !! ***")

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
            self.prompt_sell_property(property)

    def sell_property(self, property):
        if property in self.properties:
            selling_price = int(property.price * 1.3)  # Sell at 30% profit
            self.add_balance(selling_price)
            self.properties.remove(property)
            print(f"{self.name} has sold {property.name} for {selling_price} Kenyan Shillings (30% profit).")
        else:
            print(f"{self.name} does not own {property.name}.")

    def prompt_sell_property(self, property):
        sell_choice = input(f"{self.name}, you need more money to buy {property.name}. Do you want to sell a property to raise funds? (y/n): ")
        if sell_choice.lower() == 'y':
            self.display_properties()
            property_to_sell = input("Which property do you want to sell? Enter property name: ")
            property_to_sell = next((prop for prop in self.properties if prop.name.lower() == property_to_sell.lower()), None)
            if property_to_sell:
                self.sell_property(property_to_sell)
            else:
                print(f"{self.name} does not own {property_to_sell}.")
        else:
            print(f"{self.name} cannot buy {property.name}.")

    def display_properties(self):
        if self.properties:
            print(f"{self.name}'s Properties:")
            for prop in self.properties:
                print(f"- {prop.name}")
        else:
            print(f"{self.name} does not own any properties.")

def main():
    # Initialize players
    player_name = input("Enter your name: ")
    player = Player(player_name)
    computer = Player("Computer")

    # Initialize properties
    properties = [
        Property("Park Lane", 400),
        Property("Mayfair", 600),
        Property("Kings Cross Station", 300),
        Property("Bond Street", 350)
        # Add more properties as needed
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

            # Ask player if they want to see their balance
            see_balance_choice = input("Do you want to see your account balance before deciding? (y/n): ")
            if see_balance_choice.lower() == 'y':
                print(f"Your current balance is {player.balance} Kenyan Shillings.")

            # Check if player can afford the property
            if player.balance >= property_to_buy.price:
                buy_choice = input(f"Do you wish to buy {property_to_buy.name}? (y/n): ")
                if buy_choice.lower() == 'y':
                    player.buy_property(property_to_buy)
            else:
                player.prompt_sell_property(property_to_buy)

            # Check winning condition
            if player.balance >= 10000:
                print(f"\nCongratulations! {player.name} has won by reaching 10,000 Kenyan Shillings!")
                game_continue = False
            elif computer.balance >= 10000:
                print(f"\nGame over! Computer has won by reaching 10,000 Kenyan Shillings!")
                game_continue = False

            # Computer's turn (basic simulation, can be enhanced)
            if game_continue:
                print("\nComputer's turn:")
                computer_property_to_buy = random.choice(properties)
                computer.buy_property(computer_property_to_buy)

                # Check winning condition after computer's turn
                if computer.balance >= 10000:
                    print(f"\nGame over! Computer has won by reaching 10,000 Kenyan Shillings!")
                    game_continue = False

            # Display player's properties
            player.display_properties()

        elif choice == '2':
            
            print("Exiting the game...")
            time.sleep(2)
            game_continue = False

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
