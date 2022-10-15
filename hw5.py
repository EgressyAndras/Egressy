class Team():
    def __init__(self,name,munkahely,szerepkor):
        self._name = name
        self._munkahely = munkahely
        self._szerepkor = szerepkor
        print("--Developer létrehozva--")
        print(f"{self.name} a {self.munkahely}-en dolgozik {self.szerepkor} szerepkorben ")
    @property
    def name(self):
        return self._name

    @property
    def munkahely(self):
        return self._munkahely

    @property
    def szerepkor(self):
        return self._szerepkor
    @name.setter
    def name(self, nev):
        self._name = nev
    @munkahely.setter
    def munkahely(self,hely):
        self._munkahely = hely
    @szerepkor.setter
    def szerepkor(self,szerep):
        self._szerepkor = szerep

ember = []
nevek = []

ember.append(Team("Ricsi","SolArch","Frontend"))
ember.append(Team("Angéla","Zerteng","Tesztelő"))
ember.append(Team("Peti","KefERP","Backend"))
ember.append(Team("Éva","KefERP","Frontend"))
print("")
a=""
for i in range(0,len(ember)):
    for j in range(0,len(ember)):
        if(ember[i].munkahely == ember[j].munkahely and ember[i].name != ember[j].name ):
            a=ember[i].munkahely
    if (ember[i].munkahely==a):
        nevek.append(ember[i].name)
print(f"{nevek[0]} és {nevek[1]} dolgoznak egy projekten")
input("press any key to continue...")
