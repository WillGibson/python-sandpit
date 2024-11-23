from sadiqs_scooters.exceptions import PersonAlreadyRentingException, ScooterAlreadyRentedException
from sadiqs_scooters.person import Person
from sadiqs_scooters.rental import Rental
from sadiqs_scooters.scooter import Scooter


class RentalService:
    current_rentals: list[Rental] = []

    def start_rental(self, person: Person, scooter: Scooter) -> None:
        for rental in self.current_rentals:
            if rental.person == person:
                raise PersonAlreadyRentingException

            if rental.scooter == scooter:
                raise ScooterAlreadyRentedException

        self.current_rentals.append(Rental(person=person, scooter=scooter))
