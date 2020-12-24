from person import Person
import json

def main():
    with open("person_records.json") as file:
        json_data = json.load(file)
        
    toggle = True
    while toggle:
        print("1: Create Record")
        print("2: Exit")
        command = input("Select a Number: ")
        if command == "1":
            print("Create and entry")
            print("")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            person = Person(first_name, last_name)
            for field in vars(person):
                if (field != '_first_name') and (field != '_last_name'):
                    new_field = input(f"Enter {field.replace('_','',1)}: ")
                    setattr(person, field, new_field)
            json_data["person_records"].append(vars(person))
            
            with open("person_records.json", "w") as file:
                json.dump(json_data, file)
        else:
            toggle = False
     
if __name__ == "__main__":
    main()
