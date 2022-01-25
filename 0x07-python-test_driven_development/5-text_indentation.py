#!/usr/bin/python3

"""module that prints a text with 2 lines after
  special characters ?, . or :"""


def text_indentation(text):

    """ prints text
      Arguments:
            text: a string to be printed
    """
    """a flag is activated when one of the special
    characters is displayed
    """

    new_line = 0

    """ the function strip is used to remove leading
    and trailing white space from the original text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = text.strip()

    for word in new_text:
        if word == "?" or word == "." or word == ":":
            new_line = 1
            print(word)
            print()
        else:
            if new_line == 1:
                if word == " ":
                    continue
                else:
                    new_line = 0

            print(word, end="")
