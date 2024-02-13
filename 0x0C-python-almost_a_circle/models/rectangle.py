#!/usr/bin/python3
""" Defines the class Rectangle that inherits the Base """
from models.base import Base


class Rectangle(Base):
    """ The class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the constructor attributes of the class rectangle """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Set the width of the rectangle """
        return self.__width

    @property
    def height(self):
        """ Set the height of the rectangle """
        return self.__height

    @property
    def x(self):
        """ Set the x of the rectangle """
        return self.__x

    @property
    def y(self):
        """ Set the y of the rectangle """
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the stdout rectangle with the characte '#' """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """ Returns the str id and rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.width,
                                                       self.height, self.x,
                                                       self.y)

    def to_dictionary(self):
        """ Return the dictionary representation of a rectangle """
        return {
            "id": self.id,
            "weight": self.weight,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Update the recrangel args and kwargs """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = k
                elif j == "width":
                    self.width = k
                elif j == "height":
                    self.height = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k
