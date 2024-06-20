""" To overcome issue of synchronized locking system we use double locking system 
    THe issue is memory issue of store objec tin cache not in menmory solve by volatile in java which is store data in memory
    slow due to store object in memeory not cache
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
        if DBConnection._instance is None:  # First check without lock
            with DBConnection._lock:
                if DBConnection._instance is None:  # Double-check with lock
                    DBConnection._instance = DBConnection()
        return DBConnection._instance
