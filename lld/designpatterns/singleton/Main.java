class Main {
    public static void main(String[] args) {

        UserTrack u1 = UserTrack.getInstance();
        UserTrack u2 = UserTrack.getInstance();
        u2.incrementCount();
        u2.incrementCount();
        u2.incrementCount();
        u2.incrementCount();
        u2.incrementCount();
        u2.incrementCount();
        UserTrack u3 = UserTrack.getInstance();
        System.out.println(u3.getCount());

    }
}
