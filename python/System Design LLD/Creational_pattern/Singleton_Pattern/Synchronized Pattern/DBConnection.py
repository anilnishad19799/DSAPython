""" To overcome Lazy issue of threading we use synchronized 
    we use synchronized lock so that one thread can enter at one time
    
    Issue in this
    so many request come in this it will pass only one thread at a time which make it slow of locking and unlocking
"""

import threading

class DBConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # Initialization code
        # For demonstration purposes, we initialize a simple attribute
        self.connection_string = "Your database connection string here"

    @staticmethod
    def get_instance():
        if DBConnection._instance is None:
            with DBConnection._lock:
                if DBConnection._instance is None:
                    DBConnection._instance = DBConnection()
        return DBConnection._instance