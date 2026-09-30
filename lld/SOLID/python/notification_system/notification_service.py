class NotificationService:

    def __init__(self, type, message):
        self.type = type
        self.message = message

    def email(self):
        print(f"{self.message} send through email")

    def sms(self):
        print(f"{self.message} send through sms")

    def push(self):
        print(f"{self.message} send through push notification")
