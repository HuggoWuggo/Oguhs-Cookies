class ColourNotFoundError(Exception):
    """Raised if the specified colour cannot be found"""

class EmphasisNotFoundError(Exception):
    """Raised if the specified emphasis cannot be found"""

def __get_colour(colour):
    """Function for returning the corresponding colour escape character"""

    match colour.lower():
        case 'red':
            return '\033[31m'
        case 'green':
            return '\033[32m'
        case 'yellow':
            return '\033[33m'
        case 'blue':
            return '\033[34m'
        case 'magenta' | 'purple':
            return '\033[35m'
        case 'cyan':
            return '\033[36m'
        case 'dark red':
            return '\033[91m'
        case 'dark green':
            return '\033[92m'
        case 'dark yellow':
            return '\033[93m'
        case 'dark blue':
            return '\033[94m'
        case 'dark magenta' | 'dark purple':
            return '\033[95m'
        case 'dark cyan':
            return '\033[96m'
        case 'light red':
            return '\033[1;31m'
        case 'light green':
            return '\033[1;32m'
        case 'light yellow':
            return '\033[1;33m'
        case 'light blue':
            return '\033[1;34m'
        case 'light magenta' | 'light purple':
            return '\033[1;35m'
        case 'light cyan':
            return '\033[1;36m'
        case 'gray' | 'grey':
            return '\033[37m'
        case 'dark grey' | 'dark gray':
            return '\033[30m'
        case 'black':
            return '\033[1;30m'
        case 'white':
            return '\033[97m'
        case 'endc':
            return '\033[0m'
        case _:
            raise ColourNotFoundError(f"The colour '{colour}' could not be found")

def __get_emphasis(emphasis: tuple) -> str:
    """Function for returning the corresponding emphasis escape character"""

    options = ''
    for option in emphasis:
        match option:
            case 'bold':
                options += '\033[1m'
            case 'italics':
                options += '\033[3m'
            case 'underline':
                options += '\033[4m'
            case _:
                raise EmphasisNotFoundError(f"The emphasis '{option}' could not be found")
    return options

def pycolour(colour: str, text: str, *emphasis) -> None:
    """
    A function that prints text to the console with the specified colour
    and emphasis

    :param colour: The colour the text will be printed in
    :param text: The text that will be printed
    :param emphasis: The optional emphasis that the text will be printed with
    """

    print(f'{__get_emphasis(emphasis)}{__get_colour(colour)}{text}{__get_colour("endc")}') if emphasis else print(f'{__get_colour(colour)}{text}{__get_colour("endc")}')