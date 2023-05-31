import datetime


def get_month_name(months, days):
    # создаем начальную дату (1 января 2010 года)
    start_date = datetime.date(2010, 1, 1)

    # добавляем нужное количество месяцев и дней
    new_date = start_date + datetime.timedelta(days=days, weeks=0,
                                               months=months, years=0)

    # возвращаем название месяца
    return new_date.strftime("%B")