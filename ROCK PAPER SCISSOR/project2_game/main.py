from game import sps

def main():
    player_score = 0
    computer_score = 0
    
    print("════════════════════════════════════════════")
    print("      Welcome to Stone Paper Scissors!      ")
    print("════════════════════════════════════════════")
    
    while True:
        # Show scoreboard before every round
        sps.display_scoreboard(player_score, computer_score)
        
        # Display menu options
        print("Choose your weapon:")
        print("1. 🪨 Stone")
        print("2. 📄 Paper")
        print("3. ✂️ Scissors")
        print("4. 🚪 Quit Game")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        # Handle quit
        if choice == '4':
            break
            
        # Get and validate player choice
        player_choice = sps.get_player_choice(choice)
        
        if not player_choice:
            print("\n❌ Invalid choice! Please enter a number between 1 and 4.\n")
            continue
            
        # Get computer choice
        computer_choice = sps.get_computer_choice()
        
        # Determine winner
        winner = sps.determine_winner(player_choice, computer_choice)
        
        # Display choices and round result
        sps.display_result(player_choice, computer_choice, winner)
        
        # Update score
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
            
    # Show overall final winner and scores when quitting
    sps.display_final_summary(player_score, computer_score)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
