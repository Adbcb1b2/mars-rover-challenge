class Plateau:
    """
    A class used to represent a rectangular plateau

    Attributes
    ----------
    width: int
        The width of the plateau (positive integer)

    height: int
        The height of the plateau (positive integer)

    Methods
    ----------
    is_within_plateau(self, x_position, y_position)
        Checks coordinatres are within the bounds of the plateau

    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width: int
            the horizontal length of the plateau (default = 0)
        
        height: int
            the vertical length of the plateau (default = 0)
        """

        self.__width = width
        self.__height = height

    # Getter for width 
    @property
    def width(self):
        return self.__width
    
    # Setter for the width
    @width.setter
    def width(self, value):
        """
        Sets the width of the plateau

        Ensures the width is a positive integer

        Raises
        ------
        ValueError
            If the value is not a positive integer
        """
        if isinstance(value, int) and value >= 0:
            self.__width = value
        else:
            raise ValueError("Width must be a positive integer")
    
    # Getter for the height
    @property
    def height(self):
        return self.__height
    
    # Setter for the height
    @height.setter
    def height(self, value):
        """
        Sets the height of the plateau

        Ensures the height is a positive integer

        Raises
        ------
        ValueError
            If the value is not a positive integer
        """
        if isinstance(value, int) and value >= 0:
            self.__height = value
        else:
            raise ValueError("Height must be a positive integer")
        
    def is_within_plateau(self, x_position, y_position):
        """
        Checks whether x and y coordinates are within the plateau dimensions

        Returns
        -------
        bool
            True if within the plateau, False if not within plateau
        """

        return 0 <= x_position <= self.__width and 0 <= y_position <= self.__height




