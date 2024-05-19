from addressbook import AddressBook, Record

# Decorator with error handler for command functions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "KeyError. Try using a valid key."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
    
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

# @input_error
# def change_contact(args, contacts):
#     name, phone = args
#     if name in contacts:
#         contacts[name] = phone
#         return "Contact updated."
#     else:
#         return f"The contact with the name '{name}' does NOT exist!"


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    if book.find(name):
        return book.find(name)


@input_error
def show_all(book: AddressBook):
    return_str = "\n"
    for name, record in book.data.items():
        return_str += f"{record} \n"
    return return_str
    # return '\n'.join(map('\t'.join, book.data.items()))

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if birthday:
        record.add_birthday(birthday)
    return message

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    if book.find(name):
        return book.find(name).birthday

@input_error
def show_birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()


def help_info():
    return """
        help                                    - to show this information
        hello                                   - to show the greeting
        add [ім'я] [номер телефону]             - to add contact
        change [ім'я] [новий номер телефону]    - to change contact phone number
        phone [ім'я]                            - to show contact phone number
        all                                     - to show list of all contacts
        add-birthday [ім'я] [дата народження]   - to add birthday to contact
        show-birthday [ім'я]                    - to show contact birthday
        birthdays                               - to show list with next week birthdays
        close
        exit
        """


def main():
    #contacts = {}
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        # > add [ім'я] [номер телефону]
        elif command == "add":
            print(add_contact(args, book))

        # > change [ім'я] [новий номер телефону]
        elif command == "change":
            print(add_contact(args, book))

        # > phone [ім'я]
        elif command == "phone":
            print(show_phone(args, book))

        # > all
        elif command == "all":
            print(show_all(book))

        # > add-birthday [ім'я] [дата народження]
        elif command == "add-birthday":
            print(add_birthday(args, book))

        # > show-birthday [ім'я] 
        elif command == "show-birthday":
            print(show_birthday(args, book))
        
        # > birthdays
        elif command == "birthdays":
            print(show_birthdays(book))

        # > help_info
        elif command == "help":
            print(help_info())

        else:
            print("Enter valid command!")
            print(help_info())


if __name__ == "__main__":
    main()