from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abstractmethod
    def valid_moves(self, board):
        pass

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для данной фигуры на текущей доске.

        Параметры:
         - board: экземпляр класса Board, представляющий текущее состояние доски.

        Возвращаемое значение:
        Список кортежей (row, col), представляющих возможные позиции для хода фигуры.
        """
        # По умолчанию фигура не имеет возможных ходов, переопределяется в подклассах.
        return []


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False  # Флаг, указывающий, делала ли пешка первый ход

    def valid_moves(self, board):
        valid_moves = []
        row, col = self.position
        direction = 1 if self.color == 'white' else -1

        # Пешка может двигаться на одну клетку вперед
        if board.grid[row + direction][col] == '.':
            valid_moves.append((row + direction, col))

            # Пешка может двигаться на две клетки вперед, если она не двигалась ранее
            if not self.has_moved and board.grid[row + 2 * direction][col] == '.':
                valid_moves.append((row + 2 * direction, col))

        # Пешка может атаковать по диагонали
        for col_offset in (-1, 1):
            target_row = row + direction
            target_col = col + col_offset
            if 0 <= target_row < 8 and 0 <= target_col < 8:
                target_piece = board.grid[target_row][target_col]
                if isinstance(target_piece, Piece) and target_piece.color != self.color:
                    valid_moves.append((target_row, target_col))

        return valid_moves

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для данной пешки на текущей доске.

        Параметры:
         - board: экземпляр класса Board, представляющий текущее состояние доски.

        Возвращаемое значение:
        Список кортежей (row, col), представляющих возможные позиции для хода пешки.
        """
        possible_moves = []
        row, col = self.position
        direction = 1 if self.color == 'white' else -1

        # Пешка может двигаться на одну клетку вперед
        if 0 <= row + direction < 8 and board.grid[row + direction][col] == '.':
            possible_moves.append((row + direction, col))

            # Пешка может двигаться на две клетки вперед, если она не двигалась ранее
            if not self.has_moved and board.grid[row + 2 * direction][col] == '.':
                possible_moves.append((row + 2 * direction, col))

        # Пешка может атаковать по диагонали
        for col_offset in (-1, 1):
            target_row = row + direction
            target_col = col + col_offset
            if 0 <= target_row < 8 and 0 <= target_col < 8:
                target_piece = board.grid[target_row][target_col]
                if isinstance(target_piece, Piece) and target_piece.color != self.color:
                    possible_moves.append((target_row, target_col))

        return possible_moves

    def __str__(self):
        return 'p' if self.color == 'black' else 'P'


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        # Ладья может двигаться по вертикали и горизонтали
        valid_moves = []

        # Проверяем возможные ходы вверх по столбцу
        for i in range(self.position[0] - 1, -1, -1):
            if isinstance(board.grid[i][self.position[1]], Piece):
                if board.grid[i][self.position[1]].color != self.color:
                    valid_moves.append((i, self.position[1]))
                break
            valid_moves.append((i, self.position[1]))

        # Проверяем возможные ходы вниз по столбцу
        for i in range(self.position[0] + 1, 8):
            if isinstance(board.grid[i][self.position[1]], Piece):
                if board.grid[i][self.position[1]].color != self.color:
                    valid_moves.append((i, self.position[1]))
                break
            valid_moves.append((i, self.position[1]))

        # Проверяем возможные ходы влево по строке
        for j in range(self.position[1] - 1, -1, -1):
            if isinstance(board.grid[self.position[0]][j], Piece):
                if board.grid[self.position[0]][j].color != self.color:
                    valid_moves.append((self.position[0], j))
                break
            valid_moves.append((self.position[0], j))

        # Проверяем возможные ходы вправо по строке
        for j in range(self.position[1] + 1, 8):
            if isinstance(board.grid[self.position[0]][j], Piece):
                if board.grid[self.position[0]][j].color != self.color:
                    valid_moves.append((self.position[0], j))
                break
            valid_moves.append((self.position[0], j))

        return valid_moves

    def get_possible_moves(self, board):
        possible_moves = []

        # Движение по вертикали вверх
        for i in range(self.position[0] - 1, -1, -1):
            if board.grid[i][self.position[1]] == ' ':
                possible_moves.append((i, self.position[1]))
            else:
                if board.grid[i][self.position[1]].color != self.color:
                    possible_moves.append((i, self.position[1]))
                break

        # Движение по вертикали вниз
        for i in range(self.position[0] + 1, 8):
            if board.grid[i][self.position[1]] == ' ':
                possible_moves.append((i, self.position[1]))
            else:
                if board.grid[i][self.position[1]].color != self.color:
                    possible_moves.append((i, self.position[1]))
                break

        # Движение по горизонтали влево
        for j in range(self.position[1] - 1, -1, -1):
            if board.grid[self.position[0]][j] == ' ':
                possible_moves.append((self.position[0], j))
            else:
                if board.grid[self.position[0]][j].color != self.color:
                    possible_moves.append((self.position[0], j))
                break

        # Движение по горизонтали вправо
        for j in range(self.position[1] + 1, 8):
            if board.grid[self.position[0]][j] == ' ':
                possible_moves.append((self.position[0], j))
            else:
                if board.grid[self.position[0]][j].color != self.color:
                    possible_moves.append((self.position[0], j))
                break

        return possible_moves

    def __str__(self):
        return 'R' if self.color == 'white' else 'r'


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        # Конь может двигаться по "L" образно
        valid_moves = []
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        for move in moves:
            new_row = self.position[0] + move[0]
            new_col = self.position[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if not isinstance(board.grid[new_row][new_col], Piece) or \
                        board.grid[new_row][new_col].color != self.color:
                    valid_moves.append((new_row, new_col))

        return valid_moves

    def get_possible_moves(self, board):
        possible_moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for dx, dy in directions:
            new_row = self.position[0] + dx
            new_col = self.position[1] + dy
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board.grid[new_row][new_col]
                if not isinstance(target_piece, Piece) or target_piece.color != self.color:
                    possible_moves.append((new_row, new_col))

        return possible_moves

    def __str__(self):
        return 'N' if self.color == 'white' else 'n'


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        # Слон может двигаться по диагонали
        valid_moves = []

        # Проверяем возможные ходы вправо-вверх
        i, j = self.position
        while i > 0 and j < 7:
            i -= 1
            j += 1
            if isinstance(board.grid[i][j], Piece):
                if board.grid[i][j].color != self.color:
                    valid_moves.append((i, j))
                break
            valid_moves.append((i, j))

        # Проверяем возможные ходы вправо-вниз
        i, j = self.position
        while i < 7 and j < 7:
            i += 1
            j += 1
            if isinstance(board.grid[i][j], Piece):
                if board.grid[i][j].color != self.color:
                    valid_moves.append((i, j))
                break
            valid_moves.append((i, j))

        # Проверяем возможные ходы влево-вверх
        i, j = self.position
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if isinstance(board.grid[i][j], Piece):
                if board.grid[i][j].color != self.color:
                    valid_moves.append((i, j))
                break
            valid_moves.append((i, j))

        # Проверяем возможные ходы влево-вниз
        i, j = self.position
        while i < 7 and j > 0:
            i += 1
            j -= 1
            if isinstance(board.grid[i][j], Piece):
                if board.grid[i][j].color != self.color:
                    valid_moves.append((i, j))
                break
            valid_moves.append((i, j))

        return valid_moves

    def get_possible_moves(self, board):
        possible_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            new_row, new_col = self.position[0] + dx, self.position[1] + dy
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board.grid[new_row][new_col]
                if not isinstance(target_piece, Piece) or target_piece.color != self.color:
                    possible_moves.append((new_row, new_col))
                    if isinstance(target_piece, Piece):
                        break
                else:
                    break
                new_row, new_col = new_row + dx, new_col + dy

        return possible_moves

    def __str__(self):
        return 'B' if self.color == 'white' else 'b'


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        # Король может двигаться на одну клетку в любом направлении
        valid_moves = []
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for move in moves:
            new_row = self.position[0] + move[0]
            new_col = self.position[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if not isinstance(board.grid[new_row][new_col], Piece) or \
                        board.grid[new_row][new_col].color != self.color:
                    valid_moves.append((new_row, new_col))

        return valid_moves

    def get_possible_moves(self, board):
        possible_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_row, new_col = self.position[0] + dx, self.position[1] + dy
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board.grid[new_row][new_col]
                if not isinstance(target_piece, Piece) or target_piece.color != self.color:
                    possible_moves.append((new_row, new_col))

        return possible_moves

    def __str__(self):
        return 'K' if self.color == 'white' else 'k'


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        # Ферзь может двигаться по горизонтали, вертикали и диагонали
        valid_moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        for direction in directions:
            row, col = self.position
            d_row, d_col = direction
            while 0 <= row + d_row < 8 and 0 <= col + d_col < 8:
                row += d_row
                col += d_col
                if isinstance(board.grid[row][col], Piece):
                    if board.grid[row][col].color != self.color:
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))

        return valid_moves

    def get_possible_moves(self, board):
        possible_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_row, new_col = self.position[0] + dx, self.position[1] + dy
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board.grid[new_row][new_col]
                if not isinstance(target_piece, Piece) or target_piece.color != self.color:
                    possible_moves.append((new_row, new_col))
                    if isinstance(target_piece, Piece) and target_piece.color != self.color:
                        break
                else:
                    break
                new_row += dx
                new_col += dy

        return possible_moves

    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'


