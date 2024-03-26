from models.car_rental_system_cli import CarRentalSystem
from models.car_rental_system_cli import Customer
from datetime import datetime


def exit_program(car_rental_system):
    print("Nice having you🤗")
    exit()
    
def add_car(car_rental_system, make, model, year):
    if not make or not model or not year:
        print("Error: Make, Model, and year are required")
        return
    
    car_rental_system.add_car(make, model, year)
    print("Car added successfully!")

def get_all_cars(car_rental_system):
    cars = car_rental_system.get_all_cars()
    for car in cars:
        print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")

def find_car_by_id(car_rental_system, car_id):
    car = car_rental_system.find_car_by_id(car_id)
    if car:
        print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")
    else:
        print(f"Car with ID {car_id} not found.")

def find_car_by_make_and_model(car_rental_system, make, model):
    car = car_rental_system.find_car_by_name(make, model)
    if car:
        print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")
    else:
        print(f"Car with make '{make}' and model '{model}' not found.")

def update_car(car_rental_system, car_id, new_make=None, new_model=None, new_year=None):
    car_rental_system.update_car(car_id, new_make, new_model, new_year)
    print("Car updated successfully!")

def delete_car(car_rental_system, car_id):
    deleted_car_info = car_rental_system.delete_car(car_id)
    if deleted_car_info:
        car_info, car_id = deleted_car_info
        print(f"Car '{car_info}' with ID '{car_id}' deleted successfully.")
    else:
        print(f"Car with ID '{car_id}' not found. Unable to delete.")
        
    
def add_customer(car_rental_system):
    first_name = input("Enter the customer's first name: ")
    last_name = input("Enter the customer's last name: ")
    phone_no = input("Enter the customer's phone number: ")
    try:
        car_rental_system.add_customer(first_name, last_name, phone_no)
        print("Customer added successfully!")
    except Exception as exc:
        print("Error adding customer: ", exc)

def get_all_customers(car_rental_system):
    customers = car_rental_system.get_all_customers()
    for customer in customers:
        print(f"First Name: {customer.first_name}, Last Name: {customer.last_name}, Phone No: {customer.phone_no}")

def find_customer_by_id(car_rental_system, customer_id):
    customer = car_rental_system.find_customer_by_id(customer_id)
    if customer:
        print(f"Customer ID: {customer.id}")
        print(f"First Name: {customer.first_name}")
        print(f"Last Name: {customer.last_name}")
        print(f"Phone Number: {customer.phone_no}")
    else:
        print(f"Customer with ID {customer_id} not found.")
        
def find_customer_by_name(car_rental_system, first_name, last_name):
    customer = car_rental_system.find_customer_by_name(first_name, last_name)
    if customer:
        print(f"Customer ID: {customer.id}")
        print(f"First Name: {customer.first_name}")
        print(f"Last Name: {customer.last_name}")
        print(f"Phone Number: {customer.phone_no}")
    else:
        print(f"Customer with first name '{first_name}' and last name '{last_name}' not found.")

def update_customer(car_rental_system, customer_id, new_first_name=None, new_last_name=None, new_phone_no=None):
    car_rental_system.update_customer(customer_id, new_first_name, new_last_name, new_phone_no)
    print("Customer updated successfully!")

def delete_customer(car_rental_system, customer_id):
    deleted_customer_info = car_rental_system.delete_customer(customer_id)
    if deleted_customer_info:
        customer_info, customer_id = deleted_customer_info
        print(f"Customer '{customer_info}' with ID '{customer_id}' deleted successfully.")
    else:
        print(f"Customer with ID '{customer_id}' not found. Unable to delete.")
    

def register_customer_to_car(car_rental_system, customer_id, car_id, start_date_str, end_date_str):
    start_date = start_date_str if start_date_str else None
    end_date = end_date_str if end_date_str else None
    car_rental_system.register_customer_to_car(customer_id, car_id, start_date, end_date)
