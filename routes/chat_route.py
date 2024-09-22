from flask import Blueprint,request
import json
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyC1Lno7jxeVz-uEtpmbGl6VoP7cfVbWCc0")

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chat', methods=['POST'])
def chat():
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
    history=[
        {"role": "user", "parts": "hello! next question answer will all be related to airport and flight so do not go off topic and answer within 1000 words at max."},
        {"role": "model", "parts": "Okay! I'm ready for your airport and flight questions. Ask away! I'll not go off topic"},
    ]
)

    user_message = request.json.get('message')

    response = chat.send_message(user_message)
    # print(response.text)
    # response = model.generate_content(user_message)

    return response.text
    
