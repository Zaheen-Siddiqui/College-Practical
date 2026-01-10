import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.IOException;
public class FileReadWriteExample 
{
    public static void main(String[] args) 
    {
        String inputFilePath = "input.txt";  // Specify the input file path
        String outputFilePath = "output.txt"; // Specify the output file path
        // Writing to a text file
        try (FileWriter fileWriter = new FileWriter(outputFilePath)) 
        {
            fileWriter.write("Hello, this is a test file.\n");
            fileWriter.write("It contains some sample text for reading.\n");
            fileWriter.write("This file will be read by FileReader.");
            System.out.println("Data written to output.txt successfully.");
        } catch (IOException e) 
        {
            System.out.println("Error writing to file: " + e.getMessage());
        }
        // Reading from a text file
        try (FileReader fileReader = new FileReader(inputFilePath);
             BufferedReader bufferedReader = new BufferedReader(fileReader)) 
             {
             
                String line;
                System.out.println("Reading from " + inputFilePath + ":");
                while ((line = bufferedReader.readLine()) != null) 
                {
                    System.out.println(line);
                }
        } catch (IOException e) 
        {
            System.out.println("Error reading from file: " + e.getMessage());
        }
    }
}
