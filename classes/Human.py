class Human:
    __firstName = ""
    __lastName = ""
    __weight = 0
    __height = 0
    __sex = ""

    def __init__(self, firstName, lastName, weight, height, sex):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__weight = weight
        self.__height = height
        self.__sex = sex

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getFirstName(self):
        return self.__firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def getLastName(self):
        return self.__lastName

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def introduce(self):
        print("Hi!, my name is " + self.__firstName + " " + self.__lastName + ", my weight is " + str(self.__weight) + ", my height is " + str(self.__height) + " and my sex is " + self.__sex)

