class Date:
    """
    Represents a Date object.

    Attributes
    ----------
    - _date: tuple, Stores the day, month, and year of the date.

    Class attributes
    ----------
    - _months: dictionary, Stores the str names for each month.

    Methods
    -------
    - __init__(date): Initializes the Date object with the given date string.
    - _check_date(date): Validates the input date string.
    - _days_in_month(month, year): Returns the number of days in the given month and year.
    - date: property, Returns a formatted string of the date.
    - date.setter: Sets a new date for the Date object.
    - to_timestamp(): Converts the Date object to a UNIX timestamp.
    - __eq__(other): Checks if two Date objects are equal.
    - __lt__(other): Checks if the Date object is less than the other Date object.
    - __le__(other): Checks if the Date object is less than or equal to the other Date object.
    - __gt__(other): Checks if the Date object is greater than the other Date object.
    - __ge__(other): Checks if the Date object is greater than or equal to the other Date object.
    - __str__(): Returns a string representation of the Date object.
    """
    _months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл',
               8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'}

    def __init__(self, date):
        """
        Initializes the Date object with the given date string.
        :param date: tuple, Stores the day, month, and year of the date.
        """
        self._date = self._check_date(date)

    def _check_date(self, date):
        """
        Validates the input date string.
        :param date: tuple, Stores the day, month, and year of the date.
        :return: tuple, Stores the day, month, and year of the date or None.
        """
        day, month, year = date.split('.')
        if len(day) == 2 and len(month) == 2 and len(year) == 4:
            day, month, year = int(day), int(month), int(year)
            if month in self._months and 1 <= day <= self._days_in_month(month, year):
                return (day, month, year)
        print('ошибка')
        return None

    def _days_in_month(self, month, year):
        """
        Returns the number of days in the given month and year.
        :return: umber of days in each month
        """
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return None

    @property  # дискриптор
    def date(self):
        """
        Returns a formatted string of the date.
        :return: anouther form of given date
        """
        if self._date:
            day, month, year = self._date
            return f'{day} {self._months[month]} {year} г.'
        else:
            return None

    @date.setter
    def date(self, value):
        """
        Sets a new date for the Date object.
        :param value: New date
        """
        self._date = self._check_date(value)

    def to_timestamp(self):
        """
        Converts the Date object to a UNIX timestamp.
        :return: Number of seconds
        """
        days = 0
        day, month, year = list(self._date)
        for year in range(1970, year):
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days += 366
            else:
                days += 365
        for month in range(1, month):
            days += self._days_in_month(month, year)
        days += day - 1
        return days * 86400

    def __eq__(self, other):
        """
        Checks if two Date objects are equal.
        :param other: The Date object to compare with.
        :return: True if the Date objects are equal, False otherwise.
        """
        if isinstance(other, Date):
            return self._date == other._date
        return False

    def __lt__(self, other):
        """
        Checks if the Date object is less than the other Date object.
        :param other: The Date object to compare with.
        :return: True if the Date object id bigger, False otherwise.
        """
        if isinstance(other, Date):
            return self.to_timestamp() < other.to_timestamp()
        return False

    def __le__(self, other):
        """
        Checks if the Date object is less than or equal to the other Date object.
        :param other: The Date object to compare with.
        :return: True if one Date object is bigger or equal, False otherwise.
        """
        if isinstance(other, Date):
            return self.to_timestamp() <= other.to_timestamp()
        return False

    def __gt__(self, other):
        """
        Checks if the Date object is greater than the other Date object.
        :param other: The Date object to compare with.
        :return: True if one Date object is smaller, False otherwise.
        """
        if isinstance(other, Date):
            return self.to_timestamp() > other.to_timestamp()
        return False

    def __ge__(self, other):
        """
        Checks if the Date object is greater than or equal to the other Date object.
        :param other: The Date object to compare with.
        :return: True if one Date object is smaller or equal, False otherwise.
        """
        if isinstance(other, Date):
            return self.to_timestamp() >= other.to_timestamp()
        return False

    def __str__(self):
        if self._date:
            day, month, year = self._date
            return f'{day}.{month}.{year}'
        else:
            return 'Nonе'

    def __repr__(self):
        return self.__str__()


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
