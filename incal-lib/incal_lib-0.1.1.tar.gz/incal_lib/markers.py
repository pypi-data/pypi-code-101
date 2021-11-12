# custome day
import pandas as pd
import numpy as np
import datetime as dt


def custome_days(pd_DateTime64, hour=00, minute=00, sec=00):
    time_1 = dt.timedelta(hours=00, minutes=00, seconds=00)
    time_2 = dt.timedelta(hours=hour, minutes=minute, seconds=sec)
    return (pd_DateTime64 - (time_2 - time_1))


def day_and_night(pd_index_datetime, start='08:30', end='16:30'):
    times = np.array([time.time() for time in pd_index_datetime])
    greater = pd.to_datetime(start).time() <= times
    stricly_less = pd.to_datetime(end).time() > times
    return np.where((greater & stricly_less), 'Day', 'Night')


# decrepted
def __decrepted_count_custome_day_start_and_end(pd_index_datetime, shift_time='8:30am'):
    dates = sorted(set(pd_index_datetime.date))
    times = np.array([time.time() for time in pd_index_datetime
                      ])
    shift_time = pd.to_datetime(shift_time).time()
    conditiones = [
        cond for date in dates for cond in [
            ((times < shift_time)
             & (pd_index_datetime.date == date)),  # day before
            ((times >= shift_time)
             & (pd_index_datetime.date == date))   # day after
        ]
    ]
    langth = (len(conditiones) // 2) + 1
    choices = [0, *np.repeat(range(1, langth), 2)]
    choices.pop()
    return np.select(conditiones, choices, pd_index_datetime.factorize()[0])
