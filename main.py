from graph import *

win = Window(800, 600)
# point1 = Point(555, 50)
# point2 = Point(100, 500)
# line = Line(point1, point2)
# cell1 = Cell(win)
# cell1.draw(100, 100, 200, 200)

# cell2 = Cell(win)
# cell2.draw(400, 400, 550, 550)

# cell1.draw_move(cell2)
maze = Maze(300, 300, 10, 10, 50, 50, win, 10)
win.wait_for_close()