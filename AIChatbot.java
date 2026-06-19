import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class AIChatbot extends JFrame {
    private JTextArea chatArea;
    private JTextField inputField;
    private JButton sendButton;
    private Map<String, String> knowledgeBase;

    public AIChatbot() {
        // Title and Layout Setup
        setTitle("AI Chatbot Assistant");
        setSize(450, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // Initialize FAQ Knowledge Base (Rule-Based Logic)
        initializeKnowledgeBase();

        // Chat Display Area
        chatArea = new JTextArea();
        chatArea.setEditable(false);
        chatArea.setFont(new Font("Arial", Font.PLAIN, 14));
        chatArea.setLineWrap(true);
        chatArea.setWrapStyleWord(true);
        JScrollPane scrollPane = new JScrollPane(chatArea);
        add(scrollPane, BorderLayout.CENTER);

        // Bottom Panel for Input
        JPanel bottomPanel = new JPanel(new BorderLayout());
        inputField = new JTextField();
        inputField.setFont(new Font("Arial", Font.PLAIN, 14));
        sendButton = new JButton("Send");
        sendButton.setFont(new Font("Arial", Font.BOLD, 14));

        bottomPanel.add(inputField, BorderLayout.CENTER);
        bottomPanel.add(sendButton, BorderLayout.EAST);
        add(bottomPanel, BorderLayout.SOUTH);

        // Welcome Message
        chatArea.append("Bot: Hello! I am your AI Assistant. Ask me anything about our services or type 'bye' to exit.\n\n");

        // Action Listeners
        ActionListener sendAction = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                processUserMessage();
            }
        };

        sendButton.addActionListener(sendAction);
        inputField.addActionListener(sendAction);
    }

    private void initializeKnowledgeBase() {
        knowledgeBase = new HashMap<>();
        // Training data / Frequently Asked Questions
        knowledgeBase.put("hello", "Hi there! How can I help you today?");
        knowledgeBase.put("hi", "Hello! Hope you are doing great. What can I do for you?");
        knowledgeBase.put("your name", "I am a smart Java-based AI Chatbot assistant.");
        knowledgeBase.put("help", "Sure! I can answer FAQs, provide project info, or just chat. Ask me away!");
        knowledgeBase.put("java", "Java is a powerful, object-oriented programming language used widely for building robust apps!");
        knowledgeBase.put("nlp", "Natural Language Processing (NLP) helps computers understand and process human languages.");
        knowledgeBase.put("bye", "Goodbye! Have a wonderful day ahead.");
    }

    private void processUserMessage() {
        String userText = inputField.getText().trim();
        if (userText.isEmpty()) return;

        chatArea.append("You: " + userText + "\n");
        inputField.setText("");

        // Simple Natural Language Processing (Tokenization and Lowercasing)
        String cleanInput = userText.toLowerCase().replaceAll("[^a-zA-Z0-9 ]", "");
        String botResponse = generateResponse(cleanInput);

        // Bot typing response with a small delay simulation
        Timer timer = new Timer(300, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                chatArea.append("Bot: " + botResponse + "\n\n");
                chatArea.setCaretPosition(chatArea.getDocument().getLength());
            }
        });
        timer.setRepeats(false);
        timer.start();
    }

    private String generateResponse(String input) {
        // Rule-Based Machine Learning / Matching Logic
        for (String key : knowledgeBase.keySet()) {
            if (input.contains(key)) {
                return knowledgeBase.get(key);
            }
        }
        // Default fallback response if intent is unknown
        return "I'm sorry, I couldn't completely grasp that. Can you rephrase your question or ask about 'Java', 'NLP', or 'Help'?";
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new AIChatbot().setVisible(true);
            }
        });
    }
                }
