public class CsvLogParser implements LogParser {
    @Override
    public void parse(String path) {
        System.out.println("CSV log parser: " + path);
    }
}
