import tkinter as tk
from recorder import recognize_speech
from storage import save_note
from tts import speak
from diagram import convert_to_sketch
from tkinter import filedialog, messagebox

def run_gui():
    root = tk.Tk()
    root.title("NoteMate")

    text_area = tk.Text(root, height=15, width=60)
    text_area.pack()

    def record_note():
        note = recognize_speech()
        text_area.insert(tk.END, note + "\n")

    def save_current_note():
        content = text_area.get("1.0", tk.END).strip()
        if content:
            save_note("Lecture Note", content)
            messagebox.showinfo("Saved", "Note saved successfully!")

    def read_note():
        content = text_area.get("1.0", tk.END).strip()
        if content:
            speak(content)

    def attach_diagram():
        file = filedialog.askopenfilename()
        if file:
            sketch_path = convert_to_sketch(file, "attached_sketch.png")
            messagebox.showinfo("Diagram", f"Diagram saved as sketch: {sketch_path}")

    tk.Button(root, text="🎤 Record", command=record_note).pack()
    tk.Button(root, text="💾 Save Note", command=save_current_note).pack()
    tk.Button(root, text="🔊 Read Note", command=read_note).pack()
    tk.Button(root, text="🖼️ Attach Diagram", command=attach_diagram).pack()

    root.mainloop()
