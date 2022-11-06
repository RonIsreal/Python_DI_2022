'''Exercise 1 : Call History
Instructions
Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

Add a method called show_call_history. This method should print the call_history.

Add another attribute called messages to your __init__() method which value is an empty list.

Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
to : the number of another Phone object
from : your phone number (also a Phone object)
content

Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

Test your code !!!
'''

class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.outgoing_messages = []
        self.incoming_messages = []

    def call(self, other_phone):
        call_made = str(f"{self.phone_number} called {other_phone}.")
        print(call_made)
        self.call_history.append(call_made)

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, receiver, content):
        message = dict(sender = self.phone_number, receiver = receiver, content = content)
        self.outgoing_messages.append(message)

    def receive_message(self, sender, content):
        received_message = dict(sender = sender, receiver = self.phone_number, content = content)
        self.incoming_messages.append(received_message)

    def show_outgoing_messages(self):
        print(self.outgoing_messages)

    def show_incoming_messages(self):
        print(self.incoming_messages)

my_phone = Phone('0548020202')
my_phone.call('0537777054')
my_phone.show_call_history()
my_phone.send_message('0537777054', "Hello my love")
my_phone.receive_message('0537777054', "Hello you my love")
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()


