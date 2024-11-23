from sadiqs_scooters.person import Person
from sadiqs_scooters.scooter import Scooter


class Rental:
    person: Person
    scooter: Scooter

    def __init__(self, person: Person, scooter: Scooter):
        self.person = person
        self.scooter = scooter
