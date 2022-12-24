def get_formated_text(text):
    """
    Форматирует строки из файла по примеру: 'номер'. 'строка', в формате HTML.

    :return: отфарматированные строки.
    """
    list_of_lines = text.strip('\n').split()
    number = 1
    formated_text = ''
    for line in list_of_lines:
        formated_text += f'<p>{number}. {line}<p>'
        number += 1
    return formated_text
