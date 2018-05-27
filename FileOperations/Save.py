class OpenFileError:
    pass


class SaveToFile:

    def __init__(self, dstName):
        self.__dstName = dstName

    def __enter__(self):
        # С помощью открытия файла на запись очищаем его содержимое
        self.__dstFile = open(self.__dstName, "w")
        self.__dstFile.write('')
        self.__dstFile.close()
        # Дописываем значения в конец поэлементно
        self.__dstFile = open(self.__dstName, "a")
        print('Идет запись карты в файл')

    def __exit__(self, type, values, traceback):

        self.__dstFile.close()
        print('Карта сохранена')
        return True

    def write(self, fout):
        try:
            self.__dstFile.write(fout)
        except IOError:
            raise OpenFileError

