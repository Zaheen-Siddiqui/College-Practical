package packageA;
public class ClassB 
{
    public void display() 
    {
        ClassA classA = new ClassA();
        classA.publicMethod(); // Accessible
        classA.protectedMethod(); // Accessible since ClassB is in the same package
        classA.defaultMethod(); // Accessible since ClassB is in the same package
        // classA.privateMethod(); // Not accessible; private to ClassA
    }
}