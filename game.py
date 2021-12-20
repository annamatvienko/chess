class state():
    '''
    класс state используется для отслеживания игрового прогресса, 
    описывает движения фигур, их положение как начальное так и внутриигровое,
    содержит две функции построение доски, движения фигур
    ----------
    атрибуты:
    -----------
    debug - для прохождения теста на мат
    методы:
    -----------
    move_piece(step) - делает шаг
    undo_step() - отменяет шаг
    checkmate() - проверяет был ли мат
    '''
    def __init__(self, debug=False):
        '''
        функция описывает построение доски, то есть начальное расположение
        всех фигур, также содержит информацию о том, чья очередь ходить
        и о вхождениях
        параметры:
        -----------
        сh_b - chessboard
        white - очерёдность хода: True - белые, False - чёрные
        log - вхождения
        '''
        self.debug = debug
        self.ch_b = [
        ['castle_b', 'knight_b', 'bishop_b', 'queen_b', 'king_b', 'bishop_b',
        'knight_b','castle_b'],
        ['pawn_b','pawn_b','pawn_b','pawn_b','pawn_b','pawn_b','pawn_b',
        'pawn_b'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['pawn_w','pawn_w','pawn_w','pawn_w','pawn_w','pawn_w','pawn_w',
        'pawn_w'],
        ['castle_w', 'knight_w', 'bishop_w', 'queen_w', 'king_w', 'bishop_w',
        'knight_w','castle_w']
        ]       
        self.white = True
        self.log = []


    def move_piece(self, step):
        '''
        функция передвижения фигур
        p2q - при становлении пешки на край доски предоставляет выбор на какую
        фигуру меняется пешка вводом консольной команды (берётся по мод 3
        ладья - 0, конь - 1, слон - 2, королева/ферзь - 3)
        castling - рокировка (функция отмены хода для неё на данный момент 
        нормально не работает) рокировка должна начинаться с короля
        '''
        piece = ['castle', 'knight', 'bishop', 'queen']
        self.ch_b[step.st_r][step.st_c] = '-'
        self.ch_b[step.fin_r][step.fin_c] = step.moving_piece
        self.log.append(step)
        self.white = not(self.white)
        if step.p2q:
            i = int(input()) % 4 
            self.ch_b[step.fin_r][step.fin_c] = piece[i] \
            + step.moving_piece[-2:]
        if step.castling:
            if step.st_c > step.fin_c:
                self.ch_b[step.fin_r][step.fin_c] = '-'
                self.ch_b[step.fin_r][step.st_c - 2] = step.moving_piece
                self.ch_b[step.st_r][step.st_c - 1] = 'castle' \
                    + step.moving_piece[-2:]
            else:
                self.ch_b[step.fin_r][step.fin_c] = '-'
                self.ch_b[step.fin_r][step.st_c + 2] = step.moving_piece
                self.ch_b[step.st_r][step.st_c + 1] = 'castle' \
                    + step.moving_piece[-2:]


    def undo_step(self):
        '''
        функция отмены хода (в игре работает посредством нажатия пробела)
        сh_b - chessboard
        white - очерёдность хода: True - белые, False - чёрные
        '''
        if len(self.log) != 0:
            move = self.log.pop()
            self.ch_b[move.st_r][move.st_c] = move.moving_piece
            self.ch_b[move.fin_r][move.fin_c] = move.capture
            self.white = not(self.white)
    

    def checkmate(self):
        '''
        функция завершения игры. чтобы завершить игру необходимо убить короля
        k_w = 0
        k_b = 0
        счётчики королей, если на поле нет короля какой-то команды победитель
        выводится на консоль
        '''
        k_w = 0
        k_b = 0
        for r in range(8):
            for c in range(8):
                if self.ch_b[r][c] == 'king_w':
                    k_b += 1
                elif self.ch_b[r][c] == 'king_b':
                    k_w += 1
        if k_w == 0:
            if not self.debug:
                print('White Wins')
                exit()
            else:
                f = open('output.txt', 'w')
                f.write('White Wins')
                f.close()

        elif k_b == 0:
            if not self.debug:
                print('Black Wins')
                exit()
            else:
                f = open('output.txt', 'w')
                f.write('Black Wins')
                f.close()


class Moving():
    '''
    класс описывает движение фигур
    атрибуты:
    -----------
    st_sq - стартовое поле
    fin_sq - конечное поле
    ch_b - доска
    '''
    def __init__(self, st_sq, fin_sq, ch_b):
        '''
        функция указывает на начальное положение фигуры и на конечное
        также описывает превращение пешки в любую другую фигуру, которую
        необходимо выбрать с помощью консольной команды вводом цифры в
        промежутке от нуля до трёх 
        st_sq - стартовый квадрат
        fin_sq - финальный квадрат
        сh_b - chessboard
        '''
        self.st_r = st_sq[0]
        self.st_c = st_sq[1]
        self.fin_r = fin_sq[0]
        self.fin_c = fin_sq[1]
        self.moving_piece = ch_b[self.st_r][self.st_c]
        self.capture = ch_b[self.fin_r][self.fin_c]
        self.p2q = False
        if (self.moving_piece == 'pawn_w' and self.fin_r == 0)\
        or (self.moving_piece == 'pawn_b' and self.fin_r == 7):
            self.p2q = True
        self.castling = False
        if (self.moving_piece == 'king_w' and self.capture == 'castle_w' \
            and self.fin_r == self.st_r)\
        or (self.moving_piece == 'king_b' and self.capture == 'castle_b' \
            and self.fin_r == self.st_r):
            self.castling = True
