import java.util.TreeSet;

public class Program6{
  public static void main(String[] args) {
    TreeSet<String> cars = new TreeSet<>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("BMW");  // Duplicate
    cars.add("Mazda");

    System.out.println(cars);
  }
}