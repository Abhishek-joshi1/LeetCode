import java.util.ArrayList;

public class Program1{
    

    public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<>();
        cars.add("Maruti Suzuki");
        cars.add("Alto");
        cars.add("Benz");
        System.out.println(cars.get(1));

        // cars.add(1, "Mazda");
        cars.set(1, "mazda");
        System.out.println(cars.get(1));

        cars.remove(2);
        System.out.println(cars);
    }
}