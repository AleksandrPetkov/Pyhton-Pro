def get_repeated_word(string):
    """
    Функция для вывода наиболее повторяющегося слова в строке.

    :return: возвращает самое повторяемое слово,
             если слов несколько, возвращает последнее.
    """
    new_string = ''
    punctuation = '''!()-[]{};?@#$%:'"\,./^&;*_,'''
    for char in string:
        if char in punctuation:
            new_string += ''
        else:
            new_string += char
    split_new_string = new_string.lower().split()
    repeat_dict = {k: split_new_string.count(k) for k in split_new_string}
    max_val = max(repeat_dict.values())
    final_dict = {k: v for k, v in repeat_dict.items() if v == max_val}
    if len(final_dict) > 1:
        return list(final_dict.keys())[-1]
    return list(final_dict.keys())[0]
