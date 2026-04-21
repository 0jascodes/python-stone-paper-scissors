import random

# Emojis dictionary mapping strings to emojis
EMOJIS = {
    'stone': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

def get_computer_choice():
    """Returns a random choice for the computer."""
    return random.choice(['stone', 'paper', 'scissors'])

def get_player_choice(choice_input):
    """Maps user numerical input to a string choice."""
    options = {'1': 'stone', '2': 'paper', '3': 'scissors'}
    return options.get(choice_input)

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the round."""
    if player_choice == computer_choice:
        return 'draw'
    
    # Player win conditions
    if (player_choice == 'stone' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'stone') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def display_scoreboard(player_score, computer_score):
    """Displays the current score."""
    print("\n════════════════════════════════════════════")
    print(f"🏆 SCOREBOARD - Player: {player_score} | Computer: {computer_score}")
    print("════════════════════════════════════════════")

def display_result(player_choice, computer_choice, winner):
    """Displays the result of the round including choices and the round winner."""
    print("\n────────────────────────────────────────────")
    print(f"You chose:      {player_choice.capitalize()} {EMOJIS[player_choice]}")
    print(f"Computer chose: {computer_choice.capitalize()} {EMOJIS[computer_choice]}")
    print("────────────────────────────────────────────")
    
    if winner == 'player':
        print("🎉 YOU WIN this round!")
    elif winner == 'computer':
        print("😔 COMPUTER WINS this round!")
    else:
        print("🤝 It's a DRAW!")
    print("────────────────────────────────────────────\n")

def display_final_summary(player_score, computer_score):
    """Displays the final overall game results."""
    print("\n════════════════════════════════════════════")
    print("             FINAL GAME SUMMARY")
    print("════════════════════════════════════════════")
    print(f"Your Total Score:     {player_score}")
    print(f"Computer Total Score: {computer_score}")
    print("────────────────────────────────────────────")
    
    if player_score > computer_score:
        print("🎉🏆 CONGRATULATIONS! YOU ARE THE OVERALL WINNER! 🏆🎉")
    elif computer_score > player_score:
        print("😔 COMPUTER IS THE OVERALL WINNER! BETTER LUCK NEXT TIME! 😔")
    else:
        print("🤝 IT'S A TIE GAME! 🤝")
    print("════════════════════════════════════════════\n")
