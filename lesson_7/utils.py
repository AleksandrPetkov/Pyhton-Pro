def convert_data(data_str):
    """Вычисляет средний рост и вес из списка значений.

    :param data_str: строка с исходными данными по весу, росту и индексу.
    :return: текст со средним значением веса и роста.
    """
    data_list = data_str.replace('\n', ',').split(',')[3:-2]
    total_students = len(data_list) / 3
    total_height = sum([float(data_list[idx]) for idx in range(1, len(data_list), 3) if data_list[idx]]) * 2.54
    total_weight = sum([float(data_list[idx]) for idx in range(2, len(data_list), 3) if data_list[idx]]) * 0.453592
    avr_height = round(total_height / total_students, 2)
    avr_weight = round(total_weight / total_students, 2)
    return f'Average height is {avr_height} cm, Average weight is {avr_weight} kg'
