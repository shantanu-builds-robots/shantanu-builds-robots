#import
import datetime
import sqlite3
# Connect to database
conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()


# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cars (
        Car_id INTEGER ,
        Name Varchar,
        Brand TEXT,
        Model TEXT,
        Year INTEGER,
        Available TEXT,
        Return TEXT,
        Rent REAL
    )
''')
cursor.execute("DELETE FROM Cars")
# Insert some cars
cursor.executemany('''
    INSERT INTO Cars (Car_id,Name ,Brand, Model, Year, Available, Return,Rent)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''',  [
    (100,"Puspa","Toyota", "Camry", 2022, "Yes","No", 5000.0),
    (101,"Shrivalli","Honda", "Civic", 2021,"No","Yes", 5000.0),
    (102,"Mahesh Babu","Ford", "Mustang", 2023,"Yes","No", 15000.0),
    (103,"Rowdy","Ferrari","SF90 Stradale", 2000,"No","Yes", 15000.0),
    (104,"Thalapati","Ferrari","SF90 Spider" ,2025,"Yes","No", 15000.0),
    (105,"Bhavani","BMW","1 Series",2000 ,"No","Yes", 14000.0),
    (106,"Puspa","BMW"," 2 Series ",2001,"Yes","No", 13000.0),
    (107,"Shrivalli","BMW","Macan",2002,"No","Yes", 12000.0),
    (108,"Mahesh Babu","Porsche","718 Cayman",2003 , "Yes","No", 11000.0), 
    (109,"Rowdy","Lamborghini" ,"Revuelto",2004,"No","Yes", 10000.0), 
    (110,"Thalapati","Lamborghini","Countach LPI 800-4",2025 ,"Yes","No", 9000.0),
    (111,"Bhavani","Tesla","Model S",1999,"Yes","No",8000.0),
    (112,"Allu Arjun","Tesla", "Model 3",1998,"No","Yes", 7000.0),  
    (113,"Allu Arjun","Mustang", "GT390",1997,"Yes","No", 6000.0), 
    (114,"Allu Arjun","Mustang","GT",1999,"No","Yes", 5000.0),
    (115,"Samantha","BMW","X5",2023,"Yes","No", 16000.0),
    (116,"Nagarjuna","Tesla","Model v", 2024,"No","Yes", 15000.0),
    (117,"Dhanush","Audi","A8",2023,"Yes","No", 14000.0 ),
    (118,"Dhanush","Mercedes-Benz","S-Class",1999,"No","Yes",13000.0),
    (119,"Puspa","Lexus","LS 500",2000,"Yes","No", 12000.0),
    (120,"Yash","Porsche","Panamera",1998,"No","Yes", 11000.0),
    (121,"Yash","Land Rover","Range Rover",1997,"Yes","No", 5000.0),
    (122,"Yash","Cadillac","Escalade",1996,"No","Yes", 6000.0),
    (123,"Yash","Jaguar","F-Type",2023,"Yes","No",7000.0),
    (124,"Yash","Maserati","Quattroporte",2008,"No","Yes", 8000.0),
    (125,"Yash","Mercedes","10",2000,"Yes","No", 9000.0),
    (126,"Allu Arjun","Mercedes","t29",2001,"No","Yes", 10000.0)

 ])

conn.commit()

# to store customer logins
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
# to store history
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rental_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        brand TEXT,
        model TEXT,
        transmission TEXT,
        rental_date TEXT,
        return_date TEXT,
        days INTEGER,
        rate REAL
    )
''')

#classes
# Vehicle 
class Vehicle():
    def __init__(self,brand,model,year,rate,total_cost):
        self.brand=brand
        self.model=model
        self.year=year
        self.rate=rate
        self.total_cost=total_cost

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

