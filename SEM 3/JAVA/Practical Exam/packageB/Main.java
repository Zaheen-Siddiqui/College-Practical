package packageB;
import packageA.ClassA;
import packageA.ClassB;
public class Main 
{
    public static void main(String[] args) {
        ClassA classA = new ClassA();
        classA.publicMethod(); // Accessible
        // classA.protectedMethod(); // Not accessible; not in the same package
        // classA.defaultMethod(); // Not accessible; not in the same package
        // classA.privateMethod(); // Not accessible; private to ClassA

        ClassB classB = new ClassB();
        classB.display(); // Access methods in ClassB
    }
}
