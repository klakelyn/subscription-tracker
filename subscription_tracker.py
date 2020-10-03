
import csv
import tkinter as tk


## Originally prototype program that only ran through the commandline
## Currently being redeveloped using a GUI

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


## GUI program
## Currently redeveloping program from commandline interaction to GUI

if __name__ == "__main__":
    root = tk.Tk()
    MainInterface(root)
    root.mainloop()

class MainInterface:

    def __init__(self, main):
        self._main = main
        main.title("Subscription Tracker")

        # subscription entry box label (left of)
        sub_label = tk.Label(main, text="Subscription: ")
        sub_label.pack(side=tk.LEFT,anchor=tk.NW)
        # entry box for subscription name
        sub_entry = tk.Entry(main, width=30)
        sub_entry.pack(side=tk.LEFT,anchor=tk.N)
        # botton that searches for account info linked to subscription
        findBtn_sub = tk.Button(main, text="Find...", width=10, command=self.sub_search())
        findBtn_sub.pack(side=tk.RIGHT,anchor=tk.NE)
        # email entry box label (left of)
        findBtn_label = tk.Label(main, text="Email: ")
        findBtn_label.pack(side=tk.LEFT,anchor=tk.W)
        # entry box for email
        email_entry = tk.Entry(main, width=30)
        email_entry.pack(side=tk.LEFT)
        # botton that searches for account info linked to email
        findBtn_em = tk.Button(main, text="Find...", width=10, command=self.email_search())
        findBtn_em.pack(side=tk.RIGHT,anchor=tk.E)
        # button that brings user to a widget to add account details
        addBtn = tk.Button(main, text="Add", width=10, command=self.add())
        addBtn.pack(side=tk.BOTTOM,anchor=tk.SE)

    def add(self):

        account = Account(subscription, email, username, password)

    def sub_search(self):


    def email_search(self):


class Account():

    def __init__(self, subscription, email, username, password):
        self._subscription = subscription
        self._email = email
        self._username = username
        self._password = password

    def get_subscription(self):
        return self._subscription

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password
