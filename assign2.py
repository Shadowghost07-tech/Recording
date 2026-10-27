import math

# Empty board
board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print()

def winner(b):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b1, c in lines:
        if b[a] == b[b1] == b[c] != " ":
            return b[a]

    return None

def minimax(b, depth, alpha, beta, maximizing):
    result = winner(b)

    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if " " not in b:
        return 0

    if maximizing:
        best = -math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1,
                                alpha, beta, False)
                b[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1,
                                alpha, beta, True)
                b[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

def ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0,
                            -math.inf, math.inf, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        print("Ai chooses position:", move + 1)

print("TICTACTOE")
print("You are X. Ai is O.")
print("Enter positions from 1 to 9.")

display()

while True:
    try:
        move = int(input("Enter your position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid, Try again.")
            continue

    except ValueError:
        print("Enter a valid number.")
        continue

    board[move] = "X"
    display()

    if winner(board) == "X":
        print("You won!")
        break

    if " " not in board:
        print(" draw!")
        break

    ai_move()
    display()

    if winner(board) == "O":
        print("Ai won:(!")
        break

    if " " not in board:
        print("draw!")
        break