class Dog:
    tail=1
    tricks=[]
  
    def __init__(self,name,bark):
        self.name=name
        self.bark=bark
    def introduce(self):
        print(self)
        print(f"name is {self.name} and bar is {self.bark}")
D1=Dog("Tom","bho bho")
D2=Dog("Rockey","Golden retriever")
D1.introduce()
D2.introduce()


D1.tricks=[]
D1.tricks.append("Sit")
D2.tricks.append("Stand")
Dog.tricks.append("HandShake")
print(D1.tricks)
print(D2.tricks)