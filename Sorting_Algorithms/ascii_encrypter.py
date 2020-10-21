# ASCII Text Encrypter.
#--------
# Given a text with several words, encrypt the message in the following way:
# The first letter of each word must be replaced by its ASCII code.
# The second letter and the last letter of each word must be interchanged.
#--------
# Author: Jaime Fanjul García
# Date: 16/10/2020

def text_encrypter(text):

    """Return a string encrypted.

    Parameters
    ----------
    text: str
        String of characters. It can contain any type of characters

    This script generate a new string encripted which:
    The first letter of each word must be replaced by its ASCII code.
    The second letter and the last letter of each word must be interchanged..
    """
    if not isinstance(text, str):
        raise TypeError(f" {text} is not a string type")

    words = text.split(" ")

    for i , word in enumerate(words):
        ch = list(word)
        if len(ch) == 1:
            ch[0] = str(ord(word[0]))
        else:
            ch[0] = str(ord(word[0]))
            ch[1] = word[-1]
            ch[-1]= word[1]

        words[i] = ''.join(ch)

    text = ' '.join(words)

    return text


if __name__ == "__main__":

    encrypted_text = text_encrypter("To be or not to be that is the question")
    print(encrypted_text)
