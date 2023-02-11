class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
        pass

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:

    system_input = input()
    if system_input == "Stop":
        break
    else:
        s_sender, s_receiver, s_content = system_input.split()

    email = Email(s_sender, s_receiver, s_content)
    emails.append(email)

send_emails = [int(number) for number in input().split(', ')]

for send in send_emails:
    emails[send].send()

for email_info in emails:
    print(email_info.get_info())
    