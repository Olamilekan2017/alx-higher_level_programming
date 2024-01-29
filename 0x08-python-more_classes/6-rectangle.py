#!/usr/bin/python3
""" The function returns a Rectangle """


class Rectangle:
    """ Represent the rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Prints a message when an instance has been deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Returns the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the Area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Returns a string representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            rectangle_str = "\n".join("#" * self.__width
                                      for j in range(self.__height))
            return (rectangle_str)

    def __repr__(self):
        """ Return string represntation of the rectangle for production """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ Print a message for every deletion of a rectangle """
        print("Bye rectangle...")