# cars list
cars = [
    Car("Toyota", "Camry", 2022),  
    Car("Honda", "Civic", 2021),
    Car("Ford", "Mustang", 2023),
    Car("Ferrari","SF90 Stradale", 2000),
    Car("Ferrari"," SF90 Spider" ,2025),
    Car("BMW","1 Series",2000 ),
    Car("BMW"," 2 Series ",2001),
    Car("BMW","Macan",2002),
    Car("Porsche","718 Cayman",2003), 
    Car("Lamborghini" ,"Revuelto",2004), 
    Car("Lamborghini","Countach LPI 800-4",2025),
    Car("Tesla", "Model S",1999),
    Car("Tesla", "Model 3",1998),  
    Car("Mustang", "GT390",1997), 
    Car("Mustang","GT",1996),
    Car("BMW","X5",2023),
    Car("Tesla"," Model v", 2024),
    Car("Audi","A8",2023 ),
    Car("Mercedes-Benz"," S-Class",1999),
    Car("Lexus","LS 500",2000),   
    Car("Porsche"," Panamera",1998),
    Car("Land Rover","Range Rover",1997),
    Car("Cadillac","Escalade ",1996),
    Car("Jaguar","F-Type",2023),
    Car("Maserati","Quattroporte",2023),
    Car("Mercedes","10",2000),
    Car("Mercedes"," t29",2001)
]     
class Admin:
    def __init__(self, name):
        self.name = name 
        #  menu for admin to select options
    def admin_menu(self):
        print(f"\nWelcome Admin: {self.name}")
        while True:
            # Admin actions 
            print("Admin Menu:")
            print("1. Add Car")
            print("2. Remove Car")
            print("3. View data")
            print("4. Logout")
            choice = input("Select option: ").strip()
# adding car
            if choice == '1':
                    brand = input("Brand: ").strip()
                    model = input("Model: ").strip()
                    year = input("Year: ").strip()
                    rate = float(input("Rate per day: "))
                    transmission = input("Transmission (Automatic/Manual): ").strip()
                    cursor.execute("SELECT MAX(Car_id) FROM Cars")
                    last_id = cursor.fetchone()[0] or 99  # Start from 100 if table is empty
                    new_id = last_id + 1
                    cursor.execute('''
                        INSERT INTO Cars (Car_id, Name, Brand, Model, Year, Available, Return, Rent)
                        VALUES (?, ?, ?, ?, ?, 'Yes', 'No', ?)
                        ''', (new_id, "AddedByAdmin", brand, model, int(year), rate))
                    conn.commit()
                    print(f"Added {brand} {model} ({transmission}) of {year} to the system. Rate per day ₹{rate}.")
# removing car
            elif choice == '2':
                    brand = input("Brand: ").strip()
                    model = input("Model: ").strip()
                    year = input("Year: ").strip()
                    transmission = input("Transmission (Automatic/Manual): ").strip()
                    cursor.execute('''
                        DELETE FROM Cars
                        WHERE Brand = ? AND Model = ? AND Year = ?
                        ''', (brand, model, int(year)))
                    conn.commit()

                    if cursor.rowcount:
                        print(f"Removed {brand} {model} ({transmission}) of {year} from the system.")
                    else:
                        print(f"No matching car found to remove.")
# viewing data
            elif choice == '3':
                    cursor.execute("SELECT * FROM cars ;")
                    available_cars = cursor.fetchall()
                    for car in available_cars:
                        print(car) 
#logouting out    
            elif choice == '4':
                print("Logout Successful")
                break
            else: 
             print(" Invalid Option ")
             
class Customer:
    def __init__(self, name):
        self.name = name 
        self.Rental_History = []
    
    #renting system  
    def rent_car(self, brand, model, rate, days, transmission,total_cost):
        total_cost = rate* days

        print(f"Total amount to pay: ₹{total_cost}")
        confirm = input("Proceed with payment? (yes/no): ").strip().lower()

        if confirm == 'yes':
        #payment option 
            card = input("Enter card number: ").strip()
            print("Processing payment...")
            print(f"Payment of ₹{total_cost} from{card} successful!") 
            cursor.execute("SELECT Year FROM Cars WHERE Brand = ? AND Model = ?", (brand, model))
            year = cursor.fetchone()[0]
            rented_car = Vehicle(brand, model, year, rate, total_cost)
            rented_car.is_available = False  
            rental_info = { 'car': rented_car,
                            'rental_period': days,
                            'rental_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'return_date': None,
                            'transmission': transmission}
            self.Rental_History.append(rental_info) 
            print (f"{self.name} rented a {brand} {model} ({transmission}) for {days} days.")
        
            cursor.execute("UPDATE Cars SET Available = 'No', Return = 'Yes' WHERE Brand = ? AND Model = ?", (brand, model))
            conn.commit()
            cursor.execute('''
                INSERT INTO Rental_History (username, brand, model, transmission, rental_date, return_date, days, rate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                self.name,
                brand,
                model,
                transmission,
                rental_info['rental_date'],
                None,    
                days,
                rate
                ))
            conn.commit()
        else:
            print(f"{self.name} couldn't rent {brand} {model}.Payment  cancelled.")

    # returning sytem
    def return_car(self, brand, model):
        for rental in self.Rental_History:
            if rental['car'].brand == brand and rental['car'].model == model and rental['return_date'] is None:
                rental['return_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rental['car'].is_available = True
                print(f"{self.name} returned the {brand} {model}.")
                return
        print(f"{brand} {model} was not rented or already returned.")
        cursor.execute("UPDATE Cars SET Available = 'Yes', Return = 'No' WHERE Brand = ? AND Model = ?", (brand, model))
        conn.commit()
         
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
        UPDATE Rental_History
        SET return_date = ?
        WHERE username = ? AND brand = ? AND model = ? AND return_date IS NULL
        ''', (now, self.name, brand, model))
        conn.commit()


