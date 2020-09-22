import json

class Account():
    def __init__(self, username, password, email, loan=[]):
        self.username = username
        self.password = password
        self.email = email
        self.loan = loan #[{loan1},{loan2},{loan3}]
    
    @classmethod
    def from_json(cls, data):
        username, password, email, loan = data["username"], data["password"], data["email"], data["loan"]
        return cls(username=username, password=password, email=email, loan=loan)
    
    def __str__(self):
        return f"This is username: {self.username}\nThis is password: {self.password}\nThis is email: {self.email}\nThis is loan: {self.loan}"