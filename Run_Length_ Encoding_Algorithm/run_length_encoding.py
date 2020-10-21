# Run length enconding Algorithm
# Author: Jaime Fanjul García
# Date: 18/10/2020
def run_length_enconder(string):

    """Print a string of alphanum characters with the encoded result.

    Parameters
    ----------
    string: str
        String of characters. It can only contain alphabet characters.

    The program is capable of detecting numeric characters and warning
    that the string passed as argument cannot contain numeric characters

    """

    if not isinstance(string, str):
        raise TypeError(f" {string} is not a string type")

    result=[]
    counter = 0
    ref = ""

    for c in string:

        if c.isnumeric():
            raise ValueError(f" {string} cannot contain numeric characters")

        elif counter == 0 and ref != c:
            ref = c
            counter = 1
        elif ref == c:
            counter += 1
        else:
            result.append(str(counter)), result.append(ref)
            ref = c
            counter = 1

    result.append(str(counter)), result.append(ref)

    print(f"Encoded result: {''.join(result)}")


if __name__ == "__main__":

    run_length_enconder("aaaaaajjjjjbbbbccccddddyyterooyyeeu")
