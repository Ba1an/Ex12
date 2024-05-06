class Date:
    _months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл',
               8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'}

    def __init__(self, date):
        self._date = self._check_date(date)

    def _check_date(self, date):
        day, month, year = date.split('.')
        if len(day) == 2 and len(month) == 2 and len(year) == 4:
            day, month, year = int(day), int(month), int(year)
            if month in self._months and 1 <= day <= self._days_in_month(month, year):
                return (day, month, year)
        print('ошибка')
        return None

    def _days_in_month(self, month, year):
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

    @property #дискриптор
    def date(self):
        if self._date:
            day, month, year = self._date
            return f'{day} {self._months[month]} {year} г.'
        else:
            return None

    @date.setter
    def date(self, value):
        self._date = self._check_date(value)

    def to_timestamp(self):
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
        if isinstance(other, Date):
            return self._date == other._date
        return False

    def __lt__(self, other):
        if isinstance(other, Date):
            return self.to_timestamp() < other.to_timestamp()
        return False

    def __le__(self, other):
        if isinstance(other, Date):
            return self.to_timestamp() <= other.to_timestamp()
        return False

    def __gt__(self, other):
        if isinstance(other, Date):
            return self.to_timestamp() > other.to_timestamp()
        return False

    def __ge__(self, other):
        if isinstance(other, Date):
            return self.to_timestamp() >= other.to_timestamp()
        return False

    def __str__(self):
        if self._date:
            day, month, year = self._date
            return f'{day}.{month}.{year}'
        else:
            return 'Nonе'



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

