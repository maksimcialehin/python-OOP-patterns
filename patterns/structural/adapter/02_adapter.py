import math
from abc import ABC, abstractmethod


class Navigator(ABC):
    @abstractmethod
    def get_position(self) -> dict:
        pass


class OffworldGPS:
    def __init__(self, lat_rad: float, lon_rad: float, alt_m: float):
        self._lat = lat_rad
        self._lon = lon_rad
        self._alt = alt_m

    def get_coordinates_rad(self) -> tuple:
        return (self._lat, self._lon)

    def get_altitude_meters(self) -> float:
        return self._alt


class OffworldGPSAdapter(Navigator):
    def __init__(self, offworld: OffworldGPS) -> None:
        self._offworld = offworld

    @staticmethod
    def rad_to_deg(value) -> float:
        return value * 180 / math.pi

    def get_position(self) -> dict[str, float]:
        lat, lon = self._offworld.get_coordinates_rad()
        return {
            'lat_deg': round(self.rad_to_deg(lat), 6),
            'lon_deg': round(self.rad_to_deg(lon), 6),
            'alt_km': round(self._offworld.get_altitude_meters() / 1000, 3),
        }
