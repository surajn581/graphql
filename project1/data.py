import requests
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name = 'data.py')
logger.setLevel(level = logging.DEBUG)

DEFAULT = 'NOT FOUND'

def get_data(lat, long):
    url     = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=sunrise,sunset&forecast_days=1&timezone=auto'
    res = requests.get(url).json()
    logger.debug(res)
    data = dict( sunrise = res.get('daily').get('sunrise')[0], sunset = res.get('daily').get('sunset')[0], timezone = res.get('timezone') )
    return data

def read_data(lat, long):
    try:
        return get_data(lat, long)
    except Exception as ex:
        logger.error(ex)
        return dict(sunrise = DEFAULT, sunset = DEFAULT, timezone = DEFAULT)