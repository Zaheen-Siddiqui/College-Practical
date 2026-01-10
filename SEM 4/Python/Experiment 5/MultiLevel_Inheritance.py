class Car:
    def __init__(self, car_type , fuel_type, cost):
        self.fuel_type = fuel_type
        self.car_type = car_type
        self.cost = cost
        
    def fuel_tax(self,fuel_tax_type):
        self.fuel_tax_type = fuel_tax_type
        if fuel_tax_type == "DIESEL" or fuel_tax_type == "Diesel" or fuel_tax_type == "diesel":
            return .15
        elif fuel_tax_type == "PETROL" or fuel_tax_type == "Petrol" or fuel_tax_type == "petrol":
            return .75
        elif fuel_tax_type == "ELECTRIC" or fuel_tax_type == "Electric" or fuel_tax_type == "electric":
            return .05
        else:
            print("Incorrect fuel type")
            quit()

class CarBrand (Car):
    def __init__(self,brand_name, car_type, fuel_type,cost):
        super().__init__(fuel_type, car_type,cost)
        self.brand_name = brand_name
        
class CarModel(CarBrand):
    def __init__(self, brand_name, car_type, fuel_type,model_no,cost):
        super().__init__(brand_name,fuel_type, car_type,cost)
        self.model_no = model_no
    def __str__(self):
        tax = self.cost * super().fuel_tax()
        
        return f"\nCar Brand: {self.brand_name} \nCar Type: {self.car_type} \nModel Number: {self.model_no} \nFuel Type: {self.fuel_type} \nCost: {self.cost} \nFuel Tax: {tax}"


List = []
while True: 
    CB = input("Enter the car brand name ")
    CT = input("Enter the type of car example: Convertible, SUV, Sedan ")
    CM = input("Enter the car model ") 
    FT = input("Enter the type of fuel used ")
    Cost = int(input("Enter the cost of car "))
    List.append(CarModel(CB,CT,FT,CM,Cost))
    y_or_n = input("\nDo you wish to add another car (Y/n) ")
    if y_or_n == 'n' or y_or_n == 'N':
        break
    elif y_or_n == 'y' or y_or_n == 'Y':
        continue
    else:
        print("Incorrect Input")
        break
while True:
    Choice = int(input("\nEnter \n1 for print all cars of a certain brand \n2 for print all\n 3 for print all cars of a ceertain fuel type \n4 to end "))
    i=0
    if Choice == 1:
        brand = input("Enter name of brand to search ")
        for obj in List:
            if obj.brand_name == brand:
                print(obj)
                i +=1
        if i == 0:
            print("No cars of this brand")
    elif Choice == 2:
        for obj in List:
            print(obj)
    elif Choice == 3:
        break
    elif Choice == 4:
        Fuel = input("Enter the fuel type to search ")
        for obj in List:
            if obj.fuel_type == Fuel:
                print(obj)
                i +=1
        if i == 0:
            print("No cars of this fuel type")
    else:
        print("Incorrect Input")