import cards
import random

from textual import on
from textual.app import App
from textual.containers import ScrollableContainer, Horizontal, Center
from textual.widgets import Header, Footer, Static, Button

class PlayerHand(Static):

    @on(Button.Pressed)
    def selectCard(self):
        return id

    def compose(self):
        yield ScrollableContainer(
            Button(variant="primary"),
            id="hand"
        )

    def addCard(self):
        new_card = Button(variant="primary")
        self.mount(new_card)

class GoFishApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
        ("a", "addCard", "Add Card"),
        ("p", "play_game", "Play Game")
    ]

    CSS_PATH = "game.css"

    
    deck = cards.build_deck()

    computer = []
    player = []
    player_pairs = []
    computer_pairs = []

    def compose(self):
        self.setup()

        yield Header(show_clock=True)
        yield Button()
        yield PlayerHand()
        yield Button()
        yield Footer()

    def show_player_hand(self, t_player):
        print("\nPlayers hand:")
        for n, card in enumerate(t_player):
            PlayerHand.addCard()

    def setup(self):
        deck = cards.build_deck()

        PlayerHand.addCard(PlayerHand)

        computer = []
        player = []
        player_pairs = []
        computer_pairs = []

        for _ in range(7):
            computer.append(deck.pop())
            player.append(deck.pop())

        player, pairs = cards.identify_remove_pairs(player)
        player_pairs.extend(pairs)
        computer, pairs = cards.identify_remove_pairs(computer)
        computer_pairs.extend(pairs)
    
    def gameLoop(self):
        deck = cards.build_deck()

        computer = []
        player = []
        player_pairs = []
        computer_pairs = []

        for _ in range(7):
            computer.append(deck.pop())
            player.append(deck.pop())

        player, pairs = cards.identify_remove_pairs(player)
        player_pairs.extend(pairs)
        computer, pairs = cards.identify_remove_pairs(computer)
        computer_pairs.extend(pairs)
        PlayerHand.addCard(self)


        while True:
            player.sort()

            self.show_player_hand(player)
            choice = input(
                "\nPlease select the number for the card you want from the above list"
            )
            choice = int(choice)
            selection = player[int(choice)]
            value = selection[: selection.find(" ")]

            found_it = False
            for n, card in enumerate(computer):
                if card.startswith(value):
                    found_it = n
                    break

            if isinstance(found_it, bool):
                print("\nGo Fish!\n")
                player.append(deck.pop())
                print(f"You drew a {player[-1]}.")
                if len(deck) == 0:
                    break
            else:
                print(f"Here is your card from the computer: {computer[n]}.")
                player.append(computer.pop(n))

            player, pairs = cards.identify_remove_pairs(player)
            player_pairs.extend(pairs)
            self.show_player_hand(player)

            if len(player) == 0:
                print("The Game is over. The player won.")
                break
            if len(computer) == 0:
                print("The Game is over. The computer won.")
                break

            card = random.choice(computer)
            value = card[: card.find(" ")]

            choice = input(f"\nFrom the computer: Do you have a {value}? (y/n) ")

            if choice in ["y", "Y", "yes", "YES", "Yes"]:
                for n, card in enumerate(player):
                    if card.startswith(value):
                        break
                computer.append(player.pop(n))
            else:
                computer.append(deck.pop())
                if len(deck) == 0:
                    break

            computer, pairs = cards.identify_remove_pairs(computer)
            computer_pairs.extend(pairs)

            if len(computer) == 0:
                print("The Game is over. The computer won.")
                break
            if len(player) == 0:
                print("The Game is over. The player won.")
                break

            if len(deck) == 0:
                print("Game over.")
                if len(player_pairs) == len(computer_pairs):
                    print("It's a draw.")
                elif len(player_pairs) > len(computer_pairs):
                    print("The Game is over. The player won.")
                else:
                    print("The Game is over. The computer won.")

    def action_play_game(self):
        ...

    def action_toggle_dark_mode(self):
        self.dark = not self.dark

    def action_addCard(self):
        PlayerHand.addCard(self)

    def action_removeCard(self):
        PlayerHand.removeCard(self)


if __name__ == "__main__":
    GoFishApp().run()
    GoFishApp().setup()
    GoFishApp().gameLoop()

"""deck = cards.build_deck()

computer = []
player = []
player_pairs = []
computer_pairs = []

for _ in range(7):
    computer.append(deck.pop())
    player.append(deck.pop())

player, pairs = cards.identify_remove_pairs(player)
player_pairs.extend(pairs)
computer, pairs = cards.identify_remove_pairs(computer)
computer_pairs.extend(pairs)"""


def show_player_hand():
    print("\nPlayers hand:")
    for n, card in enumerate(player):
        print(f"\tSelect {n} for {card}")



"""while True:
    player.sort()

    show_player_hand()
    PlayerHand.addCard(PlayerHand)
    choice = input(
        "\nPlease select the number for the card you want from the above list"
    )
    choice = int(choice)
    selection = player[int(choice)]
    value = selection[: selection.find(" ")]

    found_it = False
    for n, card in enumerate(computer):
        if card.startswith(value):
            found_it = n
            break

    if isinstance(found_it, bool):
        print("\nGo Fish!\n")
        player.append(deck.pop())
        print(f"You drew a {player[-1]}.")
        if len(deck) == 0:
            break
    else:
        print(f"Here is your card from the computer: {computer[n]}.")
        player.append(computer.pop(n))

    player, pairs = cards.identify_remove_pairs(player)
    player_pairs.extend(pairs)
    show_player_hand()

    if len(player) == 0:
        print("The Game is over. The player won.")
        break
    if len(computer) == 0:
        print("The Game is over. The computer won.")
        break

    card = random.choice(computer)
    value = card[: card.find(" ")]

    choice = input(f"\nFrom the computer: Do you have a {value}? (y/n) ")

    if choice in ["y", "Y", "yes", "YES", "Yes"]:
        for n, card in enumerate(player):
            if card.startswith(value):
                break
        computer.append(player.pop(n))
    else:
        computer.append(deck.pop())
        if len(deck) == 0:
            break

    computer, pairs = cards.identify_remove_pairs(computer)
    computer_pairs.extend(pairs)

    if len(computer) == 0:
        print("The Game is over. The computer won.")
        break
    if len(player) == 0:
        print("The Game is over. The player won.")
        break

if len(deck) == 0:
    print("Game over.")
    if len(player_pairs) == len(computer_pairs):
        print("It's a draw.")
    elif len(player_pairs) > len(computer_pairs):
        print("The Game is over. The player won.")
    else:
        print("The Game is over. The computer won.")"""
