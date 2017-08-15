'''This code is intended to take a csv file containing weather station connection and disconnection dates
   and provide a histogram of active weather stations over time'''

import datetime

def plot_data():
    return

def read_csv():
    return

def dict_setup(min_date, max_date):
    curr_date = min_date
    date_dict = {}
    while curr_date <= max_date:
        date_dict[curr_date]=0
        curr_date = curr_date + datetime.timedelta(days=1)
    return date_dict

def modify_dict():
    return
min_date = datetime.date(1982, 5, 30)
max_date = datetime.date(2017, 1, 1)
date_dict = dict_setup(min_date, max_date)

print (date_dict)

