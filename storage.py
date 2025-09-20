import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("db/notemate.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY,
                  title TEXT,
                  content TEXT,
                  created_at TEXT,
                  diagram_path TEXT)""")
    conn.commit()
    conn.close()

def save_note(title, content, diagram_path=None):
    conn = sqlite3.connect("db/notemate.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes (title, content, created_at, diagram_path) VALUES (?, ?, ?, ?)",
              (title, content, datetime.now().isoformat(), diagram_path))
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect("db/notemate.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    rows = c.fetchall()
    conn.close()
    return rows

init_db()
save_note("Test Note", "This is a test")
print(get_notes())
