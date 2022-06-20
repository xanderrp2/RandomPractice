import java.util.Arrays;

class JavaAP_1a6bHW{
    public static void main(String[] args){
        int round = 0;
        int nums = 5;
        System.out.println(nums);
        int[][] numbers = new int[nums][];
        System.out.println(numbers.length);
        for (int i = 0; i < nums; i++){
            numbers[i] = new int[i+1];
            System.out.println(i + " numbers round");
            System.out.println(numbers[i].length + "hello");
        }
        for (int k = 0; k < numbers.length; k ++){
            for (int b = 0; b < numbers[k].length; b++){
                round = round + 1;
                System.out.println(round);
                numbers[k][b] = (round * 10);
            }

        }
        System.out.println(Arrays.deepToString(numbers));
        
    }

}
