from graphics import Window, Line, Point


class Cell:
    def __init__(self, win: Window|None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = win

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win != None:
            if self.has_left_wall:
                fill_color = "black"
            else:
                fill_color = "white"
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, fill_color)
            if self.has_right_wall:
                fill_color = "black"
            else:
                fill_color = "white"
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall, fill_color)
            if self.has_top_wall:
                fill_color = "black"
            else:
                fill_color = "white"
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall, fill_color)
            if self.has_bottom_wall:
                fill_color = "black"
            else:
                fill_color = "white"
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall, fill_color)

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if undo:
            color = "red"
        else:
            color = "gray"
        from_center = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        to_center = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        line = Line(from_center, to_center)
        if self.__win != None:
            self.__win.draw_line(line, color)