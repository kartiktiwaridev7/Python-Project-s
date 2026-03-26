# Board and occupied positions
positions = [" " for _ in range(9)]
occupied = []

# Display the game board
def gameBoard():
    print(f"""
    {positions[0]} | {positions[1]} | {positions[2]}
    ----------
    {positions[3]} | {positions[4]} | {positions[5]}
    ----------
    {positions[6]} | {positions[7]} | {positions[8]}
    """)

# Check for a winner
def checkWinner():
    winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
    for combo in winning_combinations:
        if positions[combo[0]] == positions[combo[1]] == positions[combo[2]] != " ":
            return positions[combo[0]]

# Player's move
def player_move(player, symbol):
    try:
        pos = int(input(f"{player} ({symbol}), enter position (1-9): "))
        if pos not in range(1, 10) or pos in occupied:
            print("Invalid move, try again.")
            player_move(player, symbol)
        else:
            positions[pos-1] = symbol
            occupied.append(pos)
    except ValueError:
        print("Invalid input, please enter a number between 1 and 9.")
        player_move(player, symbol)

# Main game function
def main():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    symbol1 = input(f"{player1}, choose your symbol (X or O): ").upper()
    while symbol1 not in ['X', 'O']:
        print("Invalid choice! Choose X or O.")
        symbol1 = input(f"{player1}, choose your symbol (X or O): ").upper()

    symbol2 = 'O' if symbol1 == 'X' else 'X'

    gameBoard()
    winner = None

    for turn in range(9):
        if turn % 2 == 0:
            player_move(player1, symbol1)
        else:
            player_move(player2, symbol2)
        
        gameBoard()
        winner = checkWinner()
        if winner:
            print(f"Congratulations! {player1 if winner == symbol1 else player2} ({winner}) wins!")
            break

    if not winner:
        print("It's a draw!")

if __name__ == "__main__":
    main()
