from google import genai
from dotenv import load_dotenv
import speech_recognition as sr
import os

#Load API from .env
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Create chat session
chat_session = client.chats.create(model="gemini-3-flash-preview")

def AI_response_stream(input_text, queue):
    try:
        response = chat_session.send_message_stream(input_text)
        for chunk in response:
            queue.put(chunk.text)
        queue.put(None)
    except:
        queue.put("An error occured. Please try again later.")
        queue.put(None)

def reset_chat():
    global chat_session
    chat_session = client.chats.create(model="gemini-3-flash-preview")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        response = r.recognize_google(audio, language="vi-VN")
    except sr.UnknownValueError:
        response = "Không nhận ra giọng nói."
    return response


    