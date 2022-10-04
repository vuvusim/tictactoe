board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()
        


def quit(user_input):
    if use_input == "q": return False
    else: return False

while True:
    use_input = input("Please enter position 1-9 or enter \"q\" to quit: ")
    if quit(user_input):
        print_board(board)