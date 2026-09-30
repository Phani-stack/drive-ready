public class Force {
    public static void main(String[] args) {
        AiChatClient aiChatClient1 = AiChatClientFactory.getAiChatClient("openai");
        AiChatClient aiChatClient2 = AiChatClientFactory.getAiChatClient("anthropic");
        
        aiChatClient1.chat("Hello");
        aiChatClient2.chat("Bye");
    }
}
