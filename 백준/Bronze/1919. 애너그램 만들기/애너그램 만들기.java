import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        int cnt = 0;

        int[] a_arr = new int[26];
        int[] b_arr = new int[26];

        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            a_arr[(c - 'a')] = a_arr[(c - 'a')] + 1;
        }

        for(int i = 0; i < b.length(); i++){
            char c = b.charAt(i);
            b_arr[(c - 'a')] = b_arr[(c - 'a')] + 1;
        }

        for(int i = 0; i < 26; i++){
            cnt += Math.abs(a_arr[i] - b_arr[i]);
        }

        System.out.println(cnt);
    }
}