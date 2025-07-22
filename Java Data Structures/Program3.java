import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public class Program3 {
    public static void main(String[] args) {
            // ArrayList<String> cars = new ArrayList<String>();
            LinkedList<String> cars = new LinkedList<>();
            cars.add("Volvo");
            cars.add("BMW");
            cars.add("Ford");
            cars.add("Mazda");

            Collections.sort(cars);  // Sort cars

            for (String i : cars) {
            System.out.println(i);
            }
   
    }    
}
