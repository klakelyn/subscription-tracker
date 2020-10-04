

## redeveloped subscription tracker that utilises GUI
## see original commandline prototype

import csv
import tkinter as tk

class MainInterface:

    def __init__(self, main):
        self._main = main
        main.title("Subscription Tracker")
        self._fieldnames = ['Subscription','Email','Username','Password']

        # subscription search bar
        sub_search = tk.Frame(main)
        # subscription entry box label (left of)
        sub_label = tk.Label(sub_search, text="Subscription: ")
        sub_label.pack(side=tk.LEFT,anchor=tk.NW)
        # entry box for subscription name
        self.sub_entry = tk.Entry(sub_search, width=30)
        self.sub_entry.pack(side=tk.LEFT,anchor=tk.NW)
        # botton that searches for account info linked to subscription
        findBtn_sub = tk.Button(sub_search, text="Find...", width=10, command=self.sub_search)
        findBtn_sub.pack(side=tk.RIGHT,anchor=tk.E)
        sub_search.pack(anchor=tk.W)

        # email search bar
        email_search = tk.Frame(main)
        # email entry box label (left of)
        email_label = tk.Label(email_search, text="Email: ")
        email_label.pack(side=tk.LEFT,anchor=tk.W)
        # entry box for email
        self.email_entry = tk.Entry(email_search, width=30)
        self.email_entry.pack(side=tk.LEFT,anchor=tk.W)
        # botton that searches for account info linked to email
        findBtn_em = tk.Button(email_search, text="Find...", width=10, command=self.email_search)
        findBtn_em.pack(side=tk.RIGHT,anchor=tk.E)
        email_search.pack(anchor=tk.W)

        # button that brings user to a widget to add account details
        addBtn = tk.Button(main, text="Add", width=10, command=self.add)
        addBtn.pack(side=tk.BOTTOM,anchor=tk.SE)
        
    def add(self):
        addpage = AddPage(self._main)

    def sub_search(self):
        subResult = SubResult(self._main,self._fieldnames,self.sub_entry.get())

    def email_search(self):
        emResults = EmailResults(self._main,self._fieldnames,self.email_entry.get())


class EmailResults(MainInterface):

    def __init__(self,root,fieldnames,email_search):
        self.emRes = tk.Toplevel(root)
        self.emRes.title("Subscriptions linked to email")
        heading = tk.Label(self.emRes,text="Subscriptions:")
        heading.pack(anchor=tk.NW)

        # cancel button
        cancelBtn = tk.Button(self.emRes, text="Cancel", width=10, command=self.cancel)
        cancelBtn.pack(side=tk.BOTTOM,anchor=tk.SW)

        with open('subscription_data.csv', 'r') as email_specific:
            email_reader = csv.DictReader(email_specific, fieldnames=fieldnames)
            subscriptions = [row for row in email_reader if row['Email'] == email_search]
            for row in subscriptions:
                label = tk.Label(self.emRes, text=row.get('Subscription'))
                label.pack(anchor=tk.NW)

    def cancel(self):
        self.emRes.destroy()


class SubResult(MainInterface):

    def __init__(self,root,fieldnames,sub_search):
        self.subResult = tk.Toplevel(root)
        self.subResult.title("Subscription details")

        # cancel button
        cancelBtn = tk.Button(self.subResult, text="Cancel", width=10, command=self.cancel)
        cancelBtn.pack(side=tk.BOTTOM,anchor=tk.SW)

        with open('subscription_data.csv', 'r') as website_specific:
            reader = csv.DictReader(website_specific,fieldnames=fieldnames)
            rows = [row for row in reader if row['Subscription'] == sub_search]

        try:
            data = rows[0]
        except IndexError:
            return None

        sub = "Subscription: "+data.get('Subscription')
        email = "Email: "+data.get('Email')
        username = "Username: "+data.get('Username')
        password = "Password: "+data.get('Password')

        sub_label = tk.Label(self.subResult, text=sub)
        sub_label.pack(anchor=tk.NW)

        email_label = tk.Label(self.subResult, text=email)
        email_label.pack(anchor=tk.NW)

        username_label = tk.Label(self.subResult, text=username)
        username_label.pack(anchor=tk.NW)

        password_label = tk.Label(self.subResult, text=password)
        password_label.pack(anchor=tk.NW)

    def cancel(self):
        self.subResult.destroy()


class AddPage(MainInterface):
    
    def __init__(self,root):
        self.addPage = tk.Toplevel(root)
        self.addPage.title("Add Subscription")

        sub_add = tk.Frame(self.addPage)
        # subscription entry box label (left of)
        sub_label = tk.Label(sub_add, text="Subscription: ")
        sub_label.pack(side=tk.LEFT,anchor=tk.NW)
        # entry box for subscription name
        self.sub_entry = tk.Entry(sub_add, width=30)
        self.sub_entry.pack(side=tk.LEFT,anchor=tk.NW)
        sub_add.pack(anchor=tk.W)

        email_add = tk.Frame(self.addPage)
        # email entry box label (left of)
        email_label = tk.Label(email_add, text="Email: ")
        email_label.pack(side=tk.LEFT,anchor=tk.W)
        # entry box for email
        self.email_entry = tk.Entry(email_add, width=30)
        self.email_entry.pack(side=tk.LEFT,anchor=tk.W)
        email_add.pack(anchor=tk.W)

        username_add = tk.Frame(self.addPage)
        # email entry box label (left of)
        username_label = tk.Label(username_add, text="Username: ")
        username_label.pack(side=tk.LEFT,anchor=tk.W)
        # entry box for email
        self.username_entry = tk.Entry(username_add, width=30)
        self.username_entry.pack(side=tk.LEFT,anchor=tk.W)
        username_add.pack(anchor=tk.W)

        password_add = tk.Frame(self.addPage)
        # email entry box label (left of)
        password_label = tk.Label(password_add, text="Password: ")
        password_label.pack(side=tk.LEFT,anchor=tk.W)
        # entry box for email
        self.password_entry = tk.Entry(password_add, width=30)
        self.password_entry.pack(side=tk.LEFT,anchor=tk.W)
        password_add.pack(anchor=tk.W)

        # cancel button
        cancelBtn = tk.Button(self.addPage, text="Cancel", width=10, command=self.cancel)
        cancelBtn.pack(side=tk.LEFT,anchor=tk.SW)

        # add button
        addBtn = tk.Button(self.addPage, text="Add", width=10, command=self.add)
        addBtn.pack(side=tk.BOTTOM,anchor=tk.SE)

    def cancel(self):
        self.addPage.destroy()

    def add(self):
        account = Account(self.sub_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())
        account.addAccount()
        self.addPage.destroy()


class Account:

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

    def addAccount(self):
        sub_dict = [self.get_subscription(),self.get_email(),self.get_username(),self.get_password()]
        with open('subscription_data.csv', 'a+', newline='') as sa:
            csv_writer = csv.writer(sa)
            csv_writer.writerow(sub_dict)


if __name__ == "__main__":
    root = tk.Tk()
    MainInterface(root)
    root.mainloop()
