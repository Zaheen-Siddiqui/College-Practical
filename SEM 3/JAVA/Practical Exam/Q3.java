public class OuterClass 
{
    private String outerField = "Outer Class Field";
    public void display() 
    {
        System.out.println("Inside Outer Class Method");
    }
    class InnerClass 
    {
        private String innerField = "Inner Class Field";
        public void displayInner() 
        {
            System.out.println("Inside Inner Class Method");
            System.out.println("Accessing: " + outerField);
            display();
        }
    }
    public static void main(String[] args) 
    {
        OuterClass outer = new OuterClass();
        outer.display();
        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.displayInner();
    }
}
