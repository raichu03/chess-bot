import os
import chess
import chess.svg
import chessEngine
import chess.engine
import chess.pgn

board = chess.Board()
ch = chessEngine.Engine()

#loafing stockfish to make it play with the bot
stockfish = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-ubuntu-x86-64-modern")

game = chess.pgn.Game()
game.headers["Event"] = "Stockfish example"
game.headers["White"] = "ourBot"
game.headers["Black"] = "stockfish"
node = game

def get_move():
    """Returns the best move for the white player"""
    legal_moves = list(board.legal_moves)
    best_move = None
    best_score = float('-inf')

    for move in legal_moves:
        board.push(move)
        score = ch.minMaxAlgo(board, 3, True) # 3 is the depth of the tree to be searched
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move, best_score

if __name__ == "__main__":
    ### Game loop ###
    os.system('clear||cls')

    while True:
        print(board)
        print("\n__________________________\n")

        print("Computer is thinking...")
        white_move, score = get_move()
        board.push(white_move)
        node = node.add_variation(chess.Move.from_uci(str(white_move)))
        print("Score: ", score) 
        print("__________________________\n")    

        print(board)
        print("\n__________________________\n")

        print("Stockfish is thinking...")
        fish_move = stockfish.play(board, chess.engine.Limit(time=0.01))
        board.push(fish_move.move)
        node = node.add_variation(chess.Move.from_uci(str(fish_move.move)))

        print("\n__________________________\n")

        if board.is_game_over():
            print("Game over")
            print(board.result())
            break
    
    # saves the game in a pgn file for future refrences
    with open("testGame2.pgn", "w") as f:
        exporter = chess.pgn.FileExporter(f)
        game.accept(exporter)
    stockfish.quit()
