import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            if('A' <= c && c <= 'Z') {
                System.out.print((char) ('a' + c - 'A'));
            } else{
                System.out.print((char)('A' + c - 'a'));
            }
        }
    }
}