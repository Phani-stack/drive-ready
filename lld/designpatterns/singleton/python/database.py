class Database:

    __instance = None

    def __new__(cls, url, password, max_pool_size):
        if (cls.__instance == None):
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, url, password, max_pool_size):
        self.__url = url
        self.__password = password
        self.__max_pool_size = max_pool_size

    def getInstance(self):
        if self.__instance == None:
            self.__instance = Database()

        return self.__instance
