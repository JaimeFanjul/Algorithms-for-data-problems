# Counts the number of duplicate characters in a character string.
# Note: there are no differences between upper and lower case.
# Author: Jaime Fanjul García
# Date: 5/10/2020

# 2 methods
# The first method is the most efficient and is case-sensitive.

from collections import Counter

def duplicate_sum_1(text):

    """Return a int with the sum of duplicate characters in a String.

    Use of collections library

    Parameters
    ----------
    text: str
        String of characters.
    """
    if not isinstance(text, str):
        raise TypeError(f" {text} is not a string type")

    return sum(v > 1 for v in Counter(text).values())

def duplicate_sum_2(text):

    """Return a int with the sum of duplicate characters in a String.

    Parameters
    ----------
    text: str
        String of characters.
    """
    if not isinstance(text, str):
        raise TypeError(f" {text} is not a string type")

    text_lower= text.lower()
    ch = set(text_lower)

    counter = 0

    for c in ch:
        if text_lower.count(c) > 1:
            counter += 1

    return counter


if __name__ == "__main__":

    text = " AAaabbbbBBDDffftryueeieigeeriyrinAASSG"
    print(duplicate_sum_1(text))
    print(duplicate_sum_2(text))
