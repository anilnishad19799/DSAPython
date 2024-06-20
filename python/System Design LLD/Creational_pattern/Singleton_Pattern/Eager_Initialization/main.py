from DBconnection import DBConnection

# Usage example
if __name__ == "__main__":
    conn_object1 = DBConnection.get_instance()
    conn_object2 = DBConnection.get_instance()

    print(conn_object1 is conn_object2)  # Output: True
    print(conn_object1.connection_string)  # Output: Your database connection string here