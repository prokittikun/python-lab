
def read_hour():
    return int(input("Enter hour: "))
def read_minute():
    return int(input("Enter minute: "))
def read_second():
    return int(input("Enter second: "))
def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s
def time_elapsed(start, finish):
    x = finish - start
    return f"{x // 3600} hours {x // 60 % 60} minutes {x % 60} seconds."
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)
print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))