from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def reset_password(self, new_password: str):
        self._password = new_password
