students = []

with open("/home/epicman25/code/pyhton-practice/cs50p/practice/file/students.csv") as file:
    for line in file:
        name,house = line.strip().split(',')
        student = {"name":name,"house":house}
        # student["name"] = name
        # student["house"] = house
        students.append(student)
        
def get_name(student):
    return student["name"]
        
for student in sorted(students,key=lambda tt:tt["name"]):
    print(f"{student['name']} is in {student['house']}")