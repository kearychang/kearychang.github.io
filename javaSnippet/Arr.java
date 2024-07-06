//1,2,3,4
//"a","b","c"
//1,"q" NOT
package proj;

public class Arr {
    public static void main(String[] args) {
        int iArray[] = new int[4];
        String[] sArray = new String[4];
        iArray[0] = 1;
        iArray[1] = 2;
        iArray[2] = 3;
        iArray[3] = 4;
        for (int i = 0; i < iArray.length; i++) {
            System.out.println(iArray[i]);
        }
        iArray[4] = 0;
    }
}