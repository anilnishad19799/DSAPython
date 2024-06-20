""" Lazy Initialization overcome eager initialization issue 
    Issue in eager initialization is that whether you call class fucntion or not its object will created
    in Lazy initialization if class calls then it created object

    Diadvantage of Lazy 
    if two thread come at same time two object will be created at same time

"""

class DBConnection:
    _instance = None

    def __init__(self):
        # Initialization code
        # For demonstration purposes, we initialize a simple attribute
        self.connection_string = "Your database connection string here"

    @staticmethod
    def get_instance():
        if DBConnection._instance is None:
            DBConnection._instance = DBConnection()
        return DBConnection._instance