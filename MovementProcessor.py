class MovementProcessor:
    """
    A class to apply movement commands to a rover

    Attributes
    ----------
    rover: Rover
        The rover instance to which the movement commands will be applied to 

    Methods
    -------
    apply_movement(commands: str)
        Applies the movement commands to the rover's starting position
    """

    def __init__(self, rover):
        """
        Initialises the MovementProcessor with an instance of a rover

        Parameters
        ----------
        rover: Rover
            The rover instance the commands are to be applied to
        """

        self.rover = rover

    def process_commands(self, commands):
        """
        Processes a string of movement commands to a rover

        Parameters
        ----------
        commands: str
            A string containing the movement commands ('L', 'R' or 'M')

        """

        for command in commands:
            if command == 'L':
                self.rover.turn_left()
            elif command == 'R':
                self.rover.turn_right()
            elif command == 'M':
                self.rover.move()
