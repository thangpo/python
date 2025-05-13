import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from pyvi import ViTokenizer
import string

# Định nghĩa dữ liệu intents (ý định)
intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["xin chào", "chào", "hi", "hello"],
            "responses": ["Xin chào! Rất vui được trò chuyện với bạn!", "Chào bạn!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["tạm biệt", "bye", "hẹn gặp lại"],
            "responses": ["Tạm biệt! Hẹn gặp lại nhé!", "Bye bye!"]
        },
        {
            "tag": "thanks",
            "patterns": ["cảm ơn", "thanks", "cám ơn"],
            "responses": ["Không có gì!", "Rất vui được giúp bạn!"]
        },
        {
            "tag": "about",
            "patterns": ["bạn là ai", "ai tạo ra bạn", "bạn làm gì"],
            "responses": ["Tôi là một chatbot AI được tạo bằng Python. Tôi ở đây để trả lời các câu hỏi của bạn!"]
        }
    ]
}

# Lưu intents vào file JSON
os.makedirs('data', exist_ok=True)

with open('data/intents.json', 'w', encoding='utf-8') as file:
    json.dump(intents, file, ensure_ascii=False, indent=4)

# Hàm tiền xử lý văn bản
def preprocess_text(text):
    tokens = ViTokenizer.tokenize(text.lower()).split()
    tokens = [t for t in tokens if t not in string.punctuation]
    vietnamese_stopwords = {'và', 'là', 'của', 'tôi', 'bạn'}
    tokens = [t for t in tokens if t not in vietnamese_stopwords]
    return ' '.join(tokens)

# Chuẩn bị dữ liệu huấn luyện
X_train = []
y_train = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        X_train.append(preprocess_text(pattern))
        y_train.append(intent['tag'])

# Tạo pipeline với TF-IDF và LinearSVC
pipeline = make_pipeline(TfidfVectorizer(), LinearSVC())

# Huấn luyện mô hình
pipeline.fit(X_train, y_train)

# Hàm dự đoán ý định
def predict_intent(text):
    processed_text = preprocess_text(text)
    return pipeline.predict([processed_text])[0]

# Hàm trả lời
def get_response(intent):
    for intent_data in intents['intents']:
        if intent_data['tag'] == intent:
            return np.random.choice(intent_data['responses'])
    return "Xin lỗi, tôi không hiểu ý bạn. Hãy thử lại nhé!"

# Hàm chạy chatbot
def run_chatbot():
    print("Chatbot: Xin chào! Hãy nói gì đó để bắt đầu.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ['quit', 'exit', 'thoát']:
            print("Chatbot: Tạm biệt!")
            break
        intent = predict_intent(user_input)
        response = get_response(intent)
        print(f"Chatbot: {response}")

# Chạy chatbot
if __name__ == "__main__":
    run_chatbot()