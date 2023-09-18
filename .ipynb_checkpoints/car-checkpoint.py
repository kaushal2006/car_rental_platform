class Car:
    def __init__(
        self,
        car_id,
        car_name,
        car_year,
        number_plate,
        rental_rates = {"Hourly": None, "Daily": None, "Weekly": None},
        is_available_for_rent="N",
        is_rented="N",
    ):
        self.car_id = car_id
        self.car_name = car_name
        self.car_year = car_year
        self.number_plate = number_plate
        self.rental_rates = rental_rates
        self.is_available_for_rent = is_available_for_rent
        self.is_rented = is_rented

    def __str__(self):
        return f"car_id: {self.car_id}, car_name:{self.car_name}, rental_rates: {self.rental_rates}, is_available_for_rent:{self.is_available_for_rent}, is_rented:{self.is_rented}"

    def setForRental(self, rental_rates, available_for_rent):
        self.rental_rates = rental_rates
        self.is_available_for_rent = available_for_rent
        self.is_rented = "N"  # better to reset to N for safety net

    def resetRental(self):
        self.rental_rates = {"Hourly": None, "Daily": None, "Weekly": None}
        self.is_available_for_rent = "N"
        self.is_rented = "N"
        
    def rentACar(self):
        self.is_rented = "Y"

    def returnACar(self):
        self.is_rented = "N"