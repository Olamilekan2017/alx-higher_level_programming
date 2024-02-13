#!/usr/bin/python3
""" Defines the class Square with the attributes Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new class square """

        super() .__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Return the str representation of a square """
        return "[square] ({}) {}/{} - {}".formatt(self.id, self.x, self.y,
                                                  self.width)

    def update(self, *args, **kwargs):
        """ Update the square """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k
