class SuperClass 
{
    private String privateField = "Private Field in SuperClass";
    public String getPrivateField() 
    {
        return privateField;
    }
}
class SubClass extends SuperClass 
{
    public void displayPrivateField() 
    {
        String value = getPrivateField();
        System.out.println("Accessing from SubClass: " + value);
    }
}
public class MainClass 
{
    public static void main(String[] args) 
    {
        SubClass subClass = new SubClass();
        subClass.displayPrivateField();
    }
}
