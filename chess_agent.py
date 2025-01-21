#ID: 620126951
import chess


def evaluate_board(board):
    # calculating the weighted sum of all of a players pieces on the board
    if board.turn == chess.WHITE:
        return sum(piece_value(piece) for piece in board.piece_map().values())
    else:
        return -sum(piece_value(piece) for piece in board.piece_map().values())

def piece_value(piece):
    #assign value to each chess piece
    values = {
        chess.PAWN: 10,
        chess.KNIGHT: 30,
        chess.BISHOP: 30,
        chess.ROOK: 50,
        chess.QUEEN: 90,
        chess.KING: 900 
    }
    return values[piece.piece_type]

def minimax(board, depth, alpha, beta, maximizing_player):
    #check if depth is 0 or game is over
    if depth == 0 or board.is_game_over():
        return None, evaluate_board(board)
    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        #check for legal moves on the board
        for move in board.legal_moves:
            board.push(move)
            current_eval = minimax(board, depth-1, alpha, beta, False)[1] #grabs the eval portion of the minimax algorithm and swaps player
            board.pop()
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
            #update alpha to largest value found
            alpha = max(alpha, max_eval)
            #prune if alpha is greater than or equal to beta
            if alpha >= beta:
                break
        return best_move, max_eval
    else:
        min_eval = float('inf')
        best_move = None
        #check for legal moves on the board
        for move in board.legal_moves:
            board.push(move)
            current_eval = minimax(board, depth-1, alpha, beta, True)[1] #grabs the eval portion of the minimax algorithm and swaps player
            board.pop()
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
            #update beta to smallest value found
            beta = min(beta, min_eval)
            #prune if alpha is greater than or equal to beta
            if alpha >= beta:
                break
        return best_move, min_eval

def get_best_move(board, depth):
    move, _ = minimax(board, depth, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
    return move #returns the best_move portion of the minimax algorithm to be made on the board

def play_game():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move: ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move. Try again.")
        else:
            move = get_best_move(board, depth=3)
            board.push(move)
    print("Game over:", board.result())

if __name__ == "__main__":
    play_game()
