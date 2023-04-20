import datetime
from Color import Color

class Offer:
    __id = 0
    __title = ""
    __desc = ""
    __prize = 0
    __owner = ""
    __categories = []
    __createdDate = datetime.datetime.now()
    __modifiedDate = datetime.datetime.now()
    __weight = 0
    __shippingPrize = 0
    __status = "new"
    __mainColor = Color.BLUE



