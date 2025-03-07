from Plateau import Plateau
class Rover:
    """ 
    A class used to represent a Rover

    Attributes
    ----------
    x_position: int
        the horizontal position of the rover (positive integer)

    y_position: int
        the vertical position of the rover (positive integer)

    heading: str
        the direction in which the rover is facing ('N', 'E', 'W', 'S')

    plateau: Plateau
        the plateau on which the rover is moving

    Methods
    ----------
    turn_left(self)
        Changes the direction of the rover by 90 degrees anti-clockwise e.g. the heading 'N' becomes 'W'

    turn_right(self)
        Changes the direction of the rover by 90 degrees clockwise e.g. the heading 'N' becomes 'E'

    move(self)
        Move the rover one space in the direction of the current heading, checking the new space will be within bounds
    """

    def __init__(self, x_position=0, y_position=0, heading='N', plateau=None):
        """ 
        Parameters
        ----------
        x_position: int
            the horizontal position of the rover (default = 0)

        y_position: int
            the vertical position of the rover (default = 0)

        heading: str
            the direction in which the rover is facing ('N', 'E', 'W', 'S') (default = 'N')

        plateau: Plateau
            the plateau on which the rover is positioned (default is None)
        
        """
        # Private variables, not to be directly manipulated outside of the class
        self.__x_position = x_position
        self.__y_position = y_position
        self.__heading = heading
        self.__plateau = plateau

    # Getter for x position
    @property
    def x_position(self):
        return self.__x_position

    # Setter for x position
    @x_position.setter
    def x_position(self, value):
        """
        Sets the x_position of the rover

        Ensures x_position is a positive integer

        Raises
        ------
        ValueError
            If the value is not a positive integer
        """
        if isinstance(value, int) and value >= 0:
            self.__x_position = value
        else:
            raise ValueError("x position must be a positive integer")

    # Getter for y position
    @property 
    def y_position(self):
        return self.__y_position

    # Setter for y position
    @y_position.setter
    def y_position(self, value):
        """
        Sets the y_position of the rover

        Ensures y_position is a positive integer
        
        Raises
        ------
        ValueError
            If the value is not a positive integer
        """
        if isinstance(value, int) and value >= 0:
            self.__y_position = value
        else:
            raise ValueError("y position must be a positive integer")

    # Getter for heading
    @property
    def heading(self):
        return self.__heading
    
    # Setter for heading 
    @heading.setter
    def heading(self, value):
        """
        Sets the heading of the rover

        Includes validation to ensure heading only accepts 'N', 'E', 'S' or 'W'

        Raises
        ------
        ValueError
            If the value is not in ('N', 'E', 'S', 'W')
        """
        if value in ('N', 'E', 'S', 'W'):
            self.__heading = value
        else:
            raise ValueError("Heading value must be 'N', 'E', 'S' or 'W'")
        
    # Getter for plateau
    @property
    def plateau(self):
        return self.__plateau

    # Setter for plateau
    @plateau.setter
    def plateau(self, value):
        """
        Sets the plateau for the rover

        Ensures the plateau is an instance of the Plateau class.
        """
        if isinstance(value, Plateau):
            self.__plateau = value
        else:
            raise ValueError("Plateau must be an instance of the Plateau class.")
        
        
    # Method to change rover direction by 90 degrees left
    def turn_left(self):
        """
        Rotates the rover 90 degrees anti-clockwise

        Updates the 'heading' attribute, depending on the current direction
        """
        left_rotation_mapping = {"N": "W", "E": "N", "S": "E", "W": "S"}
        self.heading = left_rotation_mapping[self.__heading]

    # Method to change rover direction by 90 degrees right
    def turn_right(self):
        """
        Rotates the rover 90 degrees clockwise

        Updates the 'heading' attribute, depending on the current direction
        """
        right_rotation_mapping = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.heading = right_rotation_mapping[self.__heading]

    # Method to move the rover, directiond determined by current heading
    def move(self):
        """
`       Moves the rover one unit forward, in the direction of the current heading

        checks the movement will be within the bounds of the plateau before returning.

        Raises
        ------
        ValueError
            If the movement takes the rover out of the plateau
        """
        # Calculate the new position
        new_x, new_y = self.x_position, self.y_position

        if self.heading == 'N':
            new_x, new_y = self.x_position, self.y_position + 1
        elif self.heading == 'E':
            new_x, new_y = self.x_position + 1, self.y_position
        elif self.heading == 'S':
            new_x, new_y = self.x_position, self.y_position - 1
        elif self.heading == 'W':
            new_x, new_y = self.x_position - 1, self.y_position

        # Check if the move is within bounds before updating position
        if self.plateau.is_within_plateau(new_x, new_y):
            self.x_position, self.y_position = new_x, new_y
        else:
            raise ValueError("Cannot move rover out of plateau bounds")
            
