from graph import Window, Point, Line

win = Window(800, 600)
point1 = Point(555, 50)
point2 = Point(100, 500)
line = Line(point1, point2)
win.draw_line(line, "red")
win.wait_for_close()