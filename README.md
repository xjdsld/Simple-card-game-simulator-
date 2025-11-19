Simple Card Game Simulator (Python)

This project is a console-based card game simulator written in Python.
It generates a deck, deals cards to a user and several bot players, determines a random trump suit, and then simulates turns where each player places a card on the table. The script also analyzes players’ trump cards, showing:

Total number of trump cards each player holds

Minimum and maximum trump card values for every player

The game loop continues until the deck is empty and players can no longer draw cards.

✨ Features
🔹 Deck Generation

Creates a full 36-card deck using:

Suits: ♥ ♦ ♣ ♠

Card meanings: 6, 7, 8, 9, 10, B, Д, К, Т

🔹 Card Distribution

Deals a standard number of cards (default: 6) to:

User

Bot1

Bot2

Bot3

🔹 Trump System

Randomly selects one suit as trump

Counts trump cards for every player

Finds minimum and maximum trump card values

🔹 Gameplay Loop

Each round:

Shows all players’ hands

Displays trump statistics

User selects a card to play

Bots play random cards

Players automatically draw back up to 6 cards (if deck allows)

📂 Main Functions
create_deck(deck, meaning, suit)

Builds the deck from suits and card meanings.

fill_cards_players(player, deck, count_cards)

Deals random cards from the deck to a player.

user_hod(player, table)

Handles user input for playing a card.

bot_hod(player, table)

Bot logic for placing a random card on the table.

trump_count(player, name, count)

Counts how many trump cards the player has.

min_max_trump(player, name, meaning, values)

Finds player’s min/max trump card based on assigned card values.

🧠 Purpose

This project serves as a foundation for a Durak-like card game, allowing you to extend it with:

Attack/defense mechanics

Bot intelligence

Round victory logic

Graphical interface

Online multiplayer logic

▶️ How to Run
python game.py


Ensure you have Python installed (3.8+ recommended).

📝 Notes

The code currently uses a continuous loop (while True:).
For a fully playable game, exit conditions should be added.

There are places where improvements can be made (e.g., card parsing, value mapping, avoiding repeated searches).

Suits include Unicode symbols, so make sure your console supports UTF-8.

If you'd like, I can also help you:
✅ rewrite the code in OOP style
✅ optimize the logic
✅ fix bugs (e.g., count being undefined)
✅ add real game mechanics
Just say "refactor please" or "add real gameplay"!
