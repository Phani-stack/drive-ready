from abc import ABC, abstractmethod

class Processable(ABC):
    @abstractmethod
    def process(self): ...
