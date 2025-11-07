##Focus on what an object does, rather than how it does it.
##Encapsulation is about protection - Hiding data (how it’s stored)
##Abstraction is about simplification - Hiding complexity (how it works)

class EmailService:
    def _connect(self):
        print("Connecting to Email server.")

    def _authenticate(self):
        print("Authenticating user.")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending Email")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from Server.")


email = EmailService()
email.send_email()