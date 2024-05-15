from phone import Phone
from name import Name


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, number: str):
        # Додавання нового номеру телефону до запису
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        # Видалення номеру телефону з запису

        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number, new_number):
       # Редагування номеру телефону у записі

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        # Пошук номеру телефону у записі

        for phone in self.phones:
            if phone.value == number:
                return phone