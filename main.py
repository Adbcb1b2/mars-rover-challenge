from Plateau import Plateau
from Rover import Rover
import Validations

#Entry point of the program
def main():
    # Get input for plateau coordinates
    plateau_dimensions = input("Please enter the coordinates of the upper right corner of the plateau (e.g 5 5)")
    try:
        #Initialise plataeu object
        plateau = Plateau()
        # Set Plateau attributes
        plateau.width, plateau.height = Validations.validate_plateau_input(plateau_dimensions)
    except ValueError as error:
        print(f"Invalid plateau dimensions: {error}")


    # Attempt to set plataeu coordinates in Plateau class
    # Get input for rover1 start position e.g. 1 2 N
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