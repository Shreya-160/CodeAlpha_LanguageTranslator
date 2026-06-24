from tkinter import *
from deep_translator import GoogleTranslator

def translate():
    text = input_text.get("1.0", END)

    translated = GoogleTranslator(
        source='english',
        target='hindi'
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translator")
root.geometry("500x400")

Label(root, text="Enter English Text").pack()

input_text = Text(root, height=5, width=40)
input_text.pack()

Button(root, text="Translate", command=translate).pack()

output_text = Text(root, height=5, width=40)
output_text.pack()

root.mainloop()