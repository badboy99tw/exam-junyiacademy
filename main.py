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


# Q2
def count_numbers(end_number):
    """
    請寫一個程式，Input 是一個數字，Output 是從 1 到這個數字，
    扣除掉所有 3 的倍數以及 5 的倍數，但是需要保留同時是 3 和 5 的倍數的總數字數。

    >>> count_numbers(15)
    9
    """

    def is_matched(n):
        if n % 15 == 0:
            return True
        elif n % 3 == 0:
            return False
        elif n % 5 == 0:
            return False
        return True

    numbers_matched = filter(is_matched, range(1, end_number + 1))
    return sum(1 for _ in numbers_matched)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
