# Usage example

from DBConnection import DBConnection
if __name__ == "__main__":
    conn_object1 = DBConnection.INSTANCE
    conn_object2 = DBConnection.INSTANCE

    print(conn_object1 is conn_object2)  # Output: True
    print(conn_object1.value)  # Output: Your database connection instance