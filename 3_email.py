#Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. The class should have two additional methods:
#· send() - sets the is_sent attribute to True
#· get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
#You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content. On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
#Call the sen#d() method for the given indices of emails. For each email, call the get_info() method.


class Email:
    def __init__(self, sender, resiver, content):
        self.sender = sender
        self.resiver = resiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return print(f"{self.sender} says to {self.resiver}: {self.content}. Sent: {self.is_sent}")

messages = []

while True:
    message = input()
    if message == "Stop":
        break
    sender, resiver, content = message.split()
    email = Email(sender, resiver, content)
    messages.append(email)

messeges_sent = list(map(int, input().split(", ")))
for x in messeges_sent:
    messages[x].send()

for message in messages:
    message.get_info()







