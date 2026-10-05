from transformers import pipeline

sentiment_analyzer = pipeline('sentiment-analysis')

texts = [
    "I feel really happy and motivated today!",
    "I am so sad and depressed, nothing seems right.",
    "I'm stressed about my exams and deadlines.",
    "Today has been okay, just a bit tired."
]

results = sentiment_analyzer(texts)

for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']}, Score: {result['score']:.2f}\n")

def chatbot_reply(sentiment_label):
    if sentiment_label == 'POSITIVE':
        return "I'm glad to hear you're feeling good! Keep it up."
    elif sentiment_label == 'NEGATIVE':
        return "I'm sorry to hear you're feeling down. Would you like some help or to talk more?"
    else:
        return "Thanks for sharing your feelings. I'm here if you want to share more."

print("--- Chatbot Responses ---")
for result in results:
    print(chatbot_reply(result['label']))
