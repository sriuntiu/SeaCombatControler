class OpenFileError:
    pass


class LoadFromFile:
    def __init__(self, sourceName):
        self.__srcName = sourceName

    def __enter__(self):
        self.src = open(self.__srcName, "r")
        print('<<< Загрузка >>>')
        return self

    def __exit__(self, type, values, traceback):
        self.src.close()
        print('<<< Карта загружена успешно >>>')
        return True

    def read(self):
        try:
            buffer = self.src.read()
            print('test')
            return buffer
        except IOError:
            raise OpenFileError

