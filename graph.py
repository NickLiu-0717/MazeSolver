from tkinter import Tk, BOTH, Canvas
import time
import random

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
        self._visited = False
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.top_left_corner = Point(self.__x1, self.__y1)
        self.bottom_right_corner = Point(self.__x2, self.__y2)
        self.top_right_corner = Point(self.__x2, self.__y1)
        self.bottom_left_corner = Point(self.__x1, self.__y2)
        if self.__win is not None:
            if self.has_left_wall is True:
                left_wall = Line(self.top_left_corner, self.bottom_left_corner)
                self.__win.draw_line(left_wall)
            else:
                left_wall = Line(self.top_left_corner, self.bottom_left_corner)
                self.__win.draw_line(left_wall, "white")
            
            if self.has_right_wall is True:
                right_wall = Line(self.top_right_corner, self.bottom_right_corner)
                self.__win.draw_line(right_wall)
            else:
                right_wall = Line(self.top_right_corner, self.bottom_right_corner)
                self.__win.draw_line(right_wall, "white")
            
            if self.has_top_wall is True:
                top_wall = Line(self.top_left_corner, self.top_right_corner)
                self.__win.draw_line(top_wall)
            else:
                top_wall = Line(self.top_left_corner, self.top_right_corner)
                self.__win.draw_line(top_wall, "white")
            
            if self.has_bottom_wall is True:
                bottom_wall = Line(self.bottom_left_corner, self.bottom_right_corner)
                self.__win.draw_line(bottom_wall)
            else:
                bottom_wall = Line(self.bottom_left_corner, self.bottom_right_corner)
                self.__win.draw_line(bottom_wall, "white")
    
    def draw_move(self, to_cell, undo=False):
        self.center = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        self.center_tocell = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        
        if undo == False:
            self.__win.draw_line(Line(self.center, self.center_tocell), "red")
        else:
            self.__win.draw_line(Line(self.center, self.center_tocell), "gray")
            
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self.seed = seed
        if self.seed != None:
            random.seed(seed)
        else:
            random.seed(0)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        self._cells = []
        for _ in range(self._num_cols):
            self._cell_columns = []
            for _ in range(self._num_rows):
                self._cell_columns.append(Cell(self._win))
            self._cells.append(self._cell_columns)
            
        for j in range(self._num_cols):
            for i in range(self._num_rows):
                self._draw_cell(i, j)
        
            
    def _draw_cell(self, i, j):
        self.cell_x1 = self._x1 + (j - 1) * self._cell_size_x
        self.cell_x2 = self._x1 + (j * self._cell_size_x)
        self.cell_y1 = self._y1 + (i - 1) * self._cell_size_y
        self.cell_y2 = self._y1 + (i * self._cell_size_y)
        self._cells[j][i].draw(self.cell_x1, self.cell_y1, self.cell_x2, self.cell_y2)
        if self._win is not None:
            self._animate()
    
    def _animate(self):
        self._win.redraw()  
        time.sleep(0.01)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(self._num_rows -1, self._num_cols -1)
    
    def _break_walls_r(self, i, j):
        while(True):
            self.to_visit = []
            if j - 1 >= 0:
                if self._cells[j-1][i]._visited is False:
                    self.to_visit.append((i, j -1))
            if j + 1 < self._num_cols:
                if self._cells[j+1][i]._visited is False:
                    self.to_visit.append((i, j +1))
            if i + 1 < self._num_rows:
                if self._cells[j][i+1]._visited is False:
                    self.to_visit.append((i + 1, j))
            if i - 1 >= 0:
                if self._cells[j][i-1]._visited is False:
                    self.to_visit.append((i - 1, j))
            if len(self.to_visit) == 0:
                self._draw_cell(i, j)
                return
            choosed_cell = random.choice(self.to_visit)
            if choosed_cell == (i, j - 1):
                self._cells[j - 1][i]._visited = True
                self._cells[j][i].has_left_wall = False
                self._cells[j - 1][i].has_right_wall = False
            elif choosed_cell == (i, j + 1):
                self._cells[j + 1][i]._visited = True
                self._cells[j][i].has_right_wall = False
                self._cells[j + 1][i].has_left_wall = False
            elif choosed_cell == (i + 1, j):
                self._cells[j][i + 1]._visited = True
                self._cells[j][i].has_bottom_wall = False
                self._cells[j][i + 1].has_top_wall = False
            elif choosed_cell == (i - 1, j):
                self._cells[j][i - 1]._visited = True
                self._cells[j][i].has_top_wall = False
                self._cells[j][i - 1].has_bottom_wall = False
            self._break_walls_r(choosed_cell[0], choosed_cell[1])
        
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[j][i]._visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[j][i]._visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        if j - 1 >= 0:
            if self._cells[j-1][i]._visited is False and self._cells[j][i].has_left_wall is False:
                self._cells[j][i].draw_move(self._cells[j-1][i])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[j][i].draw_move(self._cells[j-1][i], undo=True)
        if j + 1 < self._num_cols:
            if self._cells[j+1][i]._visited is False and self._cells[j][i].has_right_wall is False:
                self._cells[j][i].draw_move(self._cells[j+1][i])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[j][i].draw_move(self._cells[j+1][i], undo=True)
        if i + 1 < self._num_rows:
            if self._cells[j][i+1]._visited is False and self._cells[j][i].has_bottom_wall is False:
                self._cells[j][i].draw_move(self._cells[j][i+1])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[j][i].draw_move(self._cells[j][i+1], undo=True)
        if i - 1 >= 0:
            if self._cells[j][i-1]._visited is False and self._cells[j][i].has_top_wall is False:
                self._cells[j][i].draw_move(self._cells[j][i-1])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[j][i].draw_move(self._cells[j][i-1], undo=True)
        return False
        
        