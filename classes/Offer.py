from classes.Color import Color
from classes.Tools import Tools
from datetime import datetime

class Offer:
    # __id = 0
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

    def __init__(self, title, desc, price, categories, owner, weight, shippingPrice):
        self.__id = Tools.generateId()
        self.__title = title
        self.__desc = desc
        self.__price = price
        self.__categories = categories
        self.__owner = owner
        self.__weight = weight
        self.__shippingPrice = shippingPrice

    @property
    def id(self):
        return self.__id

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value):
        self.__categories = value

    @property
    def createdDate(self):
        return self.__createdDate

    @createdDate.setter
    def createdDate(self, value):
        self.__createdDate = value

    @property
    def modifiedDate(self):
        return self.__modifiedDate

    @modifiedDate.setter
    def modifiedDate(self, value):
        self.__modifiedDate = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = value

    @property
    def shippingPrice(self):
        return self.__shippingPrice

    @shippingPrice.setter
    def shippingPrice(self, value):
        if value < 0:
            raise ValueError("Shipping price cannot be negative.")
        self.__shippingPrice = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def mainColor(self):
        return self.__mainColor

    @mainColor.setter
    def mainColor(self, value):
        if not isinstance(value, Color):
            raise ValueError("Main color must be a Color enum value.")
        self.__mainColor = value
