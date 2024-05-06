class AirTicket:
    def __init__(self, info):
        self.passenger_name = info[0]
        self._from = info[1]
        self.to = info[2]
        self.date_time = info[3]
        self.flight = info[4]
        self.seat = info[5]
        self._class = info[6]
        self.gate = info[7]

    def __str__(self):
        return f'|{self.passenger_name.center(16)}|{self._from.center(4)}|{self.to.center(3)}|{self.date_time.center(16)}|{self.flight.center(20)}|{self.seat.center(4)}|{self._class.center(3)}|{self.gate.center(4)}|'

class Load():
    data = []
    def write(self, filename):
        with open(filename, 'r') as f_in:
            lines = f_in.readlines()
            for line in lines[1:]:
                info = line.strip().split(';')
                ticket = AirTicket(info)
                Load.data.append(ticket)


tickets = Load()
tickets.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)