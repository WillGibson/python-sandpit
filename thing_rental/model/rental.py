from thing_rental.model.person import Person
from thing_rental.model.thing import Thing


class Rental:
    person: Person
    thing: Thing

    def __init__(self, person: Person, thing: Thing):
        self.person = person
        self.thing = thing
