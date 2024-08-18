from abc import ABC, abstractmethod

# Abstract Base Class
class Command(ABC):
    RUN_METHOD = "run"

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
