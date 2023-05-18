class Category:
    __title = ""
    __desc = ""

    def __init__(self, title, desc):
        self.__title = title
        self.__desc = desc

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def desc(self):
            return self.__desc

    @desc.setter
    def desc(self, value):
            self.__desc = value