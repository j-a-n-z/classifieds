
from classes.Portal import Portal
from classes.Human import Human
from classes.Offer import Offer

janek = Human("Jan", "Zastawa", 73, 185, "male")
mateusz = Human("Mateusz", "Kowalski", 68, 170, "male")


portalMallegro = Portal("Mallegro", "mallegro.com", [janek, mateusz])

print(portalMallegro.getDomain())

for owner in portalMallegro.getOwners():
    owner.introduce()

print(portalMallegro.getOwners())

piano = Offer("Grand Piano Kawai B7-82", "Najepsze pianino dostępne na rynku.", 100000, janek, 300, 200)

print(piano.getId())

# TODO rozwizać problem z generowniem ID w Tools
# TODO zrobić getery i setery do ogłoszenia i stsorzyć pierwsze ogłoszenia
