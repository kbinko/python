class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    print(student)    
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError as error:
        print(error)
        return get_student()

if __name__ == "__main__":
    main()
    