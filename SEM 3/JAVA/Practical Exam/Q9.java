class EvenNumberThread extends Thread 
{
    @Override
    public void run() {
        for (int i = 0; i <= 20; i += 2) 
        {
            System.out.println("Even: " + i);
            try 
            {
                Thread.sleep(100); // Sleep for 100 milliseconds
            } catch (InterruptedException e) 
            {
                System.out.println(e.getMessage());
            }
        }
    }
}
class OddNumberThread extends Thread 
{
    @Override
    public void run() 
    {
        for (int i = 1; i <= 20; i += 2) 
        {
            System.out.println("Odd: " + i);
            try 
            {
                Thread.sleep(100); // Sleep for 100 milliseconds
            } catch (InterruptedException e) 
            {
                System.out.println(e.getMessage());
            }
        }
    }
}
public class NumberThread 
{
    public static void main(String[] args) 
    {
        EvenNumberThread evenThread = new EvenNumberThread();
        OddNumberThread oddThread = new OddNumberThread();
        evenThread.start();
        oddThread.start();
    }
}
