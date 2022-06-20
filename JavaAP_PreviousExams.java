
// public static Position[][] getSuccesorArray(int[][] intArr){
//     int n = 0;
//     Position[][] successors = new Postion[intArr.length][intArr[0].length];
//     while(findPosition(n,intArr) == null){
//         n++;
//     }
//     for(int i = 0; i < intArr.length;i++){
//         for(int j = 0; j < intArr[i].length;j++){
//             if(intArr[i][j] == n){
//                 successors[i][j] = findPosition(n+1,intArr);

//             }

//         }

//     }
// }


// public static Position findPosition(int num, int[][] intArr){
//     for(int i = 0; i < intArr.length;i++){
//         for(int j = 0; j < intArr[i].length;j++){
//             if(intArr[i][j] == num){
//                 return new Position(i,j);

//             }

//         }

//     }
//     return null;

// }

//     public int findLastOccurrence(String str){
//     int index = 0;
//     int counter = 1;
//     if(this.findNthOccurrence(str,1) == -1){
//         return -1;
//     }else{
//         while(index >= 0){
//         counter++;
//         if(this.findNthOccurrence(str,1) != -1){
//             index = this.findNthOccurrence(str,counter);

//         }else{
//             break;
//         }
//     return index;
// }
// }

//     public void relplaceNthOccurrence(String str, int n, String repl) {
//         int pos = this.findNthOccurrence(str, n);
//         if (pos >= 0) {
//             String firstHalf = currentPhrase.substring(0, pos);
//             String secondHalf = str.substring(pos + str.length(), currentPhrase.length());
//             this.currentPhrase = firstHalf + repl + secondHalf;
//         }

//     }


// public class MultPractice implements StudyPractice{
// private final int first;
// private int second;
// MultPractice(int first, int second){
// this.first = first;
// this.second = second;

// }
// public String getProblem(){
// return(first + " TIMES " + second);
// }
// public void nextProblem(){
// second++;
// }

// }

// public static boolean isLatin(int[][] square){
// int[] firstRow = square[0];
// boolean isLatinSquare = false;
// if(!containsDublicates(firstRow)){
// for(int i = 1; i < square.length; i++){
// if(!hasAllValues(firstRow, square[i])){
// return false;
// }
// for(int j = 0; j < square[i].length; j++){
// if(!hasAllValues(firstRow, getColumn(square j)){
// return false;
// }

// }else{
// return false;
// }
// return true;
// }
// }

// public static int[] getColumn(int[][] arr2D, int c){
// int[] column = new int[arr2D.length];
// for(int i = 0; i < arr2D.length; i++){
// column[i] = arr2D[i][c];

// }
// return column;

//}

// class CodeWordChecker implements StringChecker{
// private int min;
// private int max;
// private String notThis;
// CodeWordChecker(int min, int max,String word){
// this.min = min;
// this.max = max;
// this.notThis = word;

// }
// CodeWordChecker(String word){
// this.min = 6;
// this.max = 20;
// this.notThis = word;

// }

// public boolean isValid(String codeWord){
// if(word.length() > max || word.length() < min){
// return false;

// }
// for(int i = 0; i < (codeWord.length()-word.length());i++){
// if(codeWord.substring(i,word.length).equals(word)){
// return false;

// }

// }
// return true;
// }
// }

// public int numMatches(){
// int counter = 0;
// for(int i = 0; i < allPairs.size(); i++){
// if(allPairs.get(i).getFirst().equals(allPairs.get(i).getSecond()))){
// counter++;
// }
// }
// }

// public WordPairList(String[] Words){
// ArrayList<WordPair> allPairs = new ArrayList<WordPair>();
// for(int i = 0; i < Words.length; i++){
// for(int j = i; j < (Words.length-i); j++){
// WordPair holder = new WordPair(Words[i],Words[j]);
// allPairs.add(holder);
// }
// }

// }

// public double runSimulation(int num){
// double success = 0.0;
// for(int i = 0; i<num; i++){
// if(this.simulate()){
// success = success + 1.0;
// }

// }
// return success/num;

// }

// public boolean simulate(){
// int distance = 0;
// for(int i = 0, i<this.maxHops; i++){
// distance = distance + hopDistance();
// if(distance < 0){
// return false;
// }
// if(distance > this.goalDistance){
// return true;
// }
// }
// if(distance == this.goalDistance){
// return true;
// }
// return false;
// }