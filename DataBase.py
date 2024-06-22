import sqlite3
class dbBackend:
    
    # Creazione del database e connessione
    conn = sqlite3.connect('nome_del_database.db')
    cursor = conn.cursor()
    # Creazione della tabella
    cursor.execute("""
    CREATE TABLE utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        data_di_nascita TEXT
    )
""")

    # Inserimento dei dati
    cursor.execute("""
    INSERT INTO utenti (nome, email, data_di_nascita)
    VALUES ('Mario Rossi', 'mario.rossi@example.com', '1980-05-15')
    """)

    # Conferma delle modifiche
    conn.commit()

    # Chiusura della connessione
    cursor.close()
    conn.close()  