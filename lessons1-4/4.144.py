def get_previous_and_next_date(day, month):
    # определяем количество дней в каждом месяце
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # определяем предыдущий день
    prev_day = day - 1
    prev_month = month
    if prev_day == 0:
        prev_month -= 1
        prev_day = days_in_month[prev_month]

    # определяем следующий день
    next_day = day + 1
    next_month = month
    if next_day > days_in_month[month]:
        next_month += 1
        next_day = 1

    return (prev_day, prev_month), (next_day, next_month)