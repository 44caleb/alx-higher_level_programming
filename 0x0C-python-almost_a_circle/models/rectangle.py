#!/usr/bin/python3
"""creates a rectangle subclass"""

from models.base import Base


class Rectangle(Base):
    """creates a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle shape"""
        print("\n" * self.__y, end="")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """string representation of object"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """update the rectangle attributes"""
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(0, len(args)):
                setattr(self, attr[i], args[i])
        else:
            if kwargs is not None:
                pairs = kwargs.items()
                for key, value in pairs:
                    setattr(self, key, value)

    def to_dictionary(self):
        dict_rep = {}
        keys = ["id", "width", "height", "x", "y"]
        for key in keys:
            dict_rep[key] = getattr(self, key)
        return dict_rep
