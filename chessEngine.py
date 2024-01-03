import chess
import chess.engine


class Engine:

    def __init__(self):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-ubuntu-x86-64-modern")
        self.piece_values = {
            'p': -1, 'n': -3, 'b': -3.1, 'r': -5, 'q': -9, 'k': 0,
            'P': 1, 'N': 3, 'B': 3.1, 'R': 5, 'Q': 9, 'K': 0
        }

    def customEvaluate(self, board):
        """Evaluates current position and returns a score"""
        evaluation_score = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                evaluation_score += self.piece_values[piece.symbol()]

                total_moves = len(list(board.legal_moves))
                evaluation_score += 0.01 * total_moves

                if piece.symbol() == 'p' or piece.symbol() == 'P':
                    evaluation_score += 0.1 * (7 - chess.square_rank(square))
                    evaluation_score += self.evaluate_pawn_structure(board, square)

                return evaluation_score
    
    def evaluate_pawn_structure(self, board, square):
        """Evaluates pawn structure and returns a score"""
        pawn_score = 0

        if self.double_pawn(board, square):
            pawn_score -= 0.5
            
        if self.passed_pawn(board, square):
            pawn_score += 0.5
        
        return pawn_score   
    
    def double_pawn(self, board, square):
        """If there are double pawn in same file, returns True"""

        file = chess.square_file(square)
        rank = chess.square_rank(square)
        color = chess.square_color(square)

        for i in range(chess.A1, chess.H8 + 1):
            if i != file and board.piece_at(chess.square(i,rank)) == chess.Piece(chess.PAWN, color):
                return True
            
        return False
    
    def passed_pawn(self, board, square):
        """If there are no pawns in the same file and in front of the pawn, returns True"""

        file = chess.square_file(square)
        rank = chess.square_rank(square)
        color = chess.square_color(square)

        if all(board.piece_at(chess.square(i, rank)) != chess.Piece(chess.PAWN, color) for i in range(chess.FILE_A, chess.FILE_H + 1)):
            return True
        False


    def stockfishEvaluate(self, board):
        """Evaluates current position and returns a score using stockfish engine"""
        result = self.engine.analyse(board, chess.engine.Limit(depth=15))
        score = result["score"].white().score()
        if score is None:
            score = 0
        return score


    def minMaxAlgo(self, board, depth, max_player):
        """Traverses the tree and returns the best score"""
        l_moves = list(board.legal_moves)

        if(depth == 0 or board.legal_moves.count() == 0):
            # return self.stockfishEvaluate(board)
            return self.customEvaluate(board)
        
        else:

            if max_player:
                best_score = float('-inf')

                for move in l_moves:
                    board.push(move)
                    score = self.minMaxAlgo(board, depth-1, False)
                    best_score = max(score, best_score)
                    board.pop()
                return best_score
            
            else: 
                best_score = float('inf')

                for move in l_moves:
                    board.push(move)
                    score = self.minMaxAlgo(board, depth-1, True)
                    best_score = min(score, best_score)
                    board.pop()
                return best_score


