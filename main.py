import tkinter
import computer

def send_message():
    input_text = chat_area.get("1.0", tkinter.END)
    chat_area.delete("1.0", tkinter.END)
    text_area.insert(tkinter.END, "You: " + input_text)
    AI_response(input_text)

def AI_response(input_text):
    traloi = computer.AI_response(input_text)
    text_area.insert(tkinter.END, "Gemini: " + traloi + "\n")
    text_as = text_area.get("1.0", tkinter.END)
    fo = open("history.txt", "w", encoding="utf-8")
    fo.write(text_as)
    fo.close()

def clear():
    text_area.delete("1.0", tkinter.END)

def listen():
    button_listen.config(text="Listening")
    window.update()
    user_text = computer.listen()
    chat_area.insert(1.0, user_text)
    button_listen.config(text="Listened")

window = tkinter.Tk()
window.title("Chat bot")
window.config(bg="#8fbc8f")

text_area = tkinter.Text(
    width=40,
    height=13,
    wrap="word",
    font="Lexend, 20"
)
text_area.grid(
    column=0,
    row=0,
    padx=5,
    pady=10
)

chat_area = tkinter.Text(
    width=40,
    height=3,
    wrap="word",
    font="Lexend, 20")
chat_area.grid(
    column=0,
    row=1,
    pady= 10)

button_clear = tkinter.Button(
    text="Clear",
    width=10,
    height=3,
    borderwidth=4,
    command=clear,
)
button_clear.grid(
    column=1,
    row=0,
    sticky="N",
    padx=5,
    pady=10
)

button_listen = tkinter.Button(
    text="Listen",
    width=10,
    height=3,
    borderwidth=4,
    command=listen,
)
button_listen.grid(
    column=1,
    row=0,
    sticky="S",
    pady=10)

button_send = tkinter.Button(
    text="Send",
    width=10,
    height=3,
    borderwidth=4,
    command=send_message)
button_send.grid(
    column=1,
    row=1,
    sticky="S",
    pady=10
)

text_area.insert(1.0, "I'm Gemini Chat Bot, Can i help you? \n")

# try:
#     fi = open("history.txt", "r", encoding="utf-8")
# except:
#     fi = open("history.txt", "x", encoding="utf-8")
# else:
#     result = fi.read()
#     text_area.delete(2.0, tkinter.END)
#     text_area.insert(2.0, result)
# finally:
#     fi.close()

tkinter.mainloop()