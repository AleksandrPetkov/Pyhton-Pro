class DigitalCounter:
    """
    Класс описывающий счетчик.

    Aтрибуты:
    start - начальное значение счетчика(дефолтное значение 0).
    end - конечное значение счетчика(дефолтное значение 100).
    current - текущее значение счетчика(дефолтное значение None).

    Методы:
    __init__ - иницализирует класс.
    increase - увеличивает счетчик на 1.
    get_current_value - возвращает текущее значение функции.
    """

    def __init__(self, start=0, end=100, current=None):
        """
        Инициализирует класс DigitalCounter.

        :param start: начальное значение счетчика(дефолтное значение 0).
        :param end: конечное значение счетчика(дефолтное значение 100).
        :param current: текущее значение счетчика(дефолтное значение None).
        """
        self.start = start
        self.end = end
        self.current = current

    def increase(self):
        """
        Метод увеличивает текущее значение счетчика на 1.

        При достижении верхней границы счетчика, вызывается ошибка.
        """
        if self.current is None:
            self.current = self.start
            self.current += 1
        elif self.current < self.end:
            self.current += 1
        else:
            raise Exception(f'Достигнуто максимальное значение счетчика "{self.end}".')

    def get_current_value(self):
        """Возвращает текущее значение счетчика."""
        return self.current
