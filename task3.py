class Date:
    """
    Represents a Date object.

    Attributes:
    -----------
    _date : Stores the date in the format 'dd.mm.yyyy'.

    Class Attributes:
    ----------------
    _months : Stores the names of each month as strings.

    Methods:
    --------
    __init__(date): Initializes the Date object with the given date string.
    __repr__(): Returns a string representation of the Date object.
    """
    _months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл',
               8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'}

    def __init__(self, date):
        """
        Initializes the Date object with the given date string.
        :param date:
        """
        self._date = date

    def __repr__(self):
        """
        Returns a string representation of the Date object.
        """
        day, month, year = self._date.split('.')
        return f'{day} {self._months[int(month)]} {year} г.'


class User:
    """
    Represents a User object.

    Attributes:
    -----------
    :param id : The ID of the user.
    :param login : The login name of the user.
    :param name : The name of the user.
    :param gender : The gender of the user. None if not provided.

    Methods:
    --------
    __init__(date): Initializes the Date object with the given date string.
    __str__(): Returns a string representation of the User object.
    """

    def __init__(self, info):
        """
        Initializes a User object.
        :param info:  A list containing information about the user.
        """
        self.id = info[0]
        self.login = info[1]
        self.name = info[2]
        if len(info) > 3:
            self.gender = info[5]
        else:
            self.gender = None

    def __str__(self):
        """
        Returns a string representation of the User object.
        """
        if self.gender:
            return f'ID: {self.id} LOGIN: {self.login} NAME: {self.name} GENDER: {self.gender}'
        return f'ID: {self.id} LOGIN: {self.login} NAME: {self.name}'


class Meeting:
    """
    Attributes
    ----------
    - info: A list containing information about the meeting

     Class attributes
    ----------
    - _lst_meeting: list of objects

     Methods
    -------
    - __init__(info): Initializes the Meeting object with the given date string.
    - count_meeting(date): Counts the number of meetings on the given date.
    - total(): Returns the total number of employees attending all meetings.
    - __str__(): Returns a string representation of the Meeting object.
    """
    lst_meeting = []

    def __init__(self, info):
        """
        Initializes a Meeting object.
        :param info: A list containing information about the meeting
        """
        self.id = info[0]
        self.date = Date(info[1])
        self.title = info[2]
        self.employees = []
        Meeting.lst_meeting.append(self)

    @staticmethod
    def count_meeting(date):
        """
        Counts the number of meetings on the given date.
        :param date: The date to count meetings for.
        :return: The number of meetings on the given date.
        """
        count = 0
        for meeting in Meeting.lst_meeting:
            meeting_day, meeting_month, meeting_year = meeting.date._date.split('.')
            day, month, year = date._date.split('.')
            if int(meeting_day) == int(day) and int(meeting_month) == int(month) and int(meeting_year) == int(year):
                count += 1
        return count

    @staticmethod
    def total():
        """
        Returns the total number of employees attending all meetings.
        :return: The total number of employees attending all meetings.
        """
        total_users = []
        for meeting in Meeting.lst_meeting:
            for employee in meeting.employees:
                total_users.append(employee.id)
        return len(total_users)

    def __str__(self):
        """
        Returns a string representation of the Meeting object.
        """
        final = (f'\nРабочая встреча {Meeting.lst_meeting.index(self) + 1}'
                 f'\n{self.date} {self.title}')
        for x in self.employees:
            final += '\n' + User.__str__(x)
        return final


class Load:
    """
    Loads data from files and creates objects.

    Methods:
    --------
    write(meetings_file, persons_file, pers_meetings_file):
    """

    @staticmethod
    def write(meetings_file, persons_file, pers_meetings_file):
        """
        Writes data from files and creates Meeting and User objects.
        :param meetings_file: The filename containing meeting data.
        :param persons_file: The filename containing user data.
        :param pers_meetings_file: The filename containing user-meeting relationship data.
        """
        with open(meetings_file, 'r', encoding='utf-8') as f_meetings:
            for line in f_meetings.readlines()[1:]:
                info = line.strip().split(';')[:-1]
                meeting = Meeting(info)

        with open(persons_file, 'r', encoding='utf-8') as f_persons:
            users = {}
            lines = f_persons.readlines()
            for line in lines[1:]:
                info = line.strip().split(';')
                user = User(info)
                users[user.id] = user

        with open(pers_meetings_file, encoding='utf-8') as f_pers_meetings:
            lines = f_pers_meetings.readlines()[1:]
            for line in lines:
                meeting_id, user_id = line.strip().split(';')[:-1]
                found_meeting = None
                for meeting in Meeting.lst_meeting:
                    if meeting.id == meeting_id:
                        found_meeting = meeting
                        break
                if found_meeting and user_id in users:
                    found_meeting.employees.append(users[user_id])


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
