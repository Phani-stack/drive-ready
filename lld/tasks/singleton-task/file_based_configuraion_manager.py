from config_manager import ConfigManager


class FileBasedConfigurationManager(ConfigManager):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__()
            self._initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls):
        cls._instance = None

    def get_configuration(self, key, value_type=None):
        value = self.properties.get(key)
        if (value_type == None):
            return value
        return value_type(value)


    def set_configuration(self, key, value):
        self.properties[key] = value

    def remove_configuration(self, key):
        self.properties.pop(key)

    def clear(self):
        self.properties.clear()
