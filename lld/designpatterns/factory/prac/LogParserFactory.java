public class LogParserFactory {
    public static LogParser create(LogType parser) {
        switch (parser) {
            case CSV:
                return new CsvLogParser();
            case JSON:
                return new JsonLogParser();
            case TEXT:
                return new TextLogParser();
            default:
                return null;
        }
    }
}
