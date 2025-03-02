def validate_plateau_input(user_input):
    """
    Validates input consists of two integers spearated by a space

    Parameters
    ----------
    input: str
        The input provided by the user, expected to be a string containing two integers separated by a space

    Returns
    ------
    tuple of (int, int)
        A tuple containing the two integrs extracted from the input

    Raises
    ------
    ValueError
        If the input doesn't contain 2 integers or the 2 values aren't integers

    """

    # Remove trailing whitespace
    user_input = user_input.strip()

    # If input is correct, this line should split it into a list of two parts
    input_split = user_input.split()

    # Check if the split contains 2 parts, raise error if not
    if len(input_split) != 2:
        raise ValueError("Input must contain two integers separated by a space")
    
    # Attempt to convert the split input values to integers
    try:
        width = int(input_split[0])
        height = int(input_split[1])
    except ValueError:
        raise ValueError("Both values must be an integer")
    
    # Return values if they are validated
    return width, height
    
def validate_rover_start_input(user_input):
    """
    Validates input consists of an 2 integers and a valid heading

    Parameters
    ----------
    user_input: str
        The input provided by the user, expected to be in x y H

    Returns
    -------
    tuple of (int, int, str)
        A tuple containing the x, y and heading extracted from the input

    Raises
    ------
    ValueError
        if the input doesn't contain 3 parts, or if the values are incorrect
    """
    # Removed trailing white space
    user_input = user_input.strip()

    # If the user input is correct, this line should split it into a list of 3 parts
    input_split = user_input.split()

    if len(input_split) != 3:
        raise ValueError("Input must contain 2 integers and the letter 'N', 'E', 'S' or 'W' separated by a space")
    
    try:
        x_position = int(input_split[0])
        y_position = int(input_split[1])
    except ValueError:
        raise ValueError("The first 2 values must be an integer")
    
    heading = input_split[2].upper()
    if heading not in('N', 'E', 'S', 'W'):
        raise ValueError("Heading must be one of the following: 'N', 'E', 'S', 'W'")

    return x_position, y_position, heading

