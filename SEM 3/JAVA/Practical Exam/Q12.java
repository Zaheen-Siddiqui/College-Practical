import javax.swing.*;
import java.awt.*;

public class ShapeCanvas extends JPanel {
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        g.fillRect(20, 20, 100, 100); // Draw rectangle
        g.setColor(Color.BLUE);
        g.fillOval(150, 20, 100, 100); // Draw circle
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        ShapeCanvas shapes = new ShapeCanvas();
        frame.add(shapes);
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
