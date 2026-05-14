from google import genai
import speech_recognition as sr

client = genai.Client(api_key="AIzaSyCxs4_Qv7ws5v2bwxHLXtWwxpucHOF48yc")
def AI_response(input_text):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= input_text
        )
    except:
        return "An error occured. Please try again later."
    else:
        return response.text

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        response = r.recognize_google(audio, language="vi-VN")
    except sr.UnknownValueError:
        response = "Không nhận ra giọng nói."
    return response


    