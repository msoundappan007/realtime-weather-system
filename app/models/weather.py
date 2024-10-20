from pydantic import BaseModel
from datetime import datetime

class WeatherData(BaseModel):
    
    city: str
    main: str
    temp: float
    feels_like: float
    dt: datetime
    humidity: float
    min_temp: float
    max_temp: float
    wind_speed: float
