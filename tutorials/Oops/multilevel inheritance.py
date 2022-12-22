#oops work with MRO - method revolution order
class ElectronicDevice:
    gadgets = 2
    def printInfo(self):
        print(f"Electronic devices are {self.gadgets} and this execute in ElectronicGadget")

class PocketGadget(ElectronicDevice):
    gadgets = 4
    def printInfo(self):
        print(f"PocketGadgets are {self.gadgets} and this execute in PocketGadget")

class phone(PocketGadget):
    # gadgets = 2
    # def printInfo(self):
    #     print(f"no of phones are {self.gadgets} and this execute in phone")
    pass


harry = phone()
harry.printInfo()#harry cant find object in phone class so harry going in PocketGadget class and there he find attribute that he want.