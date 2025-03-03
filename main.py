from Plateau import Plateau
from Rover import Rover
from MovementProcessor import MovementProcessor
import Validations

def initialise_plateau():
    """"
    Prompt the user for plateau dimensions until a valid input is given
    """
    while True:
        # Get input for top-right plateau coordinates
        plateau_dimensions = input("Please enter the coordinates of the upper right corner of the plateau (e.g 5 5)")
        try:
            #Initialise plataeu object
            plateau = Plateau()
            # Set Plateau attributes with setters if validation passes
            plateau.width, plateau.height = Validations.validate_plateau_input(plateau_dimensions)
            return plateau
        except ValueError as error:
            print(f"Invalid plateau dimensions: {error}. Please try again")

def initialise_rover(plateau, rover_id):
    """
    Prompt the user for a valid start position until a valid input is given
    """
    while True:
        start_position = input(f"Please enter the start position for Rover {rover_id} (e.g. 1 2 N)")
        try:
            # Validate input
            start_x_position, start_y_position, start_heading = Validations.validate_rover_start_input(start_position)
            # If start position is within bounds
            if(Plateau.is_within_plateau(plateau, start_x_position, start_y_position)):
                # Initialise rover objext
                rover = Rover()
                # Set attribute values in rover object
                rover.x_position, rover.y_position, rover.heading, rover.plateau = start_x_position, start_y_position, start_heading, plateau
                return rover
            else: 
                print(f"Start position for Rover {rover_id} is outside bounds. Please try again")
            
        # If validation fails
        except ValueError as error:
            print(f"Invalid start position for Rover {rover_id}: {error}. Please try again")
            
def process_rover_movements(rover, rover_id):
    """
    Prompt the user for movement commands, if valid apply to given rover
    """
    while True:
        movements = input(f"Please enter the movement commands for Rover {rover_id} (e.g. LMLMLMLMM)")
        try:
            # Validate input
            movements = Validations.validate_movement_commands_input(movements)
            # Initialise Movement Processor, passing the rover instance
            movements_processor = MovementProcessor(rover)
            # Apply the comments to the rover
            movements_processor.process_commands(movements)
            return
        except ValueError as error:
            print(f"Invalid movement commands: {error}. Please try again")


def main():
    plateau = initialise_plateau()

    rover1 = initialise_rover(plateau, 1)
    process_rover_movements(rover1, 1)

    rover2 = initialise_rover(plateau, 2)
    process_rover_movements(rover2, 2)

    # Print rover1 end position
    print(f"{rover1.x_position} {rover1.y_position} {rover1.heading}")
    # Print rover2 end position
    print(f"{rover2.x_position} {rover2.y_position} {rover2.heading}")

if __name__ == "__main__":
    main()