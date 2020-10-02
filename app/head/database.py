import pickle
import os
import datetime
from ..globals import FUELS_FOLDER


class Database:
    ###########################     FUELS   ########################################

    @staticmethod
    def save_fuel(fuel):
        """
        :param : fuel <Fuel object>
        :return : None
        Otrzymuje paliwo <obiekt Fuel>,a nastepnie zapisuje go w jego folderze (odnalezionym lub
        stworzonym).
        """
        name = fuel.name
        path = '%s/%s' % (FUELS_FOLDER, name)
        if not os.path.exists(path):
            os.mkdir(path)
        path = '%s/%s' % (path, name)
        with open(path, 'wb') as file:
            pickle.dump(fuel, file)

    @staticmethod
    def load_fuel(f_name):
        """
        :param f_name: <string>
        :return : <fuel object> or False
        Otrzymuje nazwę paliwa <string>, przeszukuje bazę danych i
        zwraca paliwo <obiekt Fuel> albo <False> jesli nie znaleziono.
        """
        path = '%s/%s/%s' % (FUELS_FOLDER, f_name, f_name)
        if os.path.exists(path):
            with open(path, 'rb') as file:
                return pickle.load(file)
        else:
            return False

    def edit_fuel(self, fuel):
        """
        :param fuel: <obiekt Fuel>
        :return None:
        Wyszukuje paliwo po nazwie pobranej z <obiekt Fuel>, następnie usuwa je i zapisuje
        na nowo.
        """
        name = fuel.name
        if self.is_fuel(name):
            old_fuel = self.load_fuel(name)
            fuel.save_date = old_fuel.save_date
            fuel.save_time = old_fuel.save_time
            path = '%s/%s/%s' % (FUELS_FOLDER, name, name)
            os.remove(path)
        self.save_fuel(fuel)

    @staticmethod
    def remove_fuel(f_name):
        """
        :param f_name: <string>
        :return: None
        Wyszukuje folder paliwa po nazwie <string>, skanuje,
        usuwa wszystkie elementy, a nastepnie sam folder.
        """
        path = '%s/%s' % (FUELS_FOLDER, f_name)
        files = os.listdir(path)
        for file in files:
            file_path = '%s/%s' % (path, file)
            os.remove(file_path)
        os.rmdir(path)

    @staticmethod
    def is_fuel(f_name):
        """
        :param f_name: <string>
        :return: True or False
        Wyszukuje plik paliwa < .bat> po nazwie <string>,
        następnie zwraca True jeśli znajdzie, False jeśli nie.
        """
        path = '%s/%s/%s' % (FUELS_FOLDER, f_name, f_name)
        if os.path.exists(path):
            return True
        else:
            return False

    @staticmethod
    def get_fuels_list():
        """
        :return: lista paliw <list>
        Zwraca wszystkie nazwy wszystkich folderów paliw.
        """
        return os.listdir(FUELS_FOLDER)


    ##############################  SURVEYS #########################################

    def save_survey(self, f_name, survey):
        """
        :param f_name: <string>
        :param survey: <obiekt Survey>
        :return: None
        Dodaje do <obiekt Survey> czas i datę zapisu. Następnie:
            a) jeśli nie istnieje plik pomiarów:
                - nadaje <obiektowi Survey> id = 0
            b) jeśli plik istnieje:
                - ładuje pomiary
                - nadaje id nowemu pomiarowi
                - dodaje pomiar do listy
            Zapisuje listę pomiarów jako plik < .bin>
        """
        path = '%s/%s/%s' % (FUELS_FOLDER, f_name, survey.type)
        if not os.path.exists(path):
            surveys = [survey]
        else:
            surveys = self.load_surveys(f_name, survey.type)
            surveys.append(survey)
        with open(path, 'wb') as file:
            pickle.dump(surveys, file)

    @staticmethod
    def load_surveys(f_name, type):
        path = '%s/%s/%s' % (FUELS_FOLDER, f_name, type)
        if os.path.exists(path):
            with open(path, 'rb') as file:
                return pickle.load(file)
        else:
            return False

    def remove_survey(self, f_name, s_type, s_id):
        surveys = self.load_surveys(f_name, s_type)
        surveys.pop(s_id)
        path = '%s/%s/%s' % (FUELS_FOLDER, f_name, s_type)
        with open(path, 'wb') as file:
            pickle.dump(surveys, file)

    def edit_survey(self, f_name, old_s_type, old_s_id, new_survey):
        self.remove_survey(f_name, old_s_type, old_s_id)
        self.save_survey(f_name, new_survey)
