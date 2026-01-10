import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileInputOutputExample 
{
    public static void main(String[] args) 
    {
        String inputFilePath = "input.txt";  // Specify the input file path
        String outputFilePath = "output.txt"; // Specify the output file path
        // Writing to the input file for demonstration
        try (FileOutputStream fileOutputStream = new FileOutputStream(inputFilePath)) 
        {
            String sampleText = "This is a sample input file.\nIt contains some text for reading.";
            fileOutputStream.write(sampleText.getBytes());
            System.out.println("Data written to input.txt successfully.");
        } catch (IOException e) 
        {
            System.out.println("Error writing to input file: " + e.getMessage());
        }
        // Reading from the input file and writing to the output file
        try (FileInputStream fileInputStream = new FileInputStream(inputFilePath);
             FileOutputStream fileOutputStream = new FileOutputStream(outputFilePath)) 
            {
            byte[] buffer = new byte[1024]; // Buffer to hold data
            int bytesRead;
            while ((bytesRead = fileInputStream.read(buffer)) != -1) 
            {
                fileOutputStream.write(buffer, 0, bytesRead); // Write to output file
            }
            System.out.println("Data read from input.txt and written to output.txt successfully.");
        } catch (IOException e) 
        {
            System.out.println("Error reading or writing file: " + e.getMessage());
        }
    }
}
