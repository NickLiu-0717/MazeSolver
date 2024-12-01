from graph import *

win = Window(800, 600)
maze = Maze(100, 100, 15, 15, 40, 40, win, 150)
solve = maze.solve()
win.wait_for_close()