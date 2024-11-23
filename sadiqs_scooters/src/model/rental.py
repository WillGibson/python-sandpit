from sadiqs_scooters.src.model.person import Person
from sadiqs_scooters.src.model.scooter import Scooter


class Rental:
    person: Person
    scooter: Scooter

    def __init__(self, person: Person, scooter: Scooter):
        self.person = person
        self.scooter = scooter
