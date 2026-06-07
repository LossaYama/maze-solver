from time import sleep
import random
from cell import Cell
from graphics import Window


class Maze:
    def __init__(self,
      x1: int, y1: int,
      num_rows: int, num_cols: int,
      cell_size_x: float, cell_size_y: float,
      win: Window|None = None, seed = None
   ) -> None:
        if seed != None:
            random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self) -> None:
        # list of columns [list of rows [ Cells ]]
        for i in range(self.__num_cols):
            col_cells: list[Cell] = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int) -> None:
        x1 = self.__x1 + i * self.__cell_size_x
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        y2 = y1 + self.__cell_size_y
        if self.__win != None:
            self.__cells[i][j].draw(x1, y1, x2, y2)
            self.__animate()

    def __animate(self) -> None:
        self.__win.redraw()
        sleep(0.03)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, i: int, j: int):
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        while True:
            to_visit: list[tuple] = []
            if i-1 >= 0 and self.__cells[i-1][j].visited == False:
                to_visit.append((i-1, j, "left"))
            if i+1 <= self.__num_cols-1 and self.__cells[i+1][j].visited == False:
                to_visit.append((i+1, j, "right"))
            if j-1 >= 0 and self.__cells[i][j-1].visited == False:
                to_visit.append((i, j-1, "top"))
            if j+1 <= self.__num_rows-1 and self.__cells[i][j+1].visited == False:
                to_visit.append((i, j+1, "bottom"))
            
            if to_visit == []:
                self.__draw_cell(i, j)
                return
            else:
                rand_index = random.randrange(0, len(to_visit))
                next_i, next_j, direction =  to_visit[rand_index]
                next_cell = self.__cells[next_i][next_j]
                if direction == "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif direction == "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                elif direction == "top":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif direction == "bottom":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                self.__draw_cell(i, j)
                self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False