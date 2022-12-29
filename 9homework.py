PHONE_VOCABULAR = [
    {"Contact_name": "Bill","Number": +380123456789},
    ]

name=input(str("Write name... "))
phone=input(str("Write phone... "))

def add_contact(*args):
    name = args[0]
    phone = args[1]
    PHONE_VOCABULAR.append({"Contact_name": name,"Number": phone})
    print(f'Contact {name} with phone: {phone} was created!')

def input_error(func):
    def wrapper(*args):
        func(*args)
        
    return wrapper

@input_error
def simple_func(text:str):
    return text.upper()

print(simple_func("Enter user name", "Give me name and phone please"))

def exiting():
    print('Goodbye')

def unknown():
    print('Command not exist')

def new_contact():
    return input(int("New numer..."))

def new_phone(*args):
    pass

def all_contacts():
    pass

COMMANDS = {add_contact: ['add', 'додай', "+"], exiting: ['exit', 'close', '.'],
            new_contact: ["change", "other"], new_phone:["phone","show number"], all_contacts:["show all"]}

def command_parser(user_input: int):
    inputs = user_input.split()
    for key, value in COMMANDS.items():
        if inputs[0].lower() in value:
            return key, inputs[1:] #повертаємо список слів без слова 'add'
        else:
            return unknown
       

def main():
    while True:
        user_input = input('>>> ')
        if user_input in COMMANDS[exiting]:
            break
        else:
            command, data = command_parser(user_input)
            command(data)

if __name__ == '__main__':
    main()