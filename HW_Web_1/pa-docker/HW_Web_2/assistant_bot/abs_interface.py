from abc import abstractmethod, ABCMeta


class UserOutputInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def get_table(self):
        pass


class UserOutput(UserOutputInterface):
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.header = None

    def create_header(self):
        self.header = "\n|" + "-" * 155 + "|"
        self.headers = ["Name", "Phone", "Birthday", "Email", "Notes", "Address"]
        self.columns = "\n|{:^10}|{:^30}|{:^20}|{:^20}|{:^40}|{:^30}|"
        self.header += self.columns.format(*self.headers)
        self.header += "\n|" + "-" * 155 + "|"
        print(self.header)


    def create_table(self):
        for el in self.contact_list:
            line = ""
            columns = "|{:^10}|{:<30}|{:<20}|{:<20}|{:<40}|{:<30}|"
            column = el.split("|")
            line += columns.format(*column)
            line += "\n|" + "-" * 155 + "|"
            print(line)


    def get_table(self):
        UserOutput.create_header(self)
        UserOutput.create_table(self)
        return "Done"

