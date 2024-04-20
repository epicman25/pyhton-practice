class Student:
    def __init__(self,name,house) -> None:
        if not name:
            raise ValueError("Missing name")
        if house not in ["tt"]:
            raise ValueError("Invalid House")
        self.name = name 
        self.house = house
 

    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    


def main():
    student=Student.get()
    # print(f"{student.name} from {student.house}")
    # student.house = "jasdkfjasd"
    print(student)
    



if __name__ == '__main__':
    main()