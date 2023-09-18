class Customer:
    def __init__(
        self,
        customer_id,
        customer_name,
        customer_licence_number,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_licence_number = customer_licence_number

    def __str__(self):
        return f"customer_id: {self.customer_id}, customer_name:{self.customer_name}, customer_licence_number: {self.customer_licence_number}"