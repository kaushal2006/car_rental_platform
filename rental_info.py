from datetime import timedelta
import datetime

class RentalInfo:
    def __init__(
        self,
        customer_id,
        car_id,
        rental_term = None,
        rental_duration = None,
        rental_rate = None,
        rental_start_datetime = None,
        rental_end_datetime = None,
        bill = None,
        rental_return_datetime = None,
        final_bill = None
    ):
        self.customer_id = customer_id
        self.car_id = car_id
        self.rental_term = rental_term
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.rental_start_datetime = rental_start_datetime
        self.rental_end_datetime = rental_end_datetime
        self.bill = bill
        self.rental_return_datetime = rental_return_datetime
        self.final_bill = final_bill

    def __str__(self):
        return f"car_id: {self.car_id}, customer_id:{self.customer_id}, rental_start_datetime: {self.rental_start_datetime}, rental_end_datetime:{self.rental_end_datetime}, bill:{self.bill}, rental_return_datetime:{self.rental_return_datetime}, final_bill:{self.final_bill}"

    def setupRental(self, rental_term, rental_duration, rental_rate):
        self.rental_term = rental_term
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.rental_start_datetime = datetime.datetime.now()
        self.bill = self.rental_rate * self.rental_duration
        if(self.rental_term == "Hourly"):
            self.rental_end_datetime = self.rental_start_datetime + timedelta(hours = self.rental_duration)  
        elif(self.rental_term == "Daily"):
            self.rental_end_datetime = self.rental_start_datetime + timedelta(days = self.rental_duration)
        else:
            self.rental_end_datetime = self.rental_start_datetime + timedelta(days = self.rental_duration * 7)
        
    def closeRental(self, rental_return_datetime):
        self.rental_return_datetime = rental_return_datetime
        #you can add validation for Null check, guess too much for this assignment
        if(self.rental_return_datetime > self.rental_end_datetime):
            diff = self.rental_return_datetime - self.rental_end_datetime

            if(self.rental_term == "Hourly"):
                #copied this from stacktrace, not validated thoroughly
                #https://stackoverflow.com/questions/24217641/how-to-get-the-difference-between-two-dates-in-hours-minutes-and-seconds
                days, seconds = diff.days, diff.seconds
                diff_hours = days * 24 + seconds // 3600
                self.final_bill = self.rental_rate * diff_hours
            elif(self.rental_term == "Daily"):
                self.rental_return_date = self.rental_return_datetime.date()
                rental_end_date = self.rental_end_datetime.date()
                diff_in_days = rental_return_date - rental_end_date
                #for time being, adding flat penalty
                self.final_bill = self.bill + 200
            else:
                #for time being, adding flat penalty
                self.final_bill = self.bill + 1000
        else:
            self.final_bill = self.bill