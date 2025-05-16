from thing_rental.exceptions.person_already_renting_exception import (
    PersonAlreadyRentingException,
)
from thing_rental.exceptions.thing_already_rented_exception import (
    ThingAlreadyRentedException,
)
from thing_rental.model.person import Person
from thing_rental.model.rental import Rental
from thing_rental.model.thing import Thing


class RentalService:
    current_rentals: list[Rental] = []

    def start_rental(self, person: Person, thing: Thing) -> None:
        for rental in self.current_rentals:
            if rental.person == person:
                raise PersonAlreadyRentingException

            if rental.thing == thing:
                raise ThingAlreadyRentedException

        self.current_rentals.append(Rental(person=person, thing=thing))
