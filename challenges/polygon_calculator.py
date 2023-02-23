class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width**2 + self.height**2)**.5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return "Too big for picture."

        line_width = '*' * self.width + '\n'
        picture = line_width * self.height

        return picture

    def get_amount_inside(self, figure):
        height_space = self.height // figure.height
        width_space = self.width // figure.width

        inside_space = height_space * width_space
        return inside_space

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"
