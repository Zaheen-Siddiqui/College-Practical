public class PassByValueAndReference 
{
    public static void swapIntegers(int a, int b) 
    {
        int temp = a;
        a = b;
        b = temp;
        System.out.println("Inside swapIntegers - a: " + a + ", b: " + b);
    }
    public static void swapArrayValues(int[] arr) 
    {
        if (arr.length >= 2) 
        {
            int temp = arr[0];
            arr[0] = arr[1];
            arr[1] = temp;
            System.out.println("Inside swapArrayValues - arr[0]: " + arr[0] + ", arr[1]: " + arr[1]);
        }
    }
}
class Main
{
    public static void main(String[] args) 
    {
        int x = 5;
        int y = 10;
        System.out.println("Before swapIntegers - x: " + x + ", y: " + y);
        PassByValueAndReference.swapIntegers(x, y);
        System.out.println("After swapIntegers - x: " + x + ", y: " + y);
        int[] values = {5, 10};
        System.out.println("Before swapArrayValues - values[0]: " + values[0] + ", values[1]: " + values[1]);
        PassByValueAndReference.swapArrayValues(values);
        System.out.println("After swapArrayValues - values[0]: " + values[0] + ", values[1]: " + values[1]);
    }
}
