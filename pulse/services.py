import random


class MockFlightService:

    @staticmethod
    def search_flights(origin, destination):

        prices = [
            3200,
            3500,
            4200,
            4800,
            5200,
            6100,
            7500,
        ]

        return {
            "origin": origin,
            "destination": destination,
            "airline": random.choice(
                [
                    "IndiGo",
                    "Air India",
                    "SpiceJet",
                    "Akasa Air",
                ]
            ),
            "price": random.choice(prices),
            "currency": "INR",
        }