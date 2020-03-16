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


# Q3
"""
3.房間裡有三個袋子，一個只裝鉛筆，一個只裝原子筆,第三個有鉛筆也有原子筆，袋子是不透明的，單從
袋子的外表上看不出任何差異，你不知道哪一個袋子裝了什麼。除了袋子上各貼了一個標示("鉛筆"、"原子
筆"、"混和")，而且標示都是錯的(ex. 標有鉛筆的袋子一定不是只裝鉛筆)。
你只能選一個袋子，然後拿出裡面一支筆看是鉛筆還是原子筆，然後你要推論出這三個袋子分別的情況。請
列出您的作法,以及解釋為什麼這樣可以找到答案。

A:
1. 先從貼"混和"的袋子拿出一枝筆
2. 如果那枝筆是鉛筆，代表貼"混合"的袋子其實是鉛筆（因為這袋不是鉛筆就是原子筆）
3. 因為混合袋是鉛筆，代表貼"原子筆"的袋子一定是混合（因為只能是混合或鉛筆，但已經不可能是鉛筆）
4. 最後，貼"鉛筆"的袋子就一定是原子筆

如果最開始從"混和"的袋子拿出來的是原子筆，那也是用同樣方法推論。
"""

# Q4
"""
4.有三個人一起到迪士尼遊玩,中午肚子餓了,去餐廳點了一份現在最夯的冰雪奇緣雙人組,要價 900 元,
付錢後,服務生發現今天套餐大特價,只要 750 元,因此服務生應該退還 150 元給這三個人,但是這位服務
生一時鬼迷心翹,決定按扛 60 元,只退了 90 元給這三個遊客。
那麼: 三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元 270元 × 3人 + 服務生私吞的 60 元
= 810 + 60 = 870 !? 怎麼不是 900 元呢?還有 30元去哪了呢? 請用敘述的方式,儘量清楚解釋問題出在哪
裡。

A:
這個等式列錯了，應該是這樣
三個人最後共出 810 元 == 服務生私吞 60 元 + 迪士尼收了 750 元
810 = 60 + 750

所以 810 + 60 邏輯上沒道理
不是三個人和服務生付錢給迪士尼
而是三個人付錢給服務生（私吞）和迪士尼
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
