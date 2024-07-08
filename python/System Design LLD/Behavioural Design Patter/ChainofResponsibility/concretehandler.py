class InfoLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print(f"INFO: {message}")

class DebugLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print(f"DEBUG: {message}")

class ErrorLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print(f"ERROR: {message}")
