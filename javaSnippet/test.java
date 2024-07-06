package proj;

import java.util.Comparator;
import java.util.SortedSet;
import java.util.TreeSet;

public class test {
    public static void main(String[] args) {
        // Creating a SortedSet with a custom comparator
        SortedSet<String> sortedSet = new TreeSet<>(new CustomComparator());

        // Adding elements to the SortedSet
        sortedSet.add("Apple");
        sortedSet.add("Banana");
        sortedSet.add("Orange");
        sortedSet.add("Grapes");

        // Printing the SortedSet elements
        System.out.println("SortedSet elements: " + sortedSet);

        // Getting the comparator used by the SortedSet
        Comparator<? super String> setComparator = sortedSet.comparator();
        System.out.println("SortedSet comparator: " + setComparator);
    }

    // Custom Comparator implementation
    static class CustomComparator implements Comparator<String> {
        @Override
        public int compare(String s1, String s2) {
            // Custom logic for comparison (here, comparing based on length)
            return Integer.compare(s1.length(), s2.length());
        }
    }
}