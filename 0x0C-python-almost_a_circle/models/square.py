#!/usr/bin/python3
"""creates the square subclass"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """creates square subclass"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """object string representation"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square attributes"""
        attr = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns object dictionary representation"""
        dict_rep = {}
        keys = ["id", "size", "x", "y"]
        for key in keys:
            dict_rep[key] = getattr(self, key)
        return dict_rep
