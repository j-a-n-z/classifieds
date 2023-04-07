class Portal:
    __name =""
    __domain = ""
    __owners = []
    def __init__(self, name, domain, owners):
        self.__name = name
        self.__domain = domain
        self.__owners = owners

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDomain(self, domain):
        self.__domain = domain

    def getDomain(self):
        return self.__domain

    def setOwners(self, owners):
        self.__owners = owners

    def getOwners(self):
        return self.__owners


