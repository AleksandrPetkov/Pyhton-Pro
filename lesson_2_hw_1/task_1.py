import os
import sqlite3
from collections import Counter
from typing import List, Dict


def execute_query(query_sql: str) -> List:
    """
    Функция для выполнения запроса.

    :param query_sql: запрос
    :return: результат выполнения запроса
    """
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def get_repeat_names() -> Dict:
    """
    Функция для вывода результата выполнения запроса.

    :return: результат выполнения запроса в виде словаря
    (ключ - имя, значение - кол-во повторений)
    """
    query_sql = '''
        SELECT FirstName
          FROM customers
    '''
    names = execute_query(query_sql)
    repeat_names = {}
    for name, count in Counter(names).items():
        if count > 1:
            repeat_names[name[0]] = count
    return repeat_names
