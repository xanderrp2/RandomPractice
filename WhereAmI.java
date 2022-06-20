import java.util.Scanner;

/**
 * WhereAmI
 */
public class WhereAmI {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        String b = "test";
        String holder = "test";
        String compar = "test";
        int count = 0;
        for (int i = 0; i < 2; i++) {
            b = input.nextLine();
        }
        for (int k = 0; k < a; k++) {
            count = 0;
            if(k<a){
                compar = b.substring(0,k);
                for (int i = 0; i < a; i++) {
                    if(i < a && i >= k){
                        holder = b.substring(k,i);
                    }
                    if(compar.equals(holder) == false){
                        count++;
                    
                    }else{
                        System.out.println(compar + " " + holder);
                        System.out.println(count);
                    }
                }

            }
        }
        
    }
    
}