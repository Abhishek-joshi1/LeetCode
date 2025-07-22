import java.util.LinkedList;

public class Program2 {
    public static void main(String[] args) {
        LinkedList<String> cars = new LinkedList<>();
        cars.add("Maruti");
        cars.add("Alto");
        cars.add("Ciaz");
        System.out.println(cars);

        cars.addFirst("Corzo");
        System.out.println(cars);
    }    
}
