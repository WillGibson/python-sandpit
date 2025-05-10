import pytest

from thing_rental.src.exceptions.person_already_renting_exception import (
    PersonAlreadyRentingException,
)
from thing_rental.src.exceptions.thing_already_rented_exception import (
    ThingAlreadyRentedException,
)
from thing_rental.src.model.person import Person
from thing_rental.src.model.thing import Thing
from thing_rental.src.rental_service import RentalService


class TestRentalService:
    def test_person_can_rent_a_thing(self):
        person: Person = Person()
        thing: Thing = Thing()
        rental_service = RentalService()

        rental_service.start_rental(person, thing)

    def test_person_cannot_rent_more_than_one_thing(self):
        person: Person = Person()
        thing1: Thing = Thing()
        thing2: Thing = Thing()
        rental_service = RentalService()
        rental_service.start_rental(person, thing1)

        with pytest.raises(PersonAlreadyRentingException):
            rental_service.start_rental(person, thing2)

    def test_thing_cannot_be_rented_by_more_than_one_person(self):
        person1: Person = Person()
        person2: Person = Person()
        thing: Thing = Thing()
        rental_service = RentalService()
        rental_service.start_rental(person1, thing)

        with pytest.raises(ThingAlreadyRentedException):
            rental_service.start_rental(person2, thing)
