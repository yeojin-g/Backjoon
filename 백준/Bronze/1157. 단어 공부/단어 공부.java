import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next().toLowerCase();

        int[] a_arr = new int[26];

        int max = 0;
        boolean isDuplicate = false;

        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            a_arr[(c - 'a')] = a_arr[(c - 'a')] + 1;
        }

        for(int i = 1; i < a_arr.length; i++){
            if(a_arr[max] < a_arr[i]) {
                max = i;
                isDuplicate = false;
            } else if (a_arr[max] != 0 && a_arr[max] == a_arr[i]) {
                isDuplicate = true;
            }
        }

        if(isDuplicate){
            System.out.println("?");
        } else {
            System.out.println((char)(max + 'A'));
        }
    }
}