class Board:
    def __init__(self):
        self.grid = self.initialize_board()
        self.white_eaten_pieces = []
        self.black_eaten_pieces = []

    def initialize_board(self):
        # Создаем пустую доску 8x8
        board = [['.' for _ in range(8)] for _ in range(8)]

        # Расставляем начальные фигуры на доске
        # Например, пешки
        for i in range(8):
            board[1][i] = Pawn('white', (1, i))
            board[6][i] = Pawn('black', (6, i))

        board[0][0] = Rook('white', (0, 0))
        board[0][7] = Rook('white', (0, 7))
        board[7][0] = Rook('black', (7, 0))
        board[7][7] = Rook('black', (7, 7))

        board[0][1] = Knight('white', (0, 1))
        board[0][6] = Knight('white', (0, 6))
        board[7][1] = Knight('black', (7, 1))
        board[7][6] = Knight('black', (7, 6))

        board[0][2] = Bishop('white', (0, 2))
        board[0][5] = Bishop('white', (0, 5))
        board[7][2] = Bishop('black', (7, 2))
        board[7][5] = Bishop('black', (7, 5))

        board[0][3] = King('white', (0, 3))
        board[7][4] = King('black', (7, 4))

        board[0][4] = Queen('white', (0, 4))
        board[7][3] = Queen('black', (7, 3))

        return board

    def display_board(self, color):
        """
        Отображает текущее состояние доски в консоли.
        """
        # Вызываем метод threatened_pieces для определения фигур, находящихся под угрозой
        threatened_positions = self.threatened_pieces(color)

        # Отображаем текущее состояние доски в консоли
        for row in range(8):
            for col in range(8):
                if (row, col) in threatened_positions:
                    print(f"*{self.grid[row][col]}", end=" ")
                else:
                    print(self.grid[row][col], end=" ")
            print()

    def threatened_pieces(self, color):
        """
        Возвращает информацию о фигурах текущего игрока, которые находятся под угрозой.

        Возвращаемое значение:
        Список кортежей (row, col) с позициями фигур, находящихся под угрозой.
        """
        threatened = []

        # Перебираем все фигуры на доске
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if isinstance(piece, Piece) and piece.color == color:
                    # Получаем возможные ходы для текущей фигуры
                    moves = piece.get_possible_moves(self)
                    # Проверяем, есть ли среди этих ходов позиции фигур противника
                    for move in moves:
                        target_piece = self.grid[move[0]][move[1]]
                        if isinstance(target_piece, Piece) and target_piece.color != color:
                            threatened.append((row, col))  # Добавляем позицию текущей фигуры

        return threatened

    def display_help(self, color, selected_piece_position=None, possible_moves=None):
        """
        Отображает текущее состояние доски в консоли с учетом возможных ходов для выбранной фигуры.

        Параметры:
         - selected_piece_position: позиция выбранной фигуры (в виде кортежа (row, col)),
           если фигура не выбрана, передайте None.
         - possible_moves: словарь с возможными ходами для выбранной фигуры,
           где ключами являются позиции фигур (в виде кортежей (row, col)),
           а значениями - списки кортежей (row, col) возможных позиций для хода этой фигуры.
        """

        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if selected_piece_position is not None and possible_moves is not None \
                        and selected_piece_position in possible_moves \
                        and (row, col) in possible_moves[selected_piece_position]:
                    print("*", end="")
                if isinstance(piece, Piece) and (row, col) in possible_moves and \
                        possible_moves[(row, col)]:
                    target_piece = self.grid[row][col]
                    if isinstance(target_piece, Piece) and target_piece.color != color:
                        print("P", end=" ")
                        continue
                print(f"{piece} ", end="")
            print()

    def add_eaten_piece(self, piece, color):
        if color == 'white':
            self.white_eaten_pieces.append(piece)
        elif color == 'black':
            self.black_eaten_pieces.append(piece)

    def move_piece(self, start_position, end_position):
        # Получаем фигуру, которую нужно переместить
        start_row, start_col = start_position
        piece = self.grid[start_row][start_col]

        end_row, end_col = end_position
        if isinstance(self.grid[end_row][end_col], Piece):
            eaten_piece = self.grid[end_row][end_col]
            self.add_eaten_piece(eaten_piece, piece.color)

        # Проверяем, является ли piece фигурой (экземпляром класса Piece)
        if isinstance(piece, Piece):
            # Устанавливаем новую позицию фигуры
            piece.position = end_position

        # Перемещаем фигуру на новую позицию
        end_row, end_col = end_position
        self.grid[end_row][end_col] = piece
        self.grid[start_row][start_col] = '.'

    def get_piece(self, position):
        row, col = position
        return self.grid[row][col]


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'
        self.moves_history = []

    def start(self):
        while True:
            color = self.current_turn
            self.board.display_board(color)
            print(f"Turn: {self.current_turn}")
            print('Введите позицию фигуры')
            start_position = self.get_user_input()

            if start_position == "undo":
                print('Введите количество ходов, на которые хотите откатиться')
                n = int(input())
                self.undo_last_move(n)
                continue

            possible_moves = self.get_possible_moves(start_position)
            f_col = self.current_turn
            self.board.display_help(f_col, start_position, possible_moves)
            print('Введите позицию, куда хотите переместиться')
            end_position = self.get_user_input()

            if self.validate_move(start_position, end_position):
                self.make_move(start_position, end_position)

                self.current_turn = 'black' if self.current_turn == 'white' else 'white'

            else:
                print("Invalid move. Please try again.")

    def get_possible_moves(self, position):
        """
        Возвращает список возможных ходов для всех фигур указанного цвета на текущей доске.

        Параметры:
         - color: цвет фигур, для которых нужно получить возможные ходы ('white' или 'black').

        Возвращаемое значение:
        Словарь, где ключами являются позиции фигур (в виде кортежей (row, col)),
        а значениями - списки кортежей (row, col) возможных позиций для хода этой фигуры.
        """
        possible_moves = {}

        # Перебираем все фигуры на доске
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if isinstance(piece, Piece) and piece.color == self.current_turn:
                    # Получаем возможные ходы для текущей фигуры
                    moves = piece.get_possible_moves(self.board)
                    if moves:
                        # Если есть возможные ходы, добавляем их в словарь
                        possible_moves[(row, col)] = moves

        return possible_moves

    @staticmethod
    def get_user_input():
        while True:
            user_input = input()
            # Проверяем, является ли введенная команда "undo"
            if user_input.lower() == "undo":
                return user_input.lower()
            # Проверяем, что пользователь ввел два символа (например, A2)
            if len(user_input) == 2:
                column = user_input[0].upper()
                row = user_input[1]
                # Проверяем, что первый символ - буква от A до H, а второй - цифра от 1 до 8
                if column in 'ABCDEFGH' and row in '12345678':
                    # Преобразуем введенные символы в координаты на доске
                    column_index = ord(column) - ord('A')
                    row_index = int(row) - 1
                    return row_index, column_index
            print("Invalid input. Please enter a valid position (e.g., A2).")

    def validate_move(self, start_position, end_position):
        # Проверяем, что начальная и конечная позиции находятся в пределах доски
        if not (0 <= start_position[0] < 8 and 0 <= start_position[1] < 8 and
                0 <= end_position[0] < 8 and 0 <= end_position[1] < 8):
            return False

        # Проверяем, что начальная позиция не пуста и на ней стоит фигура игрока, который сейчас делает ход
        if not isinstance(self.board.grid[start_position[0]][start_position[1]], Piece) or \
                self.board.grid[start_position[0]][start_position[1]].color != self.current_turn:
            return False

        # Получаем возможные ходы для фигуры из начальной позиции
        valid_moves = self.board.grid[start_position[0]][start_position[1]].valid_moves(self.board)

        # Проверяем, что конечная позиция находится в списке возможных ходов для фигуры
        if end_position not in valid_moves:
            return False

        # Если все проверки пройдены успешно, возвращаем True (ход допустим)
        return True

    def make_move(self, start_position, end_position):
        piece = self.board.get_piece(start_position)
        if isinstance(piece, Piece):  # Проверяем, является ли piece объектом класса Piece
            piece.position = end_position
        self.moves_history.append((start_position, end_position, piece))
        self.board.move_piece(start_position, end_position)

    def undo_last_move(self, n):
        if len(self.moves_history) < n:
            print("No moves to undo.")
            return
        for i in range(n):
            last_move = self.moves_history.pop()
            start_position, end_position, piece = last_move
            self.board.move_piece(end_position, start_position)
            print("Last move undone.")


