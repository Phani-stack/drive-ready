public class UserTrack {
    private int userCount;
    private static UserTrack userTrack;

    private UserTrack() {
        userCount = 0;
    }

    public static UserTrack getInstance() {
        if (userTrack == null) {
            userTrack = new UserTrack();
        }
        return userTrack;
    }

    public int getCount() {
        return userCount;
    }

    public void incrementCount() {
        userCount += 1;
    }

}
