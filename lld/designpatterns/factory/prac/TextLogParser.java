class TextLogParser implements LogParser {
    @Override
    public void parse(String path) {
        System.out.println("Text log parser: " + path);
    }
}
