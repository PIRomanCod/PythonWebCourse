'''
Напишіть класи серіалізації контейнерів з даними Python у json, bin файли. 
Самі класи мають відповідати загальному інтерфейсу (абстрактному базовому класу) SerializationInterface.

'''

from abc import abstractmethod, ABCMeta
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def save_data_to_dump(self):
        pass

    @abstractmethod
    def save_data_to_file(self):
        pass

    @abstractmethod
    def load_data_from_dump(self):
        pass

    @abstractmethod
    def load_data_from_file(self):
        pass


class SerializationJson(SerializationInterface):
    # записуємо серіалізований обєкт до змінної
    def save_data_to_dump(self, container):
        serialized_data = json.dumps(container)
        return serialized_data

    # записуємо серіалізований обєкт у файл
    def save_data_to_file(self, filename, container):
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(container, file)

    # повераємо десеріалізований з байт-рядку обєкт
    def load_data_from_dump(self, serialized_data):
        deserialised_data = json.loads(serialized_data)
        return deserialised_data

    # повераємо десеріалізований з файлу обєкт
    def load_data_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            deserialised_data = json.load(file)
            return deserialised_data


class SerializationBin(SerializationInterface):
    # записуємо серіалізований обєкт до змінної
    def save_data_to_dump(self, container):
        serialized_data = pickle.dumps(container)
        return serialized_data

    # записуємо серіалізований обєкт у файл
    def save_data_to_file(self, filename, container):
        with open(filename, 'wb') as file:
            pickle.dump(container, file)

    # повераємо десеріалізований з байт-рядку обєкт
    def load_data_from_dump(self, serialized_data):
        deserialised_data = pickle.loads(serialized_data)
        return deserialised_data

    # повераємо десеріалізований з файлу обєкт
    def load_data_from_file(self, filename):
        with open(filename, 'rb') as read_file:
            container = pickle.load(read_file)
            return container


json_obj = SerializationJson()
bin_obj = SerializationBin()

data = {
    "developer": {
        "name": "Alex",
        "species": "Python", "contacts": [380501234567, 380981234567], "status": True, "adress": (1, 2)
    }
}

filename_bin = "data.bin"
filename_json = "data.txt"

json_obj.save_data_to_file(filename_json, data)
serialised_json = json_obj.save_data_to_dump(data)
print(serialised_json)
deserialised_json = json_obj.load_data_from_dump(serialised_json)
print(deserialised_json)

bin_obj.save_data_to_file(filename_bin, data)
serialised_bin = bin_obj.save_data_to_dump(data)
print(serialised_bin)
deserialised_bin = bin_obj.load_data_from_dump(serialised_bin)
print(deserialised_bin)
