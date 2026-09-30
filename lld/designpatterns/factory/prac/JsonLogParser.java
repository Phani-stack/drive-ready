public class JsonLogParser implements LogParser {
    @Override
    public void parse(String path) {
        System.out.println("JSON log parser: " + path);
    }
}
