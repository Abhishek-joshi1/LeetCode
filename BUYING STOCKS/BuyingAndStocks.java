import java.util.*;
import java.util.Scanner;

public class BuyingAndStocks {
    public static int BuyingAndSelling(ArrayList<Integer> arr) {
    int n = arr.size();
    int sell = 0;
    	double hold = Double.POSITIVE_INFINITY;
    for(int i = 0;i < n;i++){
        	sell = Math.max(sell, (int) (arr.get(i) - hold));
        	hold = Math.min(hold, arr.get(i));
    }

    return sell;
}

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Sequence of Prices you want to give:");
        int n = sc.nextInt();
        ArrayList<Integer> prices = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            prices.add(sc.nextInt());
        }
        int result = BuyingAndSelling(prices);
        System.out.println(result);
        sc.close();
    }
}
