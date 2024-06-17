#!/usr/bin/python3

import random
import time


class Property:

    def _init_(self, name, price):
        self.name = name
        self.price = price
        self.owner = None


class Player:

    def _init_(self, name, initial_balance=1500):
        self.name = name
        self.balance = initial_balance
        self.total_money_earned = initial_balance
        self.total_money_spent = 0
        self.properties = []
        self.turns_taken = 0
        self.bankrupt = False

    def deduct_balance(self, amount):
        self.balance -= amount
        self.total_money_spent += amount

    def add_balance(self, amount):
        self.balance += amount
        self.total_money_earned += amount

    def buy_property(self, property):
        if self.balance >= property.price:
            self.deduct_balance(property.price)
            property.owner = self
            self.properties.append(property)
            print(
                f"{self.name} has bought {property.name} for {property.price} Kenyan Shillings."
            )
        else:
            print(f"{self.name} cannot afford {property.name}.")
            self.prompt_sell_property(property)

    def sell_property(self, property):
        if property in self.properties:
            selling_price = int(property.price * 1.3)  # Sell at 30% profit
            self.add_balance(selling_price)
            property.owner = None
            self.properties.remove(property)
            print(
                f"{self.name} has sold {property.name} for {selling_price} Kenyan Shillings (30% profit)."
            )
        else:
            print(f"{self.name} does not own {property.name}.")

    def prompt_sell_property(self, property):
        if self.properties:
            sell_choice = input(
                f"{self.name}, you need more money to buy {property.name}. Do you want to sell a property to raise funds? (y/n): "
            )
            if sell_choice.lower() == 'y':
                self.display_properties()
                property_to_sell = input(
                    "Which property do you want to sell? Enter property name: "
                )
                property_to_sell = next(
                    (prop for prop in self.properties
                     if prop.name.lower() == property_to_sell.lower()), None)
                if property_to_sell:
                    self.sell_property(property_to_sell)
                else:
                    print(f"{self.name} does not own {property_to_sell}.")
            else:
                print(f"{self.name} cannot buy {property.name}.")
        else:
            print(
                f"{self.name} cannot buy {property.name} and has no properties to sell."
            )

    def display_properties(self):
        if self.properties:
            print(f"{self.name}'s Properties:")
            for prop in self.properties:
                print(f"- {prop.name}")
        else:
            print(f"{self.name} does not own any properties.")

    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(
            f"Total Money Earned: {self.total_money_earned} Kenyan Shillings")
        print(f"Total Money Spent: {self.total_money_spent} Kenyan Shillings")
        print(f"Current Balance: {self.balance} Kenyan Shillings")
        print(f"Number of Properties Owned: {len(self.properties)}")
        print(f"Number of Turns Taken: {self.turns_taken}")

    def declare_bankruptcy(self):
        print(f"{self.name} is bankrupt!")
        self.bankrupt = True
        for prop in self.properties:
            prop.owner = None
        self.properties.clear()


def pay_rent(player, property):
    rent = int(property.price * 0.1)  # Rent is 10% of property price
    print(
        f"{player.name} needs to pay {rent} Kenyan Shillings as rent for landing on {property.name} owned by {property.owner.name}."
    )
    if player.balance >= rent:
        player.deduct_balance(rent)
        property.owner.add_balance(rent)
        print(
            f"{player.name} paid {rent} Kenyan Shillings to {property.owner.name}."
        )
    else:
        print(f"{player.name} cannot afford to pay the rent.")
        while player.balance < rent and player.properties:
            player.prompt_sell_property(property)
        if player.balance >= rent:
            player.deduct_balance(rent)
            property.owner.add_balance(rent)
            print(
                f"{player.name} paid {rent} Kenyan Shillings to {property.owner.name}."
            )
        else:
            player.declare_bankruptcy()


def draw_chance_card(player):
    cards = [{
        "message": "You won a beauty contest! Collect 200 Kenyan Shillings.",
        "effect": lambda player: player.add_balance(200)
    }, {
        "message": "Pay hospital fees of 100 Kenyan Shillings.",
        "effect": lambda player: player.deduct_balance(100)
    }, {
        "message": "Bank error in your favor. Collect 500 Kenyan Shillings.",
        "effect": lambda player: player.add_balance(500)
    }, {
        "message": "You have been fined 150 Kenyan Shillings for speeding.",
        "effect": lambda player: player.deduct_balance(150)
    }, {
        "message": "Receive 50 Kenyan Shillings for your birthday.",
        "effect": lambda player: player.add_balance(50)
    }, {
        "message": "Advance to Go. Collect 200 Kenyan Shillings.",
        "effect": lambda player: player.add_balance(200)
    }]
    card = random.choice(cards)
    print(f"Chance Card: {card['message']}")
    card["effect"](player)
    if player.balance < 0:
        while player.balance < 0 and player.properties:
            player.prompt_sell_property(None)
        if player.balance < 0:
            player.declare_bankruptcy()


