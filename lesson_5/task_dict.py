import re
from collections import Counter


def get_repeated_word(string):
    """
    Функция для вывода наиболее повторяющегося слова в строке.

    :return: возвращает самое повторяемое слово,
             если слов несколько, возвращает последнее.
    """
    words = re.findall(r'\w+', string)
    repeat_dict = Counter(words)
    max_val = max(repeat_dict.values())
    final_dict = {k: v for k, v in repeat_dict.items() if v == max_val}
    if len(final_dict) > 1:
        return list(final_dict.keys())[-1]
    return list(final_dict.keys())[0]
