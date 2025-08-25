import java.util.Scanner;

public class Day5 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();

        while (t-- > 0) {
            long n = s.nextLong();
            String v = "";

            for (long i = 10; i < n; i *= 10) {
                if (n % (1 + i) == 0) {
                    long x = (long) n / (1 + i);
                    v += x + " ";
                }
            }

            System.out.println(v.length() == 0 ? 0 : v.trim());
        }
    }
}