from flask import Flask, render_template, request, redirect, url_for
from recorder import recognize_speech
from storage import init_db, save_note, get_notes
from tts import speak
from diagram import convert_to_sketch
import os


app = Flask(__name__)
init_db()

@app.route("/")
def index():
    notes = get_notes()
    return render_template("index.html", notes=notes)

@app.route("/record")
def record():
    text = recognize_speech()
    save_note("Lecture Note", text)
    return redirect(url_for("index"))

@app.route("/speak/<int:note_id>")
def speak_note(note_id):
    notes = get_notes()
    note = [n for n in notes if n[0] == note_id][0]
    speak(note[2])  # note[2] is content
    return redirect(url_for("index"))

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(url_for("index"))
    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))
    path = os.path.join("uploads", file.filename)
    file.save(path)
    sketch_path = convert_to_sketch(path, f"uploads/sketch_{file.filename}")
    save_note("Diagram Note", f"Attached diagram: {sketch_path}", sketch_path)
    return redirect(url_for("index"))

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
