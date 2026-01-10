package packageA;
public class ClassA 
{
    public void publicMethod() 
    {
        System.out.println("Public Method in ClassA");
    }
    protected void protectedMethod() 
    {
        System.out.println("Protected Method in ClassA");
    }
    void defaultMethod() 
    {
        System.out.println("Default Method in ClassA");
    }
    private void privateMethod() 
    {
        System.out.println("Private Method in ClassA");
    }
    public void accessMethods() 
    {
        publicMethod();
        protectedMethod();
        defaultMethod();
        privateMethod();
    }
}
