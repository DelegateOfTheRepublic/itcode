import datetime
import python_weather
import asyncio
from typing import Coroutine

def to_celcius(temperature) -> float:
    return (temperature - 32) * 5/9

async def get_weather() -> None:
    months:list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    cold_message: str = '\nХолодно, лучше остаться дома'

    day: int = datetime.date.today().day
    month: str = months[datetime.date.today().month % len(months) - 1]

    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather: Coroutine = await client.get("Ufa")
        temperature: float = to_celcius(weather.current.temperature)
        weather_message: str = f"Сегодня {day} {month}. На улице {temperature:.3f} градусов"

        print(weather_message if temperature >= 0 else weather_message + cold_message)

if __name__ == '__main__':
    asyncio.run(get_weather())