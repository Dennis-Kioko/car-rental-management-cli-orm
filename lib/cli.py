from models.car_rental_system_cli import CarRentalSystem
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///car_rental_database.db')
Session = sessionmaker(bind=engine)
session = Session()


from helpers import (
    exit_program,
    add_car,
    get_all_cars,
    find_car_by_id,
    find_car_by_make_and_model,
    update_car,
    delete_car,
    add_customer,
    get_all_customers,
    find_customer_by_id,
    find_customer_by_name,
    update_customer,
    delete_customer,
    register_customer_to_car
)

def main():
    car_rental_system = CarRentalSystem("car_rental_database.db")  
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program(car_rental_system)
        
        elif choice == "1":
            make = input("Enter the car's make: ")
            model = input("Enter the car's model: ")
            year = input("Enter the car's year: ")
            add_car(car_rental_system, make, model, year)
        
        elif choice == "2":
            get_all_cars(car_rental_system)
        
        elif choice == "3":
            car_id = input("Enter the car's ID: ")
            find_car_by_id(car_rental_system, car_id)
        
        elif choice == "4":
            make = input("Enter the car's make: ")
            model = input("Enter the car's model: ")
            find_car_by_make_and_model(car_rental_system, make, model)
        
        elif choice == "5":
            car_id = input("Enter the car's ID: ")
            new_make = input("Enter the new make: ")
            new_model = input("Enter the new model: ")
            new_year = input("Enter the new year: ")
            update_car(car_rental_system, car_id, new_make, new_model, new_year)
        
        elif choice == "6":
            car_id = input("Enter the car's ID: ")
            delete_car(car_rental_system, car_id)
        
        elif choice == "7":
            add_customer(car_rental_system) 
        
        elif choice == "8":
            get_all_customers(car_rental_system)
        
        elif choice == "9":
            customer_id = input("Enter the customer's ID: ")
            find_customer_by_id(car_rental_system, customer_id)
            
        elif choice == "10":
            first_name = input("Enter the customer's first name: ")
            last_name = input("Enter the customer's last name: ")
            find_customer_by_name(car_rental_system, first_name, last_name)
            
        
        elif choice == "11":
            customer_id = input("Enter the customer's ID: ")
            new_first_name = input("Enter the new first name: ")
            new_last_name = input("Enter the new last name: ")
            new_phone_no = input("Enter the new phone number: ")
            update_customer(car_rental_system, customer_id, new_first_name, new_last_name, new_phone_no)

            
        elif choice == "12":
            customer_id = input("Enter the customer's ID: ")
            delete_customer(car_rental_system, customer_id)
        
        elif choice == "13":
            customer_id = input("Enter the customer's ID: ")
            car_id = input("Enter the car's ID: ")
            start_date_str = input("Enter the start date (optional): ")
            end_date_str = input("Enter the end date (optional): ")

            register_customer_to_car(car_rental_system, customer_id, car_id, start_date_str, end_date_str)

        else:
            print("Invalid choice!")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new car")
    print("2. Get all cars")
    print("3. Find car by id")
    print("4. Find car by make and model")
    print("5. Update a car")
    print("6. Delete a car")
    print("7. Add a customer")
    print("8. Get all customers")
    print("9. Find customer by id")
    print("10.Find customer by name")
    print("11.Update a customer")
    print("12.Delete a customer")
    print("13.Register customer to a car")
    
    

if __name__ == "__main__":
    main()
