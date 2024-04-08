# Student Directory 

def view_all(people):
    """Print all details of teachers """
    for person in people:
        for key,value in person.items():
            print(key, value)

def view_by_ethnicity(people, search_ethnicity):
    """
    Loop over list and return all teachers ina subject
    """
    kid = []
    for person in people: # For each teacher
        for key, value in person.items(): # For each attribute
            if key == "ethnicity" and value == search_ethnicity:
                # Add them to our list
                kid.append(person["name"])
    return kid

# Function to add a person and their ethnicity to the dict
def add(name, ethnicity, age):
    students.append({"name": name, "ethnicity" : ethnicity, "age" : age}) 
    return students

def change_age(name, age):
    print()

if __name__ == "__main__":
    # List of students
    students = [{"name" : "Katelyn", "ethnicity" : "Chinese", "age" : "16"},
                {"name" : "Tamsin", "ethnicity" : "Chinese", "age" : "15"}, 
                {"name" : "bob", "ethnicity" : "minion", "age" : "100"}]
    dictionary = {}
    loop = True
    while loop:
        menu = int(input("""
        1.add a student (name, ethnicity, and age)
        2.change their age 
        3.delete a student
        4.list the ethnicities of all the students 
        5.enter an ethnicity and get all students who are that ethnicity
        6.show all users that are over 18 telling them they're considered an adult.
        Enter a number depending on the option: """))
        if menu == 1:
            add_name = input("What name do you want to add in: ")
            add_ethnicity = input("Enter ethnicity you want to add: ")
            add_age = int(input("Enter age of this person: "))
            add(add_name, add_ethnicity, add_age)
            print("Added")
        elif menu == 2:
            # Change students age
            name = input("What name do you want to change the age of: ")
            age = int(input("What age do you want to change it to: "))
            change_age(name, age)
        elif menu == 5:
            ethnicity = input("Ethnicity: ")
            results = view_by_ethnicity(students, ethnicity)
            # Print the results
            for name in results:
                print(name)
        elif menu == 0:
            break
        elif menu == 4:
             view_all(students)
        else:
            print("I don't understand")
            