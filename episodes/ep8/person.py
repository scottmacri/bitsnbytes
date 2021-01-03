import pickle

class Person:
    
    def __init__(self, f_name, l_name, street, city, state, zip, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        
    def __str__(self):
        return f"{self.l_name}, {self.f_name}"
    
    def greeting(self, message):
        return message
    
def save_person(person, file_path):
    file = open(file_path, "wb")
    pickle.dump(person, file)
    file.close()
    
def read_person(file_name):
    file = open(file_name, 'rb')
    person = pickle.load(file)
    file.close()
    return person

def main():
    person = Person("Joe", "Blow", "124 A st.", "Hickory", "Fl", "44444", "549-987-1245")
    print(person)
    print("Street: ", person.street)
    print("City: ", person.city)
    print("State: ", person.state)
    print("Zip: ", person.zip)
    print("Phone: ", person.phone)
    print("Greeting: ", person.greeting("Hello World!"))
    save_person(person, "./person.dat") # This pickles our object
    saved_person = read_person("./person.dat")
    print("Saved Person: ", saved_person)
    
    
if __name__ == "__main__":
    main()
    