

import csv
import tkinter as tk

def quit_continue():
    decision = input("Would you like to quit or continue? ")
    if decision == "quit":
        print("Program cancelled.")

    if decision == "continue":
        start()


def find_details():
    find = input('Would you like to a) find details pertaining to a specific digital service b) see subscriptions linked to each account? ')
    if find == 'a':
        name = input('Please enter website name: ')
        with open('subscription_data.csv', 'r') as website_specific:
            reader = csv.reader(website_specific)
            rows = list(reader)
            for count,item in enumerate(rows):
                if item[0] == name:
                    print('Email:', rows[count][1] + '\nUsername:', rows[count][2] + '\nPassword:', rows[count][3])
        quit_continue()

    if find == 'b':
        email = input('Please enter email: ')
        with open('subscription_data.csv', 'r') as email_specific:
            reader = csv.reader(email_specific)
            rows = list(reader)
            item_count = 0
            for count,item in enumerate(rows):
                if item[1] == email:
                    print(rows[count][0])
        quit_continue()


def edit_details():
    edit = input("Would you like to add, remove or change details? ")
    if edit == 'add':
        #with open('subscription_archive.py', 'a') as sa:

        #enter application/website/service/etc.
        y = input(prompt + 'the application name: ')
        applications.append(y)
        print(applications)

        #enter email address used
        y = input(prompt + 'your email address: ')
        email_address.append(y)
        print(email_address)

        #enter username
        y = input(prompt + 'your username: ')

        #usernames.append

        #enter password
        y = input(prompt + 'your password: ')

        #passwords.append

        #programmed finished

        print("Your information has been saved.")
        quit_continue()

    if edit == 'remove':
        print('pathway in development')
        #with open('subscription_archive.py', '+') as sa:

    if edit == 'change':
        print('pathway in development')
        #with open('subscription_archive.py', 'w') as sa:


def start():
    x = input("Would you like to find or edit details? ")
    if x == 'find':
        find_details()


    elif x == 'edit':
        edit_details()

    else:
        print("Invalid response.")
        quit_continue()

start()

root = tk.Tk()

root.title('Subscription Tracker')

root.mainloop()