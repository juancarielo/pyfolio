class Job():
    def __init__(self, title, description, created, changed, status):
        self.__title = title
        self.__description = description
        self.__created = created
        self.__changed = changed
        self.__stauts = stauts

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title
