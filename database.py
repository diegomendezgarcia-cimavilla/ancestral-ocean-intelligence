import sqlite3

DB="ocean_ai.db"

def init_db():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS records(
        date TEXT,
        energy INTEGER,
        mood INTEGER,
        stress INTEGER,
        sleep INTEGER,
        nature INTEGER,
        surf INTEGER,
        fishing INTEGER,
        cannabis INTEGER,
        food INTEGER,
        notes TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_record(data):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("""
    INSERT INTO records VALUES(
    date('now'),
    ?,?,?,?,?,?,?,?,?,?
    )
    """,data)
    conn.commit()
    conn.close()

def load_records():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    rows=c.execute("SELECT * FROM records").fetchall()
    conn.close()
    return rows
