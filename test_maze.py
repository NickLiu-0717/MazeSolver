import unittest
from graph import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
        num_cols = 15
        num_rows = 15
        m1 = Maze(150, 150, num_rows, num_cols, 15, 15)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_wall(self):
        win = Window(800, 600)
        num_cols = 5
        num_rows = 5
        m1 = Maze(300, 300, num_rows, num_cols, 50, 50, win)
        
if __name__ == "__main__":
    unittest.main()