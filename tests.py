import unittest
from game import state, Moving
import sys


class TestMove(unittest.TestCase):

    def test_move_piece(self):
        lol = state()
        last = []
        col = 1
        row = 1
        piece = lol.ch_b[row][col]
        col2 = 6
        row2 = 4
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], lol.ch_b)
        lol.move_piece(move)
        self.assertEqual(lol.ch_b[row2][col2], piece)

        last = []
        col = 1
        row = 0
        piece = lol.ch_b[row][col]
        col2 = 4
        row2 = 6
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], lol.ch_b)
        lol.move_piece(move)
        self.assertEqual(lol.ch_b[row2][col2], piece)


    def test_castling(self):
        rofl = state()
        last = []
        col = 4
        row = 0
        piece = rofl.ch_b[row][col]
        col2 = 7
        row2 = 0
        piece2 = rofl.ch_b[row2][col2]
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], rofl.ch_b)
        rofl.move_piece(move)
        self.assertEqual(rofl.ch_b[row2][col2-1], piece)
        self.assertEqual(rofl.ch_b[row2][col2-2], piece2)


    def test_p2q(self):
        f = open('input.txt', 'r')
        r = open('input.txt')
        sys.stdin = f
        s = int(r.readline())
        piece1 = ['castle', 'knight', 'bishop', 'queen']
        prekl = state()
        last = []
        col = 4
        row = 1
        col2 = 4
        row2 = 7
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], prekl.ch_b)
        prekl.move_piece(move)
        self.assertEqual(prekl.ch_b[row2][col2], piece1[s]+prekl.ch_b[row2][col2][-2:])
        f.close()
        r.close()


    def test_undo(self):
        rzhaka = state()
        last = []
        col = 1
        row = 1
        piece = rzhaka.ch_b[row][col]
        col2 = 6
        row2 = 4
        piece2 = rzhaka.ch_b[row2][col2]
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], rzhaka.ch_b)
        rzhaka.move_piece(move)
        rzhaka.undo_step()
        self.assertEqual(rzhaka.ch_b[row][col], piece)
        self.assertEqual(rzhaka.ch_b[row2][col2], piece2)


    def test_undo_p2q(self):
        a = open('input.txt', 'r')
        b = open('input.txt')
        sys.stdin = a
        s = int(b.readline())
        piece1 = ['castle', 'knight', 'bishop', 'queen']
        rzhaka = state()
        last = []
        col = 1
        row = 1
        piece = rzhaka.ch_b[row][col]
        col2 = 6
        row2 = 7
        piece2 = rzhaka.ch_b[row2][col2]
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], rzhaka.ch_b)
        rzhaka.move_piece(move)
        self.assertEqual(rzhaka.ch_b[row2][col2], piece1[s]+rzhaka.ch_b[row2][col2][-2:])
        rzhaka.undo_step()
        self.assertEqual(rzhaka.ch_b[row][col], piece)
        self.assertEqual(rzhaka.ch_b[row2][col2], piece2)
        a.close()
        b.close()


    def test_undo_castling(self):
        kek = state()
        last = []
        col = 4
        row = 0
        piece = kek.ch_b[row][col]
        col2 = 7
        row2 = 0
        piece2 = kek.ch_b[row2][col2]
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], kek.ch_b)
        kek.move_piece(move)
        self.assertEqual(kek.ch_b[row2][col2-1], piece)
        self.assertEqual(kek.ch_b[row2][col2-2], piece2)
        kek.undo_step()
        self.assertEqual(kek.ch_b[row][col], piece)
        self.assertEqual(kek.ch_b[row2][col2], piece2)        


    def test_checkmate(self):
        aaa = state(debug = True)
        last = []
        col = 4
        row = 5
        piece = aaa.ch_b[row][col]
        col2 = 4
        row2 = 0
        selection = (row, col)
        last.append(selection)
        selection2 = (row2, col2)
        last.append(selection2)
        move = Moving(last[0], last[1], aaa.ch_b)
        aaa.move_piece(move)
        f = open('output.txt', 'r')
        aaa.checkmate()
        s = f.readline()
        self.assertEqual('White Wins', s)
        f.close()


if __name__ == '__main__':
    unittest.main()

