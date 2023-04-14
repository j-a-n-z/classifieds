
from classes.Portal import Portal
from classes.Human import Human


janek = Human("Jan", "Zastawa", 73, 185, "male")
mateusz = Human("Mateusz", "Kowalski", 68, 170, "male")


portalMallegro = Portal("Mallegro", "mallegro.com", [janek, mateusz])

print(portalMallegro.getDomain())

for owner in portalMallegro.getOwners():
    owner.introduce()

print(portalMallegro.getOwners())
#dodaliśmuy klasę human, teraz musimy dodać właściceli do portalu
