class Email:
    def __init__(self, email: str):
        if '@' not in email:
            raise ValueError("Invalid email format")
        self.email = email

    def __eq__(self, other):
        return self.email == other.email
