class Vehicle 
{
    int speed;
    Vehicle(int speed) 
    {
        this.speed = speed;
    }
    void display() 
    {
        System.out.println("Vehicle speed: " + speed + " km/h");
    }
}
class Car extends Vehicle 
{
    String model;
    Car(int speed, String model) 
    {
        super(speed);  // Calling the constructor of the superclass
        this.model = model;
    }
    void display() 
    {
        super.display();  // Calling the method from the superclass
        System.out.println("Car model: " + model);
    }
    void showSuperSpeed() 
    {
        System.out.println("Speed from superclass: " + super.speed + " km/h");
    }
}
public class CarDisplay 
{
    public static void main(String[] args) 
    {
        Car car = new Car(120, "Toyota");
        car.display();
        car.showSuperSpeed();
    }
}
