class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title, employees=[]):
        self.id = id
        self.date = date
        self.title = title
        self.employees = employees

    def add_person(self, person):
        self.employees.append(person)
        return self.employees

    def count(self):
        return len(self.employees)

    @classmethod
    def count_meeting(cls, date):
        k = 0
        xday, xmonth, xyear = date.split('.')
        for item in Meeting.lst_meeting:
            yday, ymonth, yyear = item.split('.')
            if int(xyear) < int(yyear):
                return k
            elif int(xyear) == int(yyear) and int(xmonth) < int(ymonth):
                return k
            elif int(xyear) == int(yyear) and int(xmonth) == int(ymonth) and int(xday) < int(yday):
                return k
            k += 1

    def total(self):
        return len(Meeting.lst_meeting)


class Load:

    def write(self, file1, file2, file3):
        with open(file1, 'r') as f_in:
            info_person = []
            for line in f_in:
                info_person.append(line.strip().split(';'))
        with open(file2, 'r') as f_2:
            info_meeting = []
            for line in f_2:
                info_meeting.append(line.strip().split(';'))
        with open(file3, 'r') as f_3:
            info_per_meet = []
            for line in f_3:
                info_per_meet.append(line.strip().split(';'))
        return info_person, info_meeting, info_per_meet





Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))