class RecursionMain {
    public static void getData(String str) {
        if (str.length() == 0) {
            System.out.println("String Ended");
        } else {
            System.out.println(str.substring(0, 1).toUpperCase());
            getData(str.substring(1, str.length()));
        }
    }
    public static void main(String[] args) {
        getData("YoungWonks");
    }
}