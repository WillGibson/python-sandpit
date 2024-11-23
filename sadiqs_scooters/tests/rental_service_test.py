import pytest

from sadiqs_scooters.src.exceptions.person_already_renting_exception import \
    PersonAlreadyRentingException
from sadiqs_scooters.src.exceptions.scooter_already_rented_exception import \
    ScooterAlreadyRentedException
from sadiqs_scooters.src.model.person import Person
from sadiqs_scooters.src.model.scooter import Scooter
from sadiqs_scooters.src.rental_service import RentalService


class RentalServiceTest:
    def test_person_can_rent_a_scooter(self):
        person: Person = Person()
        scooter: Scooter = Scooter()
        rental_service = RentalService()

        rental_service.start_rental(person, scooter)


    def test_person_cannot_rent_more_than_one_scooter(self):
        person: Person = Person()
        scooter1: Scooter = Scooter()
        scooter2: Scooter = Scooter()
        rental_service = RentalService()
        rental_service.start_rental(person, scooter1)

        with pytest.raises(PersonAlreadyRentingException):
            rental_service.start_rental(person, scooter2)


    def test_scooter_cannot_be_rented_by_more_than_one_person(self):
        person1: Person = Person()
        person2: Person = Person()
        scooter: Scooter = Scooter()
        rental_service = RentalService()
        rental_service.start_rental(person1, scooter)

        with pytest.raises(ScooterAlreadyRentedException):
            rental_service.start_rental(person2, scooter)

