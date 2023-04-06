from dataclasses import dataclass


@dataclass
class AverageDurationOfTripsInDays:
    number_of_trips: int
    average_duration: float


@dataclass
class TripsTotalPriceOfActivities:
    name: str
    total_price: float


@dataclass
class TripsBasedOnAverageComfortOfTransportations:
    name: str
    average_comfort: float
