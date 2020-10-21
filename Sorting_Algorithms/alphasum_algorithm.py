
# Given a character string replace each space separated word with the sum of their positions in the alphabet.
# Author: Jaime Fanjul García
# Date: 19/10/2020

from string import ascii_letters
alphabet = ascii_letters

def alpha_sum(text):

    """Return a with the sum of all alphabet characters in a string.

    Parameters
    ----------
    text: str
        String of characters.
    """
    if not isinstance(text, str):
        raise TypeError(f" {text} is not a string type")

    w_sum = []

    for w in text.split():
      s=0

      for c in w:
          s += alphabet.index(c) + 1
          w_sum.append(s)

    return sum(w_sum)


if __name__ == "__main__":

    text = " what is the question that we want to answer"
    print(alpha_sum(text))
