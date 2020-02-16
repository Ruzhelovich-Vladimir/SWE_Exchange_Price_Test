"""
Автоматизация процесса проверки обмена по ценам
автор: Ружелович Владимир
Версия: 1.0
"""

import os


class ControlPrice:
    """
    Клласс котнтроля консистентныз данных по ценообразованию
    """
    __support_type = [".xml"]

    __slots__ = [
        "__work_path_name", "__db_dir_name", "__db_path"
    ]
    # Каталог базы данных

    def __init__(self, work_path_name="."):
        """
        Определение атрибутов класса
        """
        self.__work_path_name = work_path_name  # Рабочий каталог
        self.__db_dir_name = os.path.abspath(work_path_name) # Каталог базы данных
        # Путь к файлу базы данных
        self.__db_path = os.path.join(self.__db_dir_name, "tmp.sqlite3")

        # Загружаем файлы в базу данных SQLite
        self.__load_files_to_sqlite()

    def __get_list_file(self):
        """
        :return: Список файлов
        """
        return [os.path.join(self.__work_path_name, elem)
                for elem in os.listdir(self.__work_path_name)
                if os.path.isfile(os.path.join(self.__work_path_name, elem))
                and elem[-4:] in self.__support_type]

    def __load_files_to_sqlite(self):
        """
        загружает файлы в базу данных
        :return:
        """

        # Генерирую список файлов
        files_list = self.__get_list_file()
        # Перебираем все файлы
        for source in files_list:
            self.__load_file_to_sqllite(source)
            break

    def load_file_to_sqllite(self, file_name):

        print("Загружаем файл: %s ..." % file_name)

        load_file = file_name
        db_path = self.__db_dir_name

        sqlite3

if __name__ == "__main__":
    # 1. Загрузка файлов в базу данных
    CP = ControlPrice(
        "C:\\Users\\Vladimir\\Desktop\\SWE_Exchange_Price_Test\\files")
