interface MathConstants 
{
    double PI = 3.14159;
    double E = 2.71828;
}
class CircleRad implements MathConstants
{
    double radius;

    CircleRad(double radius) 
    {
        this.radius = radius;
    }
    double area() 
    {
        return PI * radius * radius;
    }
}
class Exponential implements MathConstants 
{
    double exponent;
    Exponential(double exponent) 
    {
        this.exponent = exponent;
    }
    double calculate() 
    {
        return Math.pow(E, exponent);
    }
}
public class CircleArea 
{
    public static void main(String[] args) 
    {
        CircleRad circle = new CircleRad(5);
        System.out.println("Area of the circle: " + circle.area());
        Exponential exp = new Exponential(3);
        System.out.println("e^" + exp.exponent + " = " + exp.calculate());
    }
}
