import random
class Hat:
    
    houses = ["Gryyfindor","Hufflepuff","Ravenclaw","Slytherin"]
    
    @classmethod
    def sort(cls,name):
        print(name, "is in",random.choice(cls.houses))
        
Hat.sort("Harry")