from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

city = input('Введите город: ')

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('65dee4c0dbc35fee27c9cb775e26a7fb', config_dict)

mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius').get('temp')
clouds = w.detailed_status

print('В городе {} сейчас {}, {} градусов'.format(city, clouds, temp))
input()