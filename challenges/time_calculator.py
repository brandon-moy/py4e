def add_time(start, duration, dayofweek=''):
    days = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]

    def period_split(time):
        return time.split()

    def time_split(time):
        hour_min_split = []
        for i in time.split(':'):
          hour_min_split.append(int(i))
        return hour_min_split

    period_switch = {'AM': 'PM', 'PM': 'AM'}

    time = period_split(start)[0]
    init_period = period_split(start)[1]
    init_hours = time_split(time)[0]
    minutes = time_split(time)[1]
    add_hours = time_split(duration)[0]
    add_minutes = time_split(duration)[1]

    hours = init_hours + add_hours
    minutes += add_minutes
    days_later = 0
    day_now, day_later, new_period = [''] * 3

    if minutes >= 59:
        hours += (minutes // 60)
        minutes %= 60

    if hours >= 24:
        days_later += hours // 24
        hours %= 24

    if (init_hours <= 11) and (hours > 11):
        new_period = period_switch[init_period]
        if (init_period, new_period) == ('PM', 'AM'):
            days_later += 1

        if hours > 12:
            hours %= 12

    if dayofweek:
        dayofweek_idx = (days.index(dayofweek.lower()) + days_later) % len(days)
        day_now = f", {days[dayofweek_idx].title()}"

    if days_later == 1:
        day_later = " (next day)"
    elif days_later > 1:
        day_later = f" ({days_later} days later)"

    new_time = f"{hours}:{str(minutes).rjust(2, '0')} {new_period or init_period}{day_now}{day_later}"

    return new_time
