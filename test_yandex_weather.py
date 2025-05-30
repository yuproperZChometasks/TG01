import os
from dotenv import load_dotenv
import requests

# Загружаем переменные из файла .env
load_dotenv()
# Получаем значение переменной
API_TOKEN = os.getenv('TGBOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
BASE_WEATHER_URL = os.getenv('BASE_WEATHER_URL')

access_key = API_TOKEN

headers = {
    'X-Yandex-Weather-Key': access_key
}

response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=52.37125&lon=4.89388', headers=headers)

print(response.json())