import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

"""This program to create a encryption password with a given Key and can get access when both the encryption and decryption key is at same location as 
   the password is created with the latitude and longitude"""

# Constant Keys
ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Free ipinfo Token
TOKEN = "8184cadabe3650"


# Geological Latitude and Longitude Algorithm Convertor
def geo_lat_long_convertor(latitude, longitude, time_minute, time_am_pm):
    """Function is to Convert the symbols to number and then the lattitude and longitude is linked to minutes for stronger encryption"""
    if time_am_pm == "AM":
        latitude = latitude + float(time_minute)
        longitude = longitude - float(time_minute)
        latitude = round(latitude, 4)
        longitude = round(longitude, 4)
    else:
        latitude = latitude - float(time_minute)
        longitude = longitude + float(time_minute)
        latitude = round(latitude, 4)
        longitude = round(longitude, 4)
    return latitude, longitude


# Latitude and Longitude alpha encryption
def encryption(lat_code, long_code, time_minute):
    """Converting the latitude and longitude into a string with random variables"""
    lat_password_string = ""
    long_password_string = ""
    lat_code = str(lat_code).replace(".", "0")
    long_code = str(long_code).replace(".", "1")
    lat_code = str(lat_code).replace("-", "0")
    long_code = str(long_code).replace("-", "1")
    for i in str(lat_code):
        lat_password_string += ALPHABETS[(int(i) + time_minute) % 26]
    for i in str(long_code):
        long_password_string += ALPHABETS[(int(i) + time_minute) % 26]
    return lat_password_string, long_password_string


# Final Encryption
class Keys:
    def __init__(self):
        pass

    def password_encrypter(self):
        """This program to create a encryption password with a given Key and can get access when both the encryption and decryption key is at same location as
           the password is created with the latitude and longitude"""
        try:
            """Getting the current location and timezone"""
            res = requests.get('https://ipinfo.io/103.171.10.65/json?token=' + TOKEN)
            data = res.json()
            city = data['city']
            location = data['loc'].split(',')

            latitude = float(location[0])
            longitude = float(location[1])
            tf = TimezoneFinder()
            time_zone = tf.timezone_at(lng=float(longitude), lat=float(latitude))

            IST = pytz.timezone(time_zone)
            datetime_ist = datetime.now(IST)
            time_minute = int(datetime_ist.strftime('%M'))
            time_am_pm = datetime_ist.strftime('%p')
            # Getting seconds from the Time Zone For the change of password timezone
            seconds = datetime_ist.strftime('%S')

            lat_code, long_code = geo_lat_long_convertor(latitude, longitude, time_minute, time_am_pm)

            lat_password, long_password = encryption(lat_code, long_code, time_minute)
            final_key = lat_password + long_password
            # Returning both password and seconds in the password_encrypter finction
            return final_key, seconds

        except ConnectionError as e:
            print(e)
            r = "ERROR: No Internet Connection! . Check Internet Status!!"

        except:
            raise Exception("Technical Error")




