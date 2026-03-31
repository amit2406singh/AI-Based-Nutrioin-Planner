import tkinter as tk


def open_chat(parent):

    window = tk.Toplevel(parent)
    window.title("AI Chat Assistant")
    window.geometry("400x450")

    chat_box = tk.Text(window,height=20,width=45)
    chat_box.pack(pady=10)

    entry = tk.Entry(window,width=30)
    entry.pack()

    def send():

        msg = entry.get()
        entry.delete(0,"end")

        chat_box.insert("end","You: "+msg+"\n")

        msg = msg.lower()

        if "protein" in msg:
            reply = "Protein foods: eggs, paneer, tofu, chickpeas"
        elif "weight loss" in msg:
            reply = "Eat high protein and low carb foods."
        elif "vitamin" in msg:
            reply = "Fruits and vegetables are rich in vitamins."
        else:
            reply = "I am your nutrition assistant."

        chat_box.insert("end","Bot: "+reply+"\n\n")

    tk.Button(window,text="Send",command=send).pack(pady=5)