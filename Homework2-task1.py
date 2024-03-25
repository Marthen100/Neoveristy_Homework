def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Give me name and phone please."
        except KeyError as e:
            return f"No contact found with the name: {e}"
        except IndexError as e:
            return "Missing command parameters."
        except Exception as e:
            return str(e)
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Add command requires a name and a phone number.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Change command requires a name and a new phone number.")
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError("Phone command requires a name.")
    name = args[0]
    if name not in contacts:
        raise KeyError(name)
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts stored."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

if __name__ == "__main__":
    main()