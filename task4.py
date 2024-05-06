import math


class GeometricObject:
    """
    Attributes:
    -----------
    - x (float): The x-coordinate of the geometric object. Default is 0.0.
    - y (float): The y-coordinate of the geometric object. Default is 0.0.
    - color (str): The color of the geometric object. Default is 'black'.
    - filled (bool): Whether the geometric object is filled or not. Default is False.

    Methods:
    --------
    - __init__(self, x=0.0, y=0.0, color='black', filled=False): Initializes a geometric object.
    - set_coordinate(self, x, y): Sets the coordinates of the geometric object.
    - set_color(self, color): Sets the color of the geometric object.
    - set_filled(self, filled): Sets whether the geometric object is filled or not.
    - get_x(self): Returns the x-coordinate of the geometric object.
    - get_y(self): Returns the y-coordinate of the geometric object.
    - get_color(self): Returns the color of the geometric object.
    - is_filled(self): Returns whether the geometric object is filled or not.
    - __str__(self): Returns a string representation of the geometric object.
    - __repr__(self): Returns a printable representation of the geometric object.
    """

    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        self.__x = x
        self.__y = y
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):
        self.__x = x
        self.__y = y

    def set_color(self, color):
        self.color = color

    def set_filled(self, filled):
        self.filled = filled

    def get_x(self):
        return float(self.__x)

    def get_y(self):
        return float(self.__y)

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def __str__(self):
        return f'({float(self.__x)}, {float(self.__y)})\ncolor:{self.color}\nfilled: {self.filled}'

    def __repr__(self):
        return self.__str__()


class Rectangle(GeometricObject):
    """
    Attributes:
    -----------
    - x (float): The x-coordinate of the geometric object. Default is 0.0.
    - y (float): The y-coordinate of the geometric object. Default is 0.0.
    - width (float): The width of the geometric object. Default is 0.0.
    - height (float): The height of the geometric object. Default is 0.0.
    - color (str): The color of the geometric object. Default is 'black'.
    - filled (bool): Whether the geometric object is filled or not. Default is False.

    Methods:
    --------
    - set_width(self, width): Sets the width of the rectangle.
    - set_height(self, height): Sets the height of the rectangle.
    - get_width(self): Returns the width of the rectangle.
    - get_height(self): Returns the height of the rectangle.
    - get_area(self): Returns the area of the rectangle.
    - get_perimeter(self): Returns the perimeter of the rectangle.
        """

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if width >= 0:
            self.width = float(width)
        else:
            self.width = 0.0
        if height >= 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def set_width(self, width):
        if width >= 0:
            self.width = float(width)
        else:
            self.width = 0.0

    def set_height(self, height):
        if height >= 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def get_width(self):
        return float(self.width)

    def get_height(self):
        return float(self.height)

    def get_area(self):
        return float(self.width * self.height)

    def get_perimetr(self):
        return float(self.width * 2 + self.height * 2)

    def __str__(self):
        return (f'width:{self.width}\nhight:{self.height}\n({self.get_x()}, {self.get_y()})\ncolor:{self.color}\n'
                f'filled:{self.filled}')

    def __repr__(self):
        return self.__str__()


class Circle(GeometricObject):
    """
    Attributes:
    -----------
    - x (float): The x-coordinate of the geometric object. Default is 0.0.
    - y (float): The y-coordinate of the geometric object. Default is 0.0.
    - radius (float): The radious of the geometric object. Default is 0.0.
    - color (str): The color of the geometric object. Default is 'black'.
    - filled (bool): Whether the geometric object is filled or not. Default is False.

    Methods:
    --------
    - radius_setter(self, radius): Sets the radius of the circle.
    - radius_getter(self): Returns the radius of the circle.
    - get_area(self): Returns the area of the circle.
    - get_perimeter(self): Returns the perimeter of the circle.
    - get_diameter(self): Returns the diameter of the circle.
        """

    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if radius >= 0:
            self.radius = float(radius)
        else:
            self.radius = 0.0

    def radius_setter(self, radius):
        if radius >= 0:
            self.radius = float(radius)
        else:
            self.radius = 0.0

    def radius_getter(self):
        return float(self.radius)

    def get_area(self):
        return float((self.radius ** 2) * math.pi)

    def get_perimetr(self):
        return float(self.radius * 2 * math.pi)

    def get_diametr(self):
        return float(self.radius * 2)

    def __str__(self):
        return f'radius:{self.radius}\n({self.get_x()}, {self.get_y()})\ncolor:{self.color}\nfilled: {self.filled}'

    def __repr__(self):
        return self.__str__()


point = GeometricObject()
print(point)
print()
point.set_coordinate(-4, 9)
print(point.get_x())
print(point.get_y())
point.set_color('red')
print(point.get_color())
point.set_filled(True)
print(point.is_filled())
print()
print(point)
print()
point_2 = GeometricObject(8, -4, 'blue', True)
print(point_2)
print()
circle = Circle()
print(circle)
print()
circle.radius = -34
print(circle.radius)
circle.radius = 12
print(circle.radius)
print()
circle_2 = Circle(3, -100, 20, 'green', True)
print(circle_2)
print()
circle_2.set_color('grey')
print(circle_2.get_color())
print()
print(circle_2.get_area())
print(circle_2.get_perimetr())
print(circle_2.get_diametr())
print()
circle_3 = Circle(90, -84, -223, 'pink')
print(circle_3)
print()
rectangle = Rectangle()
print(rectangle)
print()
rectangle.set_coordinate(11, 29)
rectangle.set_color('yellow')
rectangle.set_width(-10)
rectangle.set_height(20)
print(rectangle)
print()
rectangle.set_width(100)
print(rectangle.get_width())
print(rectangle.get_height())
print()
print(rectangle.get_area())
print(rectangle.get_perimetr())
print()
rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
print(rectangle_2)
print()
figures = []
figures.append(point)
figures.append(circle_2)
figures.append(rectangle)
print(figures)
