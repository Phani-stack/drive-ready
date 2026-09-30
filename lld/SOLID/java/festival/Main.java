class Main {
    public static void main(String[] args) {
        BoothActivity boothActivity = new BoothActivity(100000);
        boothActivity.registerStudent();
        boothActivity.deduct(100);
    }
}
