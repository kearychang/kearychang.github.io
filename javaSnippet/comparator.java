package proj;
import java.util.Comparator;
import java.util.Arrays;

public class comparator {
    public static void main(String[] args) {
        Comparator<Integer> c = new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                if (a == b) {
                    return 0;
                } else if (a < b) {
                    return 1;
                }
                return -1;
            }
        };
        Integer[] arr = {1,2,3,4};
        Arrays.sort(arr, c);
        for (Integer e : arr) {
            System.out.println(e);
        }
    }
}