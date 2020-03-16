# Q1, A
def reverse_word(word):
    """
    請寫一個程式把裡面的字串反過來。

    >>> reverse_word("junyiacademy")
    'ymedacaiynuj'
    """
    return "".join(reversed(word))


# Q1, B
def reverse_sentence(sentence):
    """
    請寫一個程式把裡面的字串,每個單字本身做反轉,但是單字的順序不變。

    >>> reverse_sentence("flipped class room is important")
    'deppilf ssalc moor si tnatropmi'
    """
    reversed_words = [reverse_word(w) for w in sentence.split(" ")]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
