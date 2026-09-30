public class Client {
    public static void main(String[] args) {
        LogParser logParser1 = LogParserFactory.create(LogType.JSON);
        LogParser logParser2 = LogParserFactory.create(LogType.CSV);
        LogParser logParser3 = LogParserFactory.create(LogType.TEXT);

        logParser1.parse("random path");
        logParser2.parse("random path");
        logParser3.parse("random path");

        System.out.print(LogType.JSON);
    }
}
