import javax.swing.*;
import java.awt.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WeatherApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Weather App");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 300);

            JTextArea weatherDisplay = new JTextArea();
            weatherDisplay.setEditable(false);

            // Read weather data from file
            try (BufferedReader br = new BufferedReader(new FileReader("weather_data.txt"))) {
                String line;
                StringBuilder content = new StringBuilder();
                while ((line = br.readLine()) != null) {
                    content.append(line).append("\n");
                }
                weatherDisplay.setText(content.toString());
            } catch (IOException e) {
                weatherDisplay.setText("Failed to load weather data. Run the Python script first.");
            }

            frame.add(new JScrollPane(weatherDisplay), BorderLayout.CENTER);
            frame.setVisible(true);
        });
    }
}
