from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import datetime as dt

#clientside callback arguments
clientside_callback_args = (
   """
    function(n) {          
        const local_time_str = new Date().toLocaleString('en-GB');                   
        return local_time_str
    }
    """,
    Output('browser-time', 'data'),
    Input('browser-time-interval', 'n_intervals'),
)

#function for setting on page
def htmlObj():
    return html.Div(
        children = [
            dcc.Store(id = "browser-time"),
            dcc.Interval(id = "browser-time-interval")
        ],
        style = {"display": "none"}
    )

#convert browsertime string to datetime object
def datetime(bt):
    return dt.datetime.strptime(bt, "%d/%m/%Y, %H:%M:%S")

#for calculating browsertime string in time shift hours
def time_shift(bt):
    bt_dt = datetime(bt)
    utc_dt = dt.datetime.utcnow()
    if bt_dt > utc_dt:
        ts = bt_dt - utc_dt
        ts_sec = round(ts.seconds/60)*60
    else:
        ts = utc_dt - bt_dt
        ts_sec = round(ts.seconds/60)*(-60)
    return dt.timedelta(seconds = ts_sec)