def draw_community_chest_card(player):
    cards = [{
        "message": "Pay school fees of 300 Kenyan Shillings.",
        "effect": lambda player: player.deduct_balance(300)
    }, {
        "message": "Receive 100 Kenyan Shillings from sale of stock.",
        "effect": lambda player: player.add_balance(100)
    }, {
        "message": "Doctor's fee. Pay 50 Kenyan Shillings.",
        "effect": lambda player: player.deduct_balance(50)
    }, {
        "message": "Go to Jail. Pay 100 Kenyan Shillings.",
        "effect": lambda player: player.deduct_balance(100)
    }, {
        "message": "Income tax refund. Collect 200 Kenyan Shillings.",
        "effect": lambda player: player.add_balance(200)
    }, {
        "message": "You inherit 400 Kenyan Shillings.",
        "effect": lambda player: player.add_balance(400)
    }]
    card = random.choice(cards)
    print(f"Community Chest Card: {card['message']}")
    card["effect"](player)
    if player.balance < 0:
        while player.balance < 0 and player.properties:
            player.prompt_sell_property(None)
        if player.balance < 0:
            player.declare_bankruptcy()


def take_turn(player, properties):
    player.turns_taken += 1
    print(f"\n{player.name}'s turn:")
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}.")

    # Simulate landing on a property
    property_to_buy = random.choice(properties)
    print(f"You landed on {property_to_buy.name}.")

    # Draw a Chance or Community Chest card
    card_type = random.choice(['chance', 'community_chest'])
    if card_type == 'chance':
        draw_chance_card(player)
    else:
        draw_community_chest_card(player)

    # Check if the property is owned by someone
    if property_to_buy.owner and property_to_buy.owner != player:
        pay_rent(player, property_to_buy)
    else:
        # Ask player if they want to see their balance
        see_balance_choice = input(
            "Do you want to see your account balance before deciding? (y/n): ")
        if see_balance_choice.lower() == 'y':
            print(
                f"Your current balance is {player.balance} Kenyan Shillings.")

        # Check if player can afford the property
        if player.balance >= property_to_buy.price:
            buy_choice = input(
                f"Do you wish to buy {property_to_buy.name}? (y/n): ")
            if buy_choice.lower() == 'y':
                player.buy_property(property_to_buy)
        else:
            player.prompt_sell_property(property_to_buy)

    # Display player's properties and stats
    player.display_properties()
    player.display_stats()


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
        Property("Bond Street", 350),
        Property("Oxford Street", 500),
        Property("Piccadilly", 550),
        Property("Coventry Street", 450),
        Property("Leicester Square", 650),
        Property("Fenchurch Street Station", 300),
        Property("Whitechapel Road", 150),
        Property("Old Kent Road", 100),
        Property("The Angel Islington", 200)
    ]

    game_continue = True

    while game_continue:
        print("\n1. Continue game")
        print("2. Exit game")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            if not player.bankrupt and not computer.bankrupt:
                # Player's turn
                take_turn(player, properties)
                # Check winning condition
                if player.balance >= 10000:
                    print(
                        f"\nCongratulations! {player.name} has won by reaching 10,000 Kenyan Shillings!"
                    )
                    game_continue = False
                elif player.bankrupt:
                    print(f"\nGame over! {player.name} is bankrupt!")
                    game_continue = False

                if game_continue:
                    # Computer's turn
                    take_turn(computer, properties)
                    # Check winning condition
                    if computer.balance >= 10000:
                        print(
                            f"\nGame over! Computer has won by reaching 10,000 Kenyan Shillings!"
                        )
                        game_continue = False
                    elif computer.bankrupt:
                        print(f"\nGame over! Computer is bankrupt!")
                        game_continue = False
            else:
                print("Game over! One of the players is bankrupt.")
                game_continue = False

        elif choice == '2':
            print("Exiting the game...")
            time.sleep(2)
            game_continue = False

        else:
            print("Invalid choice. Please enter 1 or 2.")


if _name_ == "_main_":
    main()