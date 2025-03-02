from Plateau import Plateau
from Rover import Rover
import Validations

#Entry point of the program
def main():
    # Get input for plateau coordinates
    plateau_dimensions = input("Please enter the coordinates of the upper right corner of the plateau (e.g 5 5)")
    # If validation passes
    try:
        #Initialise plataeu object
        plateau = Plateau()
        # Set Plateau attributes with setters if validation passes
        plateau.width, plateau.height = Validations.validate_plateau_input(plateau_dimensions)
    # If validation fails
    except ValueError as error:
        print(f"Invalid plateau dimensions: {error}")
        return

    # Get input for rover1 start position e.g. 1 2 N
    start_position_1 = input("Please enter the start position for the first rover (e.g. 1 2 W)")
    # If validation passes
    try:
        # Set start position if validation passes
        start_x_position, start_y_position, start_heading = Validations.validate_rover_start_input(start_position_1)
        # Check start position is within the plateau bounds
        if(Plateau.is_within_plateau(plateau, start_x_position, start_y_position)):
            # Initialise first rover objext
            rover1 = Rover()
            rover1.x_position, rover1.y_position, heading = start_x_position, start_y_position, start_heading
        else: 
            raise ValueError("Start position is not within plateau bounds")
            
    # If validation fails
    except ValueError as error:
        print(f"Invalid start position: {error}")
        return
    

    # Validate input
    # Append input to a list [x,y,H]
    # Check start position is within bounds of plataeu
    # Create object for rover 1
    # Get input for movement commands
    # Validate movement commands
    # Attempt to process movement commands

    # Get input for rover2 start position e.g. 1 2 N
    # Validate input
    # Append input to a list [x,y,H]
    # Check start position is within bounds of plataeu
    # Create object for rover2
    # Get input for movement commands
    # Validate movement commands
    # Attempt to process movement commands

    # Print rover1 end position
    # Print rover2 end position


    

if __name__ == "__main__":
    main()