from datetime import date, timedelta

def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

def meetup(year, month, week, day_of_week):

    start_date = date(year, month, 13)
    end_date = date(year, month, 20)

    for single_date in daterange(start_date, end_date):
        if single_date.strftime("%A") == day_of_week:
            return single_date



def MeetupDayException():
    pass
