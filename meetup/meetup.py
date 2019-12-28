from datetime import date, timedelta
import dateutil.relativedelta as rdelta

def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

def all_weekdays(year, month, week, day_of_week):
    dt = date(year, month, 1)

    if week == 'last':
        clean_week = int(-1)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day_offset = 31
        elif month == 2:
            day_offset = 28
        else:
            day_offset = 30
    else:
        clean_week = +int(week.strip("stndrh"))
        day_offset = 0

    if day_of_week == 'Monday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.MO(clean_week))
        return the_date
    elif day_of_week == 'Tuesday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.TU(clean_week))
        return the_date
    elif day_of_week == 'Wednesday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.WE(clean_week))
        return the_date
    elif day_of_week == 'Thursday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.TH(clean_week))
        return the_date
    elif day_of_week == 'Friday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.FR(clean_week))
        return the_date
    elif day_of_week == 'Saturday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.SA(clean_week))
        return the_date
    elif day_of_week == 'Sunday':
        the_date = dt + rdelta.relativedelta(days=day_offset, weekday=rdelta.SU(clean_week))
        return the_date



def meetup(year, month, week, day_of_week):

    if week == 'teenth':
        start_date = date(year, month, 13)
        end_date = date(year, month, 20)

        for single_date in daterange(start_date, end_date):
            if single_date.strftime("%A") == day_of_week:
                return single_date

    elif all_weekdays(year,month,week,day_of_week).month != month:
        output = all_weekdays(year,month,week,day_of_week)
        return output - timedelta(days=7)
    else:
        output = all_weekdays(year,month,week,day_of_week)
        return output

def MeetupDayException():
    assert Exception("My exception message", str(excinfo.value))
