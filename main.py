from Plateau import Plateau
from Rover import Rover
from MovementProcessor import MovementProcessor
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
    start_position_1 = input("Please enter the start position for Rover 1 (e.g. 1 2 W)")
    # If validation passes
    try:
        # Set start position if validation passes
        start_x_position, start_y_position, start_heading = Validations.validate_rover_start_input(start_position_1)
        # Check start position is within the plateau bounds
        if(Plateau.is_within_plateau(plateau, start_x_position, start_y_position)):
            # Initialise first rover objext
            rover1 = Rover()
            rover1.x_position, rover1.y_position, rover1.heading, rover1.plateau = start_x_position, start_y_position, start_heading, plateau
        else: 
            raise ValueError("Start position is not within plateau bounds")
            
    # If validation fails
    except ValueError as error:
        print(f"Invalid start position: {error}")
        return
    
    # Get input for rover1 movements
    movements_rover1 = input("Please enter the movement commands for Rover 1 (e.g. LMLMLMLMM)")
    # If validation passes
    try:
        # Validate input string
        movements_rover1 = Validations.validate_movement_commands_input(movements_rover1)
        # Apply movement
        # Initialise a movements proccessor
        movements_processer1 = MovementProcessor(rover1)
        # Use the Movement Processor to process the commands
        movements_processer1.process_commands(movements_rover1)

        
    except ValueError as error:
        print(f"Invalid movement commands for Rover 1: {error}")
        return

    # Get input for rover2 start position e.g. 1 2 N
    start_position_2 = input("Please enter the start position for Rover 2 (e.g. 1 2 W)")
    
    # If validation passes
    try:
        # Set start position if validation passes
        start_x_position, start_y_position, start_heading = Validations.validate_rover_start_input(start_position_2)
        # Check start position is within the plateau bounds
        if(Plateau.is_within_plateau(plateau, start_x_position, start_y_position)):
            # Initialise first rover objext
            rover2 = Rover()
            rover2.x_position, rover2.y_position, rover2.heading, rover2.plateau = start_x_position, start_y_position, start_heading, plateau
        else: 
            raise ValueError("Start position is not within plateau bounds")
            
    # If validation fails
    except ValueError as error:
        print(f"Invalid start position: {error}")
        return

    # Get input for rover2 movements
    movements_rover2 = input("Please enter the movement commands for Rover 2 (e.g. LMLMLMLMM)")
    # If validation passes
    try:
        # Validate input string
        movements_rover2 = Validations.validate_movement_commands_input(movements_rover2)
        # Apply movement
        # Initialise a movements proccessor
        movements_processer2 = MovementProcessor(rover2)
        # Use the Movement Processor to process the commands
        movements_processer2.process_commands(movements_rover2)
    except ValueError as error:
        print(f"Invalid movement commands for Rover 2: {error}")
        return

    # Print rover1 end position
    print(f"{rover1.x_position} {rover1.y_position} {rover1.heading}")
    # Print rover2 end position
    print(f"{rover2.x_position} {rover2.y_position} {rover2.heading}")


if __name__ == "__main__":
    main()