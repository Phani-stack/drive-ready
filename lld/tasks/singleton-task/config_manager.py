from abc import ABC, abstractmethod


class ConfigManager(ABC):

    def __init__(self):
        self.properties = {}

    @abstractmethod
    def get_configuration(self, key, value_type=None):
        pass

    @abstractmethod
    def set_configuration(self, key, value):
        pass

    @abstractmethod
    def remove_configuration(self, key):
        pass

    @abstractmethod
    def clear(self):
        pass
