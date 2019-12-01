from datetime import datetime, timedelta

def add(moment):
    date_N_seconds_later = moment + timedelta(seconds=1000000000)
    return date_N_seconds_later
