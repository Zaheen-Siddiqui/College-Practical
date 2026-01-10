public class StaticDemo 
{
    static int statvar = 0;
    static
    {
        System.out.println("Static block executed. Initializing staticVariable.");
        statvar = 10;
    }
    public static void incstatvar() 
    {
        statvar++;
        System.out.println("Static method called. staticVariable: " + statvar);
    }
    public static void main(String[] args) 
    {
        System.out.println("Main method started.");
        System.out.println("Initial value of staticVariable: " + statvar);
        incstatvar();
        incstatvar();
        System.out.println("Final value of staticVariable: " + statvar);
    }
}
