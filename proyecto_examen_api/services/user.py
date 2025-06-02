from config.conn import connection_db
from schema.users_sch import schema_user

def tabla_users():
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def getusuarios():
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return schema_user(result)

def postusuario(name, surname):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", (name, surname))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "Usuari inserit correctament"}

def putusuario(user_id, name, surname):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, surname = %s WHERE id = %s", (name, surname, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "Usuari actualitzat correctament"}

def deleteusuario(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "Usuari eliminat correctament"}
