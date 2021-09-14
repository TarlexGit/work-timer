from datetime import date, datetime,time,timedelta

def calculate(h: int, m:int):
    dt = datetime.combine(date.today(), time(h, m)) + timedelta(hours=8, minutes=30)
    return dt

def get_end_time(hours, minutes):
    time_to_exit = calculate(int(hours), int(minutes)).strftime('%H:%M:%S')
    return 'End working time to {}'.format(time_to_exit)

if __name__ == '__main__':
    get_end_time()