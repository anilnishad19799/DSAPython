""" Still double locking is slow we use bill pugh solution which make helper class of it"""

class DBConnection:
    def __init__(self):
        # Initialization code
        # For demonstration purposes, we initialize a simple attribute
        self.connection_string = "Your database connection string here"

    class __DBConnectionSingleton:
        def __init__(self):
            self.instance = DBConnection()

    _instance = None

    @staticmethod
    def get_instance():
        if not DBConnection._instance:
            DBConnection._instance = DBConnection.__DBConnectionSingleton().instance
        return DBConnection._instance