from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen
from json import loads, dump
from buying_page import display_products


def render_entry():
    # creating the register button
    register_button = Button(
        root,  # the place where we hook it
        text="Register",
        background='green',
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )

    # attach the button to the frame
    frame.create_window(350, 260, window=register_button)

    # creating the register button
    login_button = Button(
        root,  # the place where we hook it
        text='Login',
        background='blue',
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    # attach the button to the frame
    frame.create_window(350, 320, window=login_button)


def get_users_data():
    info_data = []

    with open("gui_shop/db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def login():
    clean_screen()
    frame.create_text(100, 50, text='Username:')
    frame.create_text(100, 100, text='Password:')

    frame.create_window(200, 50, window=user_name_box)
    frame.create_window(200, 100, window=password_box)

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        borderwidth=0,
        fg="white",
        command=logging
    )

    frame.create_window(250, 150, window=login_button)


def check_logging():
    info_data = get_users_data()

    user_username = user_name_box.get()
    user_password = password_box.get()

    for record in info_data:
        record_username = record["Username"]
        record_password = record["Password"]

        if user_username == record_username and user_password == record_password:
            return True

    return False


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(160, 200, text="Invalid Username or Password!", fill="red")


def register():
    clean_screen()

    # create and attach text
    frame.create_text(100, 50, text='First Name')
    frame.create_text(100, 100, text='Last Name')
    frame.create_text(100, 150, text='User Name')
    frame.create_text(100, 200, text='Password')

    # attach the entry boxes
    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=user_name_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,  # the place where we hook it
        text="Register",
        background='green',
        fg='white',
        borderwidth=0,
        command=registration
    )

    frame.create_window(300, 250, window=register_button)


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': user_name_box.get(),
        'Password': password_box.get()
    }

    if check_registration(info_dict):
        with open("gui_shop/db/users_information.txt", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()


def check_registration(info):
    frame.delete('error')

    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error'
            )

            return False

    info_data = get_users_data()

    for record in info_data:
        if record["Username"] == info["Username"]:
            frame.create_text(
                300,
                300,
                text=f'Username is already taken!',
                fill='red',
                tags='error'
            )

            return False
    return True


# Creating this entry boxes in global
first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
user_name_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')
