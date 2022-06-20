import java.util.Scanner;
import java.util.*;

public class DMOJ_SW {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        String b;
        String[][] values = new String[a][3];
        String[] holder = new String[3];
        long w;
        long e;
        long r;
        for (int i = 0; i < a; i++) {
            b = input.nextLine();
            holder = b.split(" ");
            values[i] = holder;
        }
        System.out.println(values.toString());
        for (int i = 0; i < values.length; i++) {
            w = Long.parseLong(values[i][0]);
            e = Long.parseLong(values[i][1]);
            r = Long.parseLong(values[i][3]);
            if(w*e == r){
                System.out.println("16 BIT S/W ONLY");
            }else{
                System.out.println("POSSIBLE DOUBLE SIGMA");
            }
            
        }
    }
    
}