class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # You can add validation or constraints if needed
        self._name = new_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        # You can add validation or constraints if needed
        self._email = new_email

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number):
        # You can add validation or constraints if needed
        self._phone_number = new_phone_number
