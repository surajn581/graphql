import requests
import logging

DEFAULT = 'NOT FOUND'

def get_data(lat, long):
    url     = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=sunrise,sunset&forecast_days=1&timezone=auto'
    res = requests.get(url).json()
    print(res)
    data = dict( sunrise = res.get('daily').get('sunrise')[0], sunset = res.get('daily').get('sunset')[0] )
    return data

def read_data(lat, long):
    try:
        return get_data(lat, long)
    except Exception as ex:
        logging.error(ex)
        return dict(sunrise = DEFAULT, sunset = DEFAULT)