# showing history
  
    def view_history(self):
        cursor.execute("SELECT brand, model, transmission, rental_date, return_date, days, rate FROM Rental_History WHERE username = ?", (self.name,))
        Rental_History = cursor.fetchall()

        if not Rental_History:
            print(f"No rental history found for {self.name}.")
        else:
            print(f"Rental History for {self.name}:")
        for record in Rental_History:
            brand, model, transmission, rental_date, return_date, days, rate = record
            print(f"Car: {brand} {model} ({transmission}), Days: {days}, Rate: ₹{rate}, "
                  f"Rented on: {rental_date}, Returned: {return_date if return_date else 'Not yet returned'}")


    def customer_menu(self):
        print(f"\nWelcome Customer: {self.name}")
        while True:
        # Customer actions 
            print("Customer Menu:")
            print("1. View Available Cars")
            print("2. Rent Car")
            print("3. Return Car")
            print("4. View History")
            print("5. Logout")
            choice = input("Select option: ")

# view available cars option 
            if choice == '1':
                cursor.execute("SELECT Brand, Model FROM Cars WHERE Available = 'Yes';")
                available_cars = cursor.fetchall()
                for car in available_cars:
                    print(car)

# rent car option
            elif choice == '2':
                brand= input("Car to be rented: ").strip()
                model=input ("Which model:  ").strip()
                days= int(input("time period:   ").strip())
                transmission=input("transmission(Automatic/Manual): ").strip()
                cursor.execute("SELECT Rent FROM Cars WHERE Brand = ? AND Model = ? AND Available = 'Yes'", (brand, model))
                result = cursor.fetchone()

                if result:
                    rate = result[0]
                    total_cost = rate * days
                    self.rent_car(brand, model, rate, days, transmission, total_cost)
                else:
                    print(f"{brand} {model} is not available .")

#return car option 
            elif choice == '3':
                brand= input("Car to be returned:")
                model= input ("Car Model:")
                self.return_car(brand, model)
    
# view history option
            elif choice == '4':
                self.view_history()
                            
            elif choice == '5':
                print(" Logout Successful")
                break
            else:
                print("Invalid option")

def info():
    while True:
         print("Welcome to the Car Rental System")
         while True:
            role = input("Are you an Admin or Customer? (a/c) or 'q' to quit: ").strip().lower()
            if role == 'q':
                print("Goodbye!")
                break
            # name = input("Enter your name: ")
# if u choose admin a
            if  role == 'a':
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                admin = {'KGF': '1234'}
                if username in admin and admin[username] == password:
                    print("login successfull")
                    admin = Admin(username)
                    Admin.admin_menu(admin)
                else:
                    print("Invalid admin credentials.")
                    
# if u choose customer c
            elif role == 'c':
                action = input("Do you want to (l)ogin or (s)ign up? ").strip().lower()
                if action == 's':     #sigh up 
                    new_user = input("Choose username: ")
                    new_pass = input("Choose password: ")
# storing login ids
                    cursor.execute("SELECT * FROM Customers WHERE username = ?", (new_user,))
                    if cursor.fetchone():
                        print("Username already exists. Try logging in.")
                    else:
                        cursor.execute("INSERT INTO Customers (username, password) VALUES (?, ?)", (new_user, new_pass))
                    conn.commit()
                    print("Signup successful. Please log in now.")

                    
                elif action == 'l': # login 
                    username = input("Username: ").strip()
                    password = input("Password: ").strip()
                    if not username or not password:
                        print("Username and password cannot be empty. Please try again.")
                        return  
                    cursor.execute("SELECT * FROM Customers WHERE username = ? AND password = ?", (username, password))
                    if cursor.fetchone():
                        print("Login successful.")
                    customer = Customer(username)
                    Customer.customer_menu(customer)
                else:
                    print("Invalid login. Please try again.")
                    exit()
            else:
                print("Invalid input. Try again.")

if __name__ == '__main__':
    info()
    
