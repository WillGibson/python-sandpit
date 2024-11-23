from sadiqs_scooters.src.exceptions.person_already_renting_exception import \
    PersonAlreadyRentingException
from sadiqs_scooters.src.exceptions.scooter_already_rented_exception import \
    ScooterAlreadyRentedException
from sadiqs_scooters.src.model.person import Person
from sadiqs_scooters.src.model.rental import Rental
from sadiqs_scooters.src.model.scooter import Scooter


class RentalService:
    current_rentals: list[Rental] = []

    def start_rental(self, person: Person, scooter: Scooter) -> None:
        for rental in self.current_rentals:
            if rental.person == person:
                raise PersonAlreadyRentingException

            if rental.scooter == scooter:
                raise ScooterAlreadyRentedException

        self.current_rentals.append(Rental(person=person, scooter=scooter))
