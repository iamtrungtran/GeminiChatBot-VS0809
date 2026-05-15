import tkinter
import computer
import threading
import queue

response_queue = queue.Queue()

def send_message():
    input_text = chat_area.get("1.0", tkinter.END)
    chat_area.delete("1.0", tkinter.END)
    text_area.insert(tkinter.END, "You: " + input_text)
    AI_response(input_text)

def AI_response(input_text):
    text_area.insert(tkinter.END, "Gemini: ")
    button_send.config(state="disabled")
    button_listen.config(state="disabled")
    #Tạo luồng để get repsponse
    t = threading.Thread(
        target=computer.AI_response_stream,
        args=(input_text, response_queue)
    )
    t.start()
    check_queue()

def check_queue():
    try:
        chunk = response_queue.get_nowait()
        if chunk == None:
            text_area.insert(tkinter.END, "\n")
            save_history()
            button_send.config(state="normal")
            button_listen.config(state="normal")
            return
        text_area.insert(tkinter.END, chunk)
        text_area.see(tkinter.END)
    except queue.Empty:
        pass
    window.after(100, check_queue)

def clear():
    print("clear() duoc goi")
    text_area.delete("1.0", tkinter.END)
    computer.reset_chat()
    text_area.insert(1.0, "I'm Gemini Chat Bot, Can i help you? \n")

def listen():
    button_listen.config(text="Listening")
    window.update()
    user_text = computer.listen()
    chat_area.insert(1.0, user_text)
    button_listen.config(text="Listened")

def save_history():
    text_as = text_area.get("1.0", tkinter.END)
    fo = open("history.txt", "w", encoding="utf-8")
    fo.write(text_as)
    fo.close()

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

text_area.insert(1.0, "I'm Gemini Chat Bot, Can i help you? \n")

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

tkinter.mainloop()