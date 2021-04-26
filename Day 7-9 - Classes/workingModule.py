class Message():
    def __init__(self, username, email, message):
        self.username = username
        self.email = email
        self.message = message
    def create_message(self):
        return "Hello {0}! We have just received a message from {1}. {2} ".format(self.username, self.email, self.message)