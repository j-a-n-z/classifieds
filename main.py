from classes.Color import Color
from classes.Portal import Portal
from classes.Human import Human
from classes.Offer import Offer
from classes.Category import Category

janek = Human("Jan", "Zastawa", 73, 185, "male")
mateusz = Human("Mateusz", "Kowalski", 68, 170, "male")

catMusic = Category("Music", "Music general")
catInstruments = Category("Instruments", "Music instruments")
catPlayers = Category("Players", "Where music can be played")

portalMallegro = Portal("Mallegro", "mallegro.com", [janek, mateusz])

# print(portalMallegro.getDomain())

# for owner in portalMallegro.getOwners():
#     owner.introduce()

# print(portalMallegro.getOwners())

piano = Offer("Grand Piano Kawai B7-82", "Best grand piano out there", 100000, [catMusic, catInstruments], janek, 300, 200)

gramophone = Offer("AudioRetro Gramophone XD-700", "Looking very nice, retro graophone", 900, [catMusic], mateusz, 17, 20)

gramophone.status = "used"

print(piano.id)
print(piano.title)
print(piano.desc)
print(piano.price)
print(piano.owner.getFirstName())
print(piano.categories)

for category in piano.categories:
    print(category.title)

print(piano.createdDate)
print(piano.modifiedDate)
print(piano.weight)
print(piano.shippingPrice)
print(piano.status)
# piano.mainColor = Color.RED
print(piano.mainColor, "zobaczmy kolor")
print(Color)

for attribute, value in gramophone.__dict__.items():
    print(attribute, value)



# TODO

# HOMEWORK wymyślić co zamodelować w postaci klas


class Janek:
    # @staticmethod
    def dupa(self):
        print("dupa")

nowyJanek = Janek()
nowyJanek.dupa()
