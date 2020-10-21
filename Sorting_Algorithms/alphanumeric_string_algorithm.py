# Only alphanumeric characters string Algorithm
# Author: Jaime Fanjul García
# Date: 19/10/2020

def alphanum_string(text):

    """Return a string with only alphanumeric characters.

    Parameters
    ----------
    text: str
        String of characters to be clean.

    This script generate a new string that contains only alphanumeric characters from another string with any type of characters.

    """
    if not isinstance(text, str):
        raise TypeError(f" {text} is not a string type")

    return "".join(c for c in text if c.isalnum())


if __name__ == "__main__":

    alphanum = alphanum_string("hello//((.)(.))//&w@or-l.d")
    print(alphanum)
