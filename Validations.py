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
    



