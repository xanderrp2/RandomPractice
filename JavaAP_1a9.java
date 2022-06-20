import java.util.Array;
import java.util.Scanner;

public class JavaAP_1a9 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int day = input.nextInt();
        
        switch(day){
            case 0: System.out.println("sunday"); break;
            case 1: System.out.println("Monday"); break;
            case 2: System.out.println("Tuesday"); break;
            case 3: System.out.println("Wednesday"); break;
            case 4: System.out.println("Thursday"); break;
            case 5: System.out.println("Friday"); break;
            case 6: System.out.println("Saturday"); break;
            case 7: System.out.println("Sunday"); break;

            default: System.out.println("no idea what day it is " + day);;
            

        

     
     }
    }

}
    



// import java.util.Array;
// import java.util.Scanner;

// import javax.swing.event.SwingPropertyChangeSupport;
// import javax.swing.plaf.synth.SynthScrollBarUI;

// public class JavaAP_1a9 {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         String name = input.next();
//         int vowels = 0;
//         int nonvowels = 0;

//         switch(name){
//         case "a": vowels++; 
//         case "e": vowels++;
//         case "i": vowels++;
//         case "o": vowels++;
//         case "u": vowels++; 
//         default: nonvowels++;
        
//         }
//         System.out.println((String)nonvowels, (String)vowels);
    
    
//     }  
// }