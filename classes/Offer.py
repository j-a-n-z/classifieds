from classes.Color import Color
from classes.Tools import Tools
from datetime import datetime

class Offer:
    __id = 0
    __title = ""
    __desc = ""
    __price = 0
    __owner = ""
    __categories = []
    __createdDate = datetime.now()
    __modifiedDate = datetime.now()
    __weight = 0
    __shippingPrice = 0
    __status = "new"
    __mainColor = Color.BLUE

    def __init__(self, title, desc, price, owner, weight, shippingPrice):
        self.__id = 123

    def getId(self):
        return self.__id

print(Tools.generateId(self))
