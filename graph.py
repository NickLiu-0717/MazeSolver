from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
      
    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.top_left_corner = Point(self.__x1, self.__y1)
        self.bottom_right_corner = Point(self.__x2, self.__y2)
        self.top_right_corner = Point(self.__x2, self.__y1)
        self.bottom_left_corner = Point(self.__x1, self.__y2)
        if self.has_left_wall is True:
            left_wall = Line(self.top_left_corner, self.bottom_left_corner)
            self.__win.draw_line(left_wall)
        if self.has_right_wall is True:
            right_wall = Line(self.top_right_corner, self.bottom_right_corner)
            self.__win.draw_line(right_wall)
        if self.has_top_wall is True:
            top_wall = Line(self.top_left_corner, self.top_right_corner)
            self.__win.draw_line(top_wall)
        if self.has_bottom_wall is True:
            bottom_wall = Line(self.bottom_left_corner, self.bottom_right_corner)
            self.__win.draw_line(bottom_wall)