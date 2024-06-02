def gen_secs():
    """
    Generator function that yields seconds from 0 to 59.

    :return: Yields seconds from 0 to 59.
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generator function that yields minutes from 0 to 59.

    :return: Yields minutes from 0 to 59.
    """
    for minute in range(60):
        yield minute


def gen_hours():
    """
    Generator function that yields hours from 0 to 23.

    :return: Yields hours from 0 to 23.
    """
    for hour in range(24):
        yield hour


def gen_time():
    """
    Generator function that yields time in HH:MM:SS format for every second of a day.

    :return: Yields time strings in HH:MM:SS format.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    """
    Generator function that yields years starting from a given year.

    :param start: The starting year, defaults to 2019.
    :return: Yields years starting from the given start year.
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
    Generator function that yields months from 1 to 12.

    :return: Yields months from 1 to 12.
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generator function that yields days for a given month, considering leap years for February.

    :param month: The month for which to generate days.
    :param leap_year: Boolean indicating if it is a leap year, defaults to True.
    :return: Yields days for the given month.
    """
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            # Months with 31 days
            for day in range(1, 32):
                yield day
        case 4 | 6 | 9 | 11:
            # Months with 30 days
            for day in range(1, 31):
                yield day
        case 2:
            if leap_year:
                # February in a leap year
                for day in range(1, 30):
                    yield day
            else:
                # February in a non-leap year
                for day in range(1, 29):
                    yield day


def gen_date():
    """
    Generator function that yields date and time in DD/MM/YYYY HH:MM:SS format starting from 01/01/2019.

    :return: Yields date and time strings in DD/MM/YYYY HH:MM:SS format.
    """
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d " % (day, month, year) + time


def main():
    """
    Main function to print the next date and time every million iterations.

    :return: None
    """
    date_gen = gen_date()  # Create a generator for dates
    next(date_gen)  # Initialize the generator
    while True:
        for _ in range(1, 1000000):
            next(date_gen)  # Advance the generator a million steps
        print(next(date_gen))  # Print the current date and time


if __name__ == "__main__":
    main()
