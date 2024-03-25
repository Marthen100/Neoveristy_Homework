from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if isinstance(value, str) and value.strip():
            self.value = value.strip()
        else:
            raise ValueError("Name field is required")

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

    @staticmethod
    def validate(phone):
        return phone.isdigit() and len(phone) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Creation of a new address book
    book = AddressBook()

    # Creation of an entry for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add a John entry to the address book
    book.add_record(john_record)

    # Creating and adding a new entry for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all entries in the contact list
    for name, record in book.items():
        print(record)

    # Find and edit a phone number for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

    # Searching for a phone number in John's entry
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"{john.name}: {found_phone}")  

    # Deletion: Jane's entry
    book.delete("Jane")