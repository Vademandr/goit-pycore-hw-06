from field import Field


class Phone(Field):

    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):
        # Перевірка на коректність формату номеру телефону

        if len(number) != 10:
            raise ValueError("Phone number must be a string of 10 digits.")

        if not number.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return number