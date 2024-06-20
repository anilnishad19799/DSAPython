class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialization code
        # For demonstration purposes, we initialize a simple attribute
        self.connection_string = "Your database connection string here"

    @staticmethod
    def get_instance():
        return DBConnection()