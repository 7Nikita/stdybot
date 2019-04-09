command_list = []


class Command:
    def __init__(self):
        self.__keys = []
        self.description = ''
        command_list.append(self)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, mas):
        for i in mas:
            self.__keys.append(i.lower())

    def process(self):
        pass
