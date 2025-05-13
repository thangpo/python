import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from pyvi import ViTokenizer
import string
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS

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
        },
        {
            "tag": "weather",
            "patterns": [
                "thời tiết hôm nay thế nào",
                "dự báo thời tiết",
                "trời có mưa không",
                "thời tiết ở Hà Nội",
                "thời tiết ở TP.HCM"
            ],
            "responses": ["Để tôi kiểm tra thời tiết cho bạn..."]
        },
    ]
}

OPENWEATHER_API_KEY = '2d5d17fa4dfbe09e488c3b9cc2485a98'

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

def get_weather(city='Hanoi'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&lang=vi&units=metric'
    try:
        res = requests.get(url)
        data = res.json()
        if data.get('cod') != 200:
            return "Xin lỗi, tôi không lấy được thông tin thời tiết."
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Thời tiết tại {city}: {desc}, nhiệt độ {temp}°C."
    except:
        return "Xin lỗi, tôi không lấy được thông tin thời tiết."
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
def get_response(intent, user_message=None):
    if intent == "weather":
        # Tìm tên thành phố trong user_message nếu có
        city = "Hanoi"
        if user_message:
            if "hồ chí minh" in user_message.lower() or "tp.hcm" in user_message.lower():
                city = "Ho Chi Minh City"
            elif "hà nội" in user_message.lower():
                city = "Hanoi"
        return get_weather(city)
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
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    intent = predict_intent(user_message)
    bot_reply = get_response(intent)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)