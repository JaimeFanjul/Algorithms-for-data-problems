# Anagram Detection Algorithm
# Author: Jaime Fanjul García
# Date: 16/10/2020

def anagram_detector(word1,word2):

    """Print the result of the anagram detectition,
indicating if the words are anagrams or not.

    Parameters
    ----------
    word1: str
        String of characters. It can not contain numeric characters.

    word2: str
        String of characters. It can not contain numeric characters.


        The program is capable of detecting numeric characters and warning
        that the words passed as arguments cannot contain these characters

    """
    chars = set(word1)
    count_str1 = []
    count_str2 = []
    check = [(True,"")]


    if not isinstance(word1,str) or not isinstance(word2,str):
        check[0]= (False,"Arguments must be strings")
    else:
        for c in word1 + word2:
            if c.isnumeric():
                check[0] = (False,"Arguments can NOT contain numeric characters")
                break

    if check[0][0] == True:
        if chars == set(word2):
            for c in chars:
                count_str1.append(word1.count(c))
                count_str2.append(word2.count(c))
            if count_str1 == count_str2:
                    print(f" The words {word1,word2} --> ARE Anagrams ")
            else:
                    print(f" The words {word1,word2} --> ARE NOT Anagrams")
        else:
            print(f" The words {word1,word2} --> ARE NOT Anagrams")
    else:
        print(check[0][1])

if __name__ == "__main__":

    anagram_detector("mora","roma")
