from . import ABC, abstractmethod

class Button(ABC):
    @abstractmethod

    def is_pressed() -> bool:
        pass

    def press() -> bool:
        pass