
import csv


## Originally prototype program that only ran through the commandline
## Revised version uses GUI

def quit_continue():
    decision = input("Would you like to quit or continue? ")
    if decision == "quit":
        print("Program cancelled.")

    if decision == "continue":
        start()


def find_details():
    fieldnames = ['Subscription','Email','Username','Password']
    find = input('Would you like to a) find details pertaining to a specific digital service b) see subscriptions linked to each account? ')
    if find == 'a':
        name = input('Please enter website name: ')
        with open('subscription_data.csv', 'r') as website_specific:
            reader = csv.DictReader(website_specific,fieldnames=fieldnames)
            details = [row for row in reader if row['Subscription'] == name]
            for key,val in details[0].items():
                print(key+':',val)
        quit_continue()

    if find == 'b':
        email = input('Please enter email: ')
        with open('subscription_data.csv', 'r') as email_specific:
            email_reader = csv.DictReader(email_specific, fieldnames=fieldnames)
            subscriptions = [row for row in email_reader if row['Email'] == email]
            print('Subscription:',subscriptions[0]['Subscription'])
        quit_continue()


def edit_details():
    edit = input("Would you like to add, remove or change details? ")
    if edit == 'add':
        name = input('Please enter the application name: ')
        email = input('Please enter your email address: ')
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        sub_dict = [name,email,username,password]

        with open('subscription_data.csv', 'a+', newline='') as sa:
            csv_writer = csv.writer(sa)
            csv_writer.writerow(sub_dict)

        print('Your information has been saved.')
        quit_continue()

    if edit == 'remove':
        #with open('subscription_archive.py', '+') as sa:
        app = input('Please enter the application name: ')
        with open('subscription_data.csv', 'a+', newline='') as sa:
            csv_writer = csv.DictWriter(sa)
            csv_writer.writerow(sub_dict)

    if edit == 'change':
        print('pathway in development')
        #with open('subscription_archive.py', 'w') as sa:

def start():
    decision = input("Would you like to find or edit details? ")
    if decision == 'find':
        find_details()


    elif decision == 'edit':
        edit_details()

    else:
        print("Invalid response.")
        quit_continue()

start()
