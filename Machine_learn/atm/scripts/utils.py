import datetime

FUTURE_HOLIDAYS = {datetime.date(2005, 12, 31): 7,}
FUTURE_HOLIDAYS_DAYS = 7


def read_data():
    """
    :return: iterable of point-date-money *tuple*s
    """
    with open('data.csv', mode='r') as f:
        for line in f.readlines()[1:]:
            point, date, value = line.split(',')
            date = datetime.datetime.strptime(date.strip('"'), '%d.%m.%Y').date()
            yield (int(point.strip('"')), date, int(value.strip('"\n')))