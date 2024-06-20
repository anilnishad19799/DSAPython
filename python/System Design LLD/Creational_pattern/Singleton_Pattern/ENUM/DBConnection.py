""" By default enum are created singleton """
import enum

class DBConnection(enum.Enum):
    INSTANCE = "Your database connection instance"