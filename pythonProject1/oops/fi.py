# class partyAnimal:
#     x=0
#     def party(self):
#         self.x=self.x+1
#         print("so far",self.x)
#
# an=partyAnimal()
# an.party()
# an.party()
# an.party()
# an.party()
class partyAnimal:
    x=0
    def __init__(self):
        print("i am a constructor")
    def party(self):
        self.x=self.x+1
        print("so far",self.x)
    def __del__(self):
        print('i am de',self.x)

an=partyAnimal()
an.party()
an.party()
an.party()
an.party()