class Checkers:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'white'

    def create_board(self):
        board = [['.' for ro in range(8)] for col in range(8)]
        board[0][1] = 'O'
        board[0][3] = 'O'
        board[0][5] = 'O'
        board[0][7] = 'O'
        board[1][0] = 'O'
        board[1][2] = 'O'
        board[1][4] = 'O'
        board[1][6] = 'O'
        board[2][1] = 'O'
        board[2][3] = 'O'
        board[2][5] = 'O'
        board[2][7] = 'O'

        board[7][0] = 'o'
        board[7][2] = 'o'
        board[7][4] = 'o'
        board[7][6] = 'o'
        board[6][1] = 'o'
        board[6][3] = 'o'
        board[6][5] = 'o'
        board[6][7] = 'o'
        board[5][0] = 'o'
        board[5][2] = 'o'
        board[5][4] = 'o'
        board[5][6] = 'o'
        return board

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]

        if piece == '.':
            print("Invalid move: Empty cell.")
            return False

        if (end_row + end_col) % 2 != 0:
            print("Invalid move: Destination cell is not valid.")
            return False

        if self.board[end_row][end_col] != '.':
            print("Invalid move: Destination cell is not empty.")
            return False

        if self.current_player == 'white' and piece != 'o':
            print("Invalid move: It's white player's turn.")
            return False

        if self.current_player == 'black' and piece != '.':
            print("Invalid move: It's black player's turn.")
            return False

        if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
            print("Invalid move: Piece can only move diagonally by one cell.")
            return False

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '.'
        return True

    def is_valid_move(self, start_pos, end_pos):
        pass  # Implement validation of move here

    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    @staticmethod
    def main():
        game = Checkers()
        while True:
            game.display_board()
            print(f"It's {game.current_player}'s turn.")
            start_pos = input("Enter start position (row col): ").split()
            end_pos = input("Enter end position (row col): ").split()
            start_pos = tuple(map(int, start_pos))
            end_pos = tuple(map(int, end_pos))

            if game.is_valid_move(start_pos, end_pos):
                game.move_piece(start_pos, end_pos)
                game.switch_player()
            else:
                print("Invalid move. Try again.")


print('шахматы - 1, шашки - 2')
num = int(input())
if num == 1:
    if __name__ == "__main__":
        game = Game()
        game.start()
else:
    if __name__ == "__main__":
        Checkers.main()
