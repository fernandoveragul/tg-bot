from enum import Enum

from pydantic import BaseModel


class Location(BaseModel):
    latitude: float | None = None
    longitude: float | None = None


class Temperature(BaseModel):
    temp: float | None = None
    feels_like: float | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    pressure: int | None = None
    humidity: int | None = None


class Wind(BaseModel):
    speed: float | None = None
    deg: int | None = None


class Sun(BaseModel):
    type: int | None = None
    id: int | None = None
    country: str | None = None
    sunrise: int | None = None
    sunset: int | None = None


class WindDirection(Enum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315
