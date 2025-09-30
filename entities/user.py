class User:
    def __init__(self,username: str, password_hash: str):
        self.username = username
        self._password_hash = password_hash

    def __repr__(self):
        return f"<User username = '{self.username}'>"
    
    def user_info(self):
        return f"User : {self.username}"