from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.exc import IntegrityError


Base = declarative_base()


# Define data model
class Car(Base):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    
    rentals = relationship("Rental", back_populates="car")
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_no = Column(Integer, unique=True, nullable=False)
    
    rentals = relationship("Rental", back_populates="customer")

class Rental(Base):
    __tablename__ = 'rentals'
    
    id = Column(Integer, primary_key=True, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    
    customer = relationship("Customer", back_populates="rentals")
    car = relationship("Car", back_populates="rentals")

    __table_args__ = (
        UniqueConstraint('customer_id', 'car_id', name='_customer_car_uc'),
    )
    

# Set up the database connection:    
class CarRentalSystem:
    
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
        
    # Method to register a customer to a car
    def register_customer_to_car(self, customer_id, car_id, start_date=None, end_date=None):
        try:
            if start_date:
                start_date = datetime.strptime(start_date, '%d/%m/%Y')
            if end_date:
                end_date = datetime.strptime(end_date, '%d/%m/%Y')
        except ValueError:
            print("Error: Invalid date format. Please use the format DD/MM/YYYY.")
            return False

        existing_rental = self.session.query(Rental).filter_by(customer_id=customer_id).first()

        if existing_rental:
            print("Error: Customer is already registered to a car")
            return False

        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if not customer:
            print(f"Error: Customer with ID '{customer_id}' not found")
            return False

        car = self.session.query(Car).filter_by(id=car_id).first()
        if not car:
            print(f"Error: Car with ID '{car_id}' not found")
            return False

        try:
            rental = Rental(
                start_date=start_date,
                end_date=end_date,
                customer_id=customer_id,
                car_id=car_id
            )
            self.session.add(rental)
            self.session.commit()

            print(f"Customer '{customer.first_name} {customer.last_name}' (ID: {customer_id}) successfully added to car '{car.make} {car.model}' (ID: {car_id})")
            return True

        except IntegrityError:
            self.session.rollback()
            print("Error: Integrity constraint violation - Customer is already registered to a car")
            return False

        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
            return False

# CRUD methods for car:
    def add_car(self, make, model, year):
        if not make or not model or not year:
            print("Error: Make, Model and year are required")
            
        # Check if a car with the given make and model already exists
        existing_car = self.session.query(Car).filter_by(make=make, model=model, year=year).first()
        if existing_car:
            print(f"A car with make '{make}', model '{model}', and year '{year}' already exists!")
            return
        
        car = Car(make=make, model=model, year=year)
        
        try:
            self.session.add(car)
            self.session.commit()
            return True
            # print(f"{make} {model} Added Successfully")
            
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
            return False
    
    def get_all_cars(self):
        return self.session.query(Car).all()
    
    def find_car_by_id(self, car_id):
        return self.session.query(Car).filter_by(id=car_id).first()
    
    def find_car_by_name(self, make, model):
        car = self.session.query(Car).filter_by(make=make, model=model).first()
        if car:
            return car
        else:
            print(f"Car with make '{make}' and model '{model}' not found.")
            return None
    
    def update_car(self, car_id, new_make=None, new_model=None, new_year=None):
        # Find the car by its ID
        car = self.session.query(Car).filter_by(id=car_id).first()
        if not car:
            print(f"Car with ID '{car_id}' not found. Unable to update.")
            return
        
        if new_make is not None:
            car.make = new_make
        if new_model is not None:
            car.model = new_model
        if new_year is not None:
            car.year = new_year
            
        try:
            self.session.commit()
            print(f"Car with ID '{car_id}' updated successfully.")
        
        except Exception as e:
            self.session.rollback()
            print(f"Error updating car:{e}")
    
    
    def delete_car(self, car_id):
    # Find the car by its ID
        car = self.session.query(Car).filter_by(id=car_id).first()
        if not car:
            print(f"Car with ID '{car_id}' not found. Unable to delete.")
            return None
    
    # Store the make and model of the car before deleting
        car_info = f"{car.make} {car.model}"
    
        try:
            self.session.delete(car)
            self.session.commit()
            return car_info, car_id
        
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting car: {e}")
            return None

    
# CRUD methods for customer
    def add_customer(self, first_name, last_name, phone_no):
        if not first_name or not last_name or not phone_no:
            print("Error: First Name, Last Name and phone are required!")
            
            # Check if a customer with the given phone number already exists
        existing_customer = self.session.query(Customer).filter_by(phone_no=phone_no).first()
        
        if existing_customer:
            print(f"Customer with phone number {phone_no} already exists!")
            return
        
        customer = Customer(first_name=first_name, last_name=last_name, phone_no=phone_no)
    
        try:
            self.session.add(customer)
            self.session.commit()
            print(f"{first_name} {last_name} Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
                        
    
    def get_all_customers(self):
        return self.session.query(Customer).all()
    
    def find_customer_by_id(self, customer_id):
        return self.session.query(Customer).filter_by(id=customer_id).first()
    
    def find_customer_by_name(self, first_name, last_name):
        customer = self.session.query(Customer).filter_by(first_name=first_name, last_name=last_name).first()
        if customer:
            return customer
        else:
            print(f"Customer with first name '{first_name}' and last '{last_name}' not found.")
            return None
        
    def update_customer(self, customer_id, new_first_name=None, new_last_name=None, new_phone_no=None):
        # Find the customer by its ID
        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if not customer:
            print(f"Customer with ID '{customer_id}' not found. Unable to update")
            return

        # Update customer attributes if new values are provided
        if new_first_name is not None:
            customer.first_name = new_first_name
        if new_last_name is not None:
            customer.last_name = new_last_name
        if new_phone_no is not None:
            customer.phone_no = new_phone_no

        try:
            self.session.commit()
            print(f"Customer with ID '{customer_id}' updated successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error updating customer: {e}")
        
    
    def delete_customer(self, customer_id,):
        # Find the customer by its ID
        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if not customer:
            print(f"Customer with ID '{customer_id}' not found. Unable to delete.")
            return
        # Store the name of the customer before deleting
        customer_name = f"{customer.first_name} {customer.last_name}"
        try:
            # Delete the customer
            self.session.delete(customer)
            self.session.commit()
            print(f"Customer '{customer_name}' with ID '{customer_id}' deleted successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting customer: {e}")

    
    def get_customers_in_a_car(self, car_id):
        car = self.session.query(Car).filter_by(id=car_id).first()

        if car:
            return car.customers
        else: 
            print("Car not found")
            return []
        
    
        # Method to register a customer to a car
    


# Inside the CarRentalSystem class
# def register_customer_to_car(self, session, customer_id, car_id, start_date=None, end_date=None):
#     try:
#         # Parse date strings into datetime objects if provided
#         start_date = datetime.strptime(start_date, '%d/%m/%Y') if start_date else None
#         end_date = datetime.strptime(end_date, '%d/%m/%Y') if end_date else None
#     except ValueError:
#         print("Error: Invalid date format. Please use the format DD/MM/YYYY.")
#         return False

#     existing_rental = session.query(Rental).filter_by(customer_id=customer_id).first()

#     if existing_rental:
#         print("Error: Customer is already registered to a car")
#         return False

#     customer = session.query(Customer).filter_by(id=customer_id).first()
#     if not customer:
#         print(f"Error: Customer with ID '{customer_id}' not found")
#         return False

#     car = session.query(Car).filter_by(id=car_id).first()
#     if not car:
#         print(f"Error: Car with ID '{car_id}' not found")
#         return False

#     try:
#         rental = Rental(
#             start_date=start_date,
#             end_date=end_date,
#             customer_id=customer_id,
#             car_id=car_id
#         )
#         session.add(rental)
#         session.commit()

#         print(f"Customer '{customer.first_name} {customer.last_name}' (ID: {customer_id}) successfully added to car '{car.make} {car.model}' (ID: {car_id})")
#         return True

#     except IntegrityError:
#         session.rollback()
#         print("Error: Integrity constraint violation - Customer is already registered to a car")
#         return False

#     except Exception as e:
#         session.rollback()
#         print(f'Error: {e}')
#         return False


        
if __name__ == '__main__':
    
    car_rental_system = CarRentalSystem("car_rental_database.db")
    
        # Add a car
    car_rental_system.add_car("Toyota", "Camry", 2022)
    car_rental_system.add_car("Toyota", "Corolla", 2020)
    car_rental_system.add_car("Aston Martin", "DBX", 2016)
    car_rental_system.add_car("Audi", "A4 Avant", 2015)
    car_rental_system.add_car("BMW", "X6", 2023)
    car_rental_system.add_car("Chevrolet", "Corvette", 2021)
    car_rental_system.add_car("Honda", "Elegance", 2019)
    car_rental_system.add_car("Ford", "Mustang", 2014)
    
    
        # find_car_by_id
    # car_id = 2
    # car = car_rental_system.find_car_by_id(car_id)
    
    # if car:
    #     print(f"Car ID: {car.id}")
    #     print(f"Make: {car.make}")
    #     print(f"Model: {car.model}")
    #     print(f"Year: {car.year}")
    
    # else:
    #     print("Car not found")
    
        #find_car_by_name
    # car = car_rental_system.find_car_by_name("BMW", "X6")
    # if car:
    #     print(f"Car found: {car.make} {car.model} {car.year}")
    # else:
    #     print("Car not found.")
    
            # get all cars
    # all_cars = car_rental_system.get_all_cars()
    # print("All cars:")
    
    # for car in all_cars:
    #     print(f"Make: {car.make}, Model:{car.model}, Year:{car.year}" )
    
        
#         # update car
# car_rental_system.update_car(car_id=11, new_make="Subaru", new_model="Edith", new_year=2023)

# #  Check if the car details were updated successfully
# updated_car = car_rental_system.find_car_by_id(11)

# if updated_car:
#     print(f"Updated Car Details:")
#     print(f"ID: {updated_car.id}")
#     print(f"Make: {updated_car.make}")
#     print(f"Model: {updated_car.model}")
#     print(f"Year: {updated_car.year}")
# else:
#     print("Car not found.")

        # Delete_car
    # car_rental_system.delete_car(car_id=1)

    
        # Add a customer
    car_rental_system.add_customer("John", "Doe", "0734576890")
    car_rental_system.add_customer("Maru", "Junior", "0753728282")
    car_rental_system.add_customer("Dennis", "Kioko", "0764544543")
    car_rental_system.add_customer("Doris", "Kerubo", "0732411135")
    car_rental_system.add_customer("Allen", "Shamrock", "0798756324")
    car_rental_system.add_customer("Mulei", "Archy", "0700453678")
    car_rental_system.add_customer("Mutua", "James", "0700453670")
    car_rental_system.add_customer("Jane", "Ruto", "0700543678")
    
    
        # find_customer_by_id
    # customer_id = 2
    # customer= car_rental_system.find_customer_by_id(customer_id)
    
    # if customer:
    #     print(f"Customer ID: {customer.id}")
    #     print(f"First name: {customer.first_name}")
    #     print(f"Last name: {customer.last_name}")
    #     print(f"Phone no: {customer.phone_no}")
    
    # else:
    #     print("Customer id not found")
        
        
        # get all customers
    # all_customers = car_rental_system.get_all_customers()
    # print("All customers:")
    
    # for customer in all_customers:
    #     print(f"First Name: {customer.first_name}, Last name:{customer.last_name}, Phone No:{customer.phone_no}")
    
        
        # Find Customer by name
    # first_name = "John"
    # last_name = "Kamau"
    
    # customer = car_rental_system.find_customer_by_name(first_name, last_name)
    
    # if customer:
    #     # Print customer information
    #     print(f"Customer ID: {customer.id}")
    #     print(f"First name: {customer.first_name}")
    #     print(f"Last name: {customer.last_name}")
    #     print(f"Phone no: {customer.phone_no}")
    # else:
    #     print("Customer not found")
    
            # update customer
# car_rental_system.update_customer(customer_id=14, new_first_name="Mutua", new_last_name="Kilonzo", new_phone_no="0744444444")

# updated_customer = car_rental_system.find_customer_by_id(14)
# if updated_customer:
#     print(f"Updated Customer Details:")
#     print(f"ID: {updated_customer.id}")
#     print(f"First Name: {updated_customer.first_name}")
#     print(f"Last Name: {updated_customer.last_name}")
#     print(f"Phone Number: {updated_customer.phone_no}")

# else:
#     print("Customer not found.")

    #     # Delete Customer by id
    # car_rental_system.delete_customer(2)

    
    
        # Register customers to a car
    car_rental_system.register_customer_to_car(4, 3, start_date="01/01/2024", end_date="31/12/2024")
    car_rental_system.register_customer_to_car(2, 1, start_date="01/02/2024", end_date="28/02/2024")

