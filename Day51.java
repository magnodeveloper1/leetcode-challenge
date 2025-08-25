import java.util.Scanner;

public class Day51 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();

        while(t-- > 0) {
            int n = s.nextInt();
            System.out.println(n%3 == 0 || n%7 == 0 ? "YES" : "NO");
        }
    